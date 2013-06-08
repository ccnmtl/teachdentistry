from annoying.decorators import render_to
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from pagetree.helpers import get_section_from_path, get_module, needs_submit, \
    submitted
from quizblock.models import Submission
from teachdentistry.main.helpers import get_or_create_profile, has_responses, \
    allow_redo, is_section_unlocked, primary_nav_sections
from teachdentistry.main.models import UserProfile


@render_to('main/index.html')
def index(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return {'modules': primary_nav_sections(profile)}


@login_required
def page(request, path):
    section = get_section_from_path(path)
    hierarchy = section.hierarchy
    module = get_module(section)

    user_profile = get_or_create_profile(user=request.user, section=section)
    accessible = is_section_unlocked(user_profile, section)
    if accessible:
        user_profile.save_visit(section)

    can_edit = False
    if not request.user.is_anonymous():
        can_edit = request.user.is_staff

    first_leaf = hierarchy.get_first_leaf(section)
    ancestors = first_leaf.get_ancestors()

    # Skip to the first leaf, make sure to mark these sections as visited
    if (section != first_leaf):
        user_profile.save_visits(ancestors)
        return HttpResponseRedirect(first_leaf.get_absolute_url())

    if accessible and request.method == "POST":
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

        items = dict(section=section,
                     module=module,
                     accessible=accessible,
                     needs_submit=needs_submit(section),
                     is_submitted=submitted(section, request.user),
                     modules=primary_nav_sections(user_profile),
                     root=section.hierarchy.get_root(),
                     instructor_link=instructor_link,
                     can_edit=can_edit,
                     allow_redo=allow_redo(section),
                     next_unlocked=is_section_unlocked(user_profile, section.get_next()))

        if not accessible:
            template_name = 'main/inaccessible.html'
        elif path.startswith('map'):
            template_name = 'main/map.html'
        elif path.startswith('profile'):
            template_name = 'main/profile.html'
        else:
            template_name = 'main/page.html'

        return render_to_response(template_name,
                                  items,
                                  context_instance=RequestContext(request))


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
    user_profile = get_or_create_profile(user=request.user, section=section)

    return dict(section=section,
                module=get_module(section),
                modules=primary_nav_sections(user_profile),
                root=section.hierarchy.get_root(),
                can_edit=True)
