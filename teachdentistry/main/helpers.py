from pagetree.helpers import get_hierarchy
from teachdentistry.main.models import UserProfile
from django.core.exceptions import MultipleObjectsReturned


def is_section_unlocked(profile, section):
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


def primary_nav_sections(profile):
    sections = []
    hierarchy = get_hierarchy()
    modules = hierarchy.get_root().get_children()
    for x in modules:
        sections.append({
            'id': x.id,
            'label': x.label,
            'url': x.get_absolute_url(),
            'locked': not is_section_unlocked(profile, x),
            'complete': is_section_unlocked(profile, x.get_next_sibling())})
    return sections


def get_or_create_profile(user, section):
    if user.is_anonymous():
        return None
    try:
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if created:
            first_leaf = section.hierarchy.get_first_leaf(section)
            ancestors = first_leaf.get_ancestors()
            for a in ancestors:
                user_profile.save_visit(a)
    except MultipleObjectsReturned:
        user_profile = UserProfile.objects.filter(user=user)[0]

    return user_profile


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
