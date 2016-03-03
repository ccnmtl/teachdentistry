# Django settings for teachdentistry project.
import os.path
from ccnmtlsettings.shared import common

project = 'teachdentistry'
base = os.path.dirname(__file__)
locals().update(common(project=project, base=base))

AUTH_PROFILE_MODULE = "main.UserProfile"
ACCOUNT_ACTIVATION_DAYS = 7

PROJECT_APPS = [
    'teachdentistry.main',
]

ALLOWED_HOSTS += ['.teachdentistry.org']  # noqa

USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS += [  # noqa
    'teachdentistry.main.views.context_processor'
]

INSTALLED_APPS += [  # noqa
    'sorl.thumbnail',
    'tagging',
    'typogrify',
    'bootstrapform',
    'lettuce.django',
    'django_extensions',
    'teachdentistry.main',
    'pagetree',
    'pageblocks',
    'quizblock',
    'treebeard',
    'localflavor',
]

PAGEBLOCKS = [
    'pageblocks.TextBlock',
    'pageblocks.HTMLBlock',
    'pageblocks.PullQuoteBlock',
    'pageblocks.ImageBlock',
    'pageblocks.ImagePullQuoteBlock',
    'quizblock.Quiz',
]


LETTUCE_APPS = (
    'teachdentistry.main',
)

THUMBNAIL_SUBDIR = "thumbs"
