from django.utils.translation import ugettext_lazy as _

from settings.base import rel


TIME_ZONE = 'UTC'

LANGUAGES = (
    ('en', _('English')),
)

LANGUAGE_CODE = 'en-US'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    rel('locale'),
)
