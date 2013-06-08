from annoying.decorators import render_to
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from pagetree.helpers import get_section_from_path, get_module, needs_submit, \
    submitted
from quizblock.models import Submission
from teachdentistry.main.models import UserProfile
import django.core.exceptions


# returns important setting information for all web pages.
def django_settings(request):
    whitelist = ['GOOGLE_API_KEY']

    rv = {'settings': dict([(k, getattr(settings, k, None))
                            for k in whitelist])}

    return rv


def get_or_create_profile(user, section):
    if user.is_anonymous():
        return None
    try:
        user_profile, created = UserProfile.objects.get_or_create(user=user)
    except django.core.exceptions.MultipleObjectsReturned:
        user_profile = UserProfile.objects.filter(user=user)[0]
        created = False
    if created:
        first_leaf = section.hierarchy.get_first_leaf(section)
        ancestors = first_leaf.get_ancestors()
        for a in ancestors:
            user_profile.save_visit(a)
    return user_profile


def _unlocked(profile, section):
    """ if the user can proceed past this section """
    if profile is None:
        return False
    if not section:
        return True
    if section.is_root():
        return True
    if profile.has_visited(section):
        return True

    previous = section.get_previous()
    if not previous:
        return True
    else:
        if not profile.has_visited(previous):
            return False

    # if the previous page had blocks to submit
    # we only let them by if they submitted
    for p in previous.pageblock_set.all():
        if hasattr(p.block(), 'unlocked'):
            if not p.block().unlocked(profile.user):
                return False

    return profile.has_visited(previous)


def has_responses(section):
    quizzes = [p.block() for p in section.pageblock_set.all(
    ) if hasattr(p.block(), 'needs_submit') and p.block().needs_submit()]
    return quizzes != []


def allow_redo(section):
    """ if blocks on the page allow redo """
    allowed = True
    for p in section.pageblock_set.all():
        if hasattr(p.block(), 'allow_redo'):
            if not p.block().allow_redo:
                allowed = False
    return allowed


@login_required
@render_to('main/page.html')
def page(request, path):
    section = get_section_from_path(path)
    hierarchy = section.hierarchy
    root = hierarchy.get_root()
    module = get_module(section)

    user_profile = get_or_create_profile(user=request.user, section=section)
    can_access = _unlocked(user_profile, section)
    if can_access:
        user_profile.save_visit(section)
    else:
        if request.user.is_anonymous():
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect(user_profile.last_location)

    can_edit = False
    if not request.user.is_anonymous():
        can_edit = request.user.is_staff

    if section.id == root.id:
        # trying to visit the root page
        if section.get_first_leaf():
            # just send them to the first child, but save
            # the ancestors first
            first_leaf = section.get_first_leaf()
            ancestors = first_leaf.get_ancestors()
            user_profile.save_visits(ancestors)
            return HttpResponseRedirect(first_leaf.get_absolute_url())

    if request.method == "POST":
        # user has submitted a form. deal with it
        if request.POST.get('action', '') == 'reset':
            section.reset(request.user)
            return HttpResponseRedirect(section.get_absolute_url())

        section.submit(request.POST, request.user)

        next_section = section.get_next()
        if next_section:
            # ignoring proceed and always pushing them along. see PMT #77454
            return HttpResponseRedirect(next_section.get_absolute_url())
        else:
            return HttpResponseRedirect("/")
    else:
        instructor_link = has_responses(section)
        allow_next_link = not needs_submit(
            section) or submitted(section, request.user)

        return dict(section=section,
                    module=module,
                    allow_next_link=allow_next_link,
                    needs_submit=needs_submit(section),
                    is_submitted=submitted(section, request.user),
                    modules=root.get_children(),
                    root=section.hierarchy.get_root(),
                    instructor_link=instructor_link,
                    can_edit=can_edit,
                    allow_redo=allow_redo(section),
                    next_unlocked=_unlocked(
                        user_profile, section.get_next())
                    )


@login_required
@render_to("main/instructor_page.html")
def instructor_page(request, path):
    if not request.user.is_superuser:
        return HttpResponseForbidden

    hierarchy_name, slash, section_path = path.partition('/')
    section = get_section_from_path(section_path, hierarchy=hierarchy_name)

    root = section.hierarchy.get_root()

    if request.method == "POST":
        if 'clear' in request.POST.keys():
            submission = get_object_or_404(
                Submission, id=request.POST['clear'])
            submission.delete()
            return HttpResponseRedirect(
                "/instructor" + section.get_absolute_url())

    quizzes = [p.block() for p in section.pageblock_set.all(
    ) if hasattr(p.block(), 'needs_submit') and p.block().needs_submit()]
    return dict(section=section,
                quizzes=quizzes,
                module=get_module(section),
                modules=root.get_children(),
                root=root)


@staff_member_required
@render_to('main/edit_page.html')
def edit_page(request, path):
    section = get_section_from_path(path)
    root = section.hierarchy.get_root()

    return dict(section=section,
                module=get_module(section),
                modules=root.get_children(),
                root=section.hierarchy.get_root())


@render_to('main/index.html')
def index(request):
    return dict()
