from django import template
from teachdentistry.main.helpers import is_section_unlocked
from teachdentistry.main.models import UserProfile

register = template.Library()


class UnlockedNode(template.Node):
    def __init__(self, section, nodelist_true, nodelist_false=None):
        self.nodelist_true = nodelist_true
        self.nodelist_false = nodelist_false
        self.section = section

    def render(self, context):
        s = context[self.section]
        r = context['request']
        u = r.user
        profile, created = UserProfile.objects.get_or_create(user=u)
        if is_section_unlocked(profile, s):
            return self.nodelist_true.render(context)
        else:
            return self.nodelist_false.render(context)


@register.tag('ifunlocked')
def unlocked(parser, token):
    section = token.split_contents()[1:][0]
    nodelist_true = parser.parse(('else', 'endifunlocked'))
    token = parser.next_token()
    if token.contents == 'else':
        nodelist_false = parser.parse(('endifunlocked',))
        parser.delete_first_token()
    else:
        nodelist_false = None
    return UnlockedNode(section, nodelist_true, nodelist_false)
