from annoying.decorators import render_to
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from pagetree.helpers import get_section_from_path, get_module, needs_submit, \
    submitted
from quizblock.models import Submission
from registration.signals import user_registered
from teachdentistry.main.helpers import get_or_create_profile, has_responses, \
    allow_redo, is_section_unlocked, primary_nav_sections
from teachdentistry.main.models import UserProfile, DentalEducator, \
    CAREER_STAGE_CHOICES, TeachingResponsibility, TimeCommitment, \
    PrimaryTraineesType, UserProfileForm, ClinicalField


@login_required
@render_to('main/index.html')
def index(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return {'modules': primary_nav_sections(profile)}


def can_user_edit(request):
    can_edit = False
    if not request.user.is_anonymous():
        can_edit = request.user.is_staff
    return can_edit


@login_required
def page(request, path):
    section = get_section_from_path(path)
    hierarchy = section.hierarchy
    module = get_module(section)

    user_profile = get_or_create_profile(user=request.user, section=section)
    accessible = is_section_unlocked(user_profile, section)
    if accessible:
        user_profile.save_visit(section)

    can_edit = can_user_edit(request)

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

        if section.slug == "ce-credit":
            next_section = section.get_next()
            if next_section:
                return HttpResponseRedirect(next_section.get_absolute_url())
        else:
            return HttpResponseRedirect(section.get_absolute_url())
    else:
        instructor_link = has_responses(section)

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
                     next_unlocked=is_section_unlocked(user_profile,
                                                       section.get_next()))

        template_name = template_from_path(accessible, path)
        if accessible and path.startswith('map'):
            items['career_stages'] = CAREER_STAGE_CHOICES
            items['clinical_fields'] = \
                ClinicalField.objects.all().distinct().order_by('name')
            items['teaching_responsibilities'] = \
                TeachingResponsibility.objects.all().order_by('name')
            items['paid_time_commitments'] = TimeCommitment.objects.all()
            items['volunteer_time_commitments'] = TimeCommitment.objects.all()
            items['trainee_types'] = PrimaryTraineesType.objects.all()

        return render_to_response(template_name,
                                  items,
                                  context_instance=RequestContext(request))


def template_from_path(accessible, path):
    if not accessible:
        return 'main/inaccessible.html'
    elif path.startswith('map'):
        return 'main/map.html'
    elif path.startswith('profile'):
        return 'main/profile.html'
    else:
        return 'main/page.html'


@login_required
@render_to("main/instructor_page.html")
def instructor_page(request, path):
    if not request.user.is_superuser:
        return HttpResponseForbidden()

    # TD has only 'main' hierarchy
    section = get_section_from_path(path, hierarchy='main')

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
    user_profile = get_or_create_profile(user=request.user, section=section)

    return dict(section=section,
                module=get_module(section),
                modules=primary_nav_sections(user_profile),
                root=section.hierarchy.get_root(),
                can_edit=True)


@login_required
@render_to('main/profile.html')
def profile(request, educator_id):
    section = get_section_from_path("map/")
    user_profile = get_or_create_profile(user=request.user, section=section)
    if not is_section_unlocked(user_profile, section):
        return HttpResponseRedirect("/")

    educator = get_object_or_404(DentalEducator, id=educator_id)

    return dict(educator=educator,
                module=get_module(section),
                modules=primary_nav_sections(user_profile),
                root=section.hierarchy.get_root())


def update_user_profile(sender, user, request, **kwargs):
    form = UserProfileForm(request.POST)

    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=user)

    user.first_name = form.data['first_name']
    user.last_name = form.data['last_name']
    user.save()

    user_profile.gender = form.data['gender']
    user_profile.primary_discipline = form.data['primary_discipline']
    user_profile.primary_other_dental_discipline =  \
        form.data['primary_other_dental_discipline']
    user_profile.primary_other_discipline = \
        form.data['primary_other_discipline']
    user_profile.year_of_graduation = form.data['year_of_graduation']
    user_profile.dental_school = form.data['dental_school']
    user_profile.postal_code = form.data['postal_code']
    user_profile.plan_to_teach = form.data['plan_to_teach']
    user_profile.qualified_to_teach = form.data['qualified_to_teach']
    user_profile.opportunities_to_teach = form.data['opportunities_to_teach']
    user_profile.possible_to_teach = form.data['possible_to_teach']
    user_profile.ethnicity = form.data['ethnicity']
    user_profile.race = form.data['race']
    user_profile.age = form.data['age']
    user_profile.highest_degree = form.data['highest_degree']
    user_profile.consented = form.data['consented']

    user_profile.state = u','.join(request.POST.getlist('state'))
    user_profile.work_description = \
        u','.join(request.POST.getlist('work_description'))

    user_profile.save()

user_registered.connect(update_user_profile)
