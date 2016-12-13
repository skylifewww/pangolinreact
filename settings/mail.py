ADMINS = (
    ('Admin', 'admin@pangolin.com'),
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'skylifewww@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'skylifewww@gmail.com'
EMAIL_HOST_PASSWORD = 'skywww123'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_PORT = 587
