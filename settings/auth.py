AUTHENTICATION_BACKENDS = (
    'social.backends.open_id.OpenIdAuth',
    'social.backends.vk.VKOAuth2',    
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
    'social.backends.email.EmailAuth',
    'social.backends.username.UsernameAuth',
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
)

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/signin/'
LOGIN_ERROR_URL = '/signin/failed/'

ANONYMOUS_USER_ID = -1

AUTH_USER_MODEL = 'users.User'