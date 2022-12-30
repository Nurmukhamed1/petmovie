# from datetime import timedelta
#
# REST_FRAMEWORK = {
#     "DEFAULT_PAGINATION_CLASS": "utils.pagination.CustomPagination",
#     "PAGE_SIZE": 5,
#     "DEFAULT_RENDERER_CLASSES": [
#         "rest_framework.renderers.JSONRenderer",
#         "rest_framework.renderers.BrowsableAPIRenderer",
#     ],
#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         "rest_framework_simplejwt.authentication.JWTAuthentication",
#     ),
#     "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
# }
#
# SPECTACULAR_SETTINGS = {
#     "TITLE": "Your Project API",
#     "DESCRIPTION": "Your project description",
#     "VERSION": "1.0.0",
#     "SERVE_INCLUDE_SCHEMA": False,
# }
#
# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(hours=12),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
#     "ROTATE_REFRESH_TOKENS": False,
#     "AUTH_HEADER_TYPES": ("Bearer",),
#     "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
#     "USER_ID_FIELD": "id",
#     "USER_ID_CLAIM": "user_id",
#     "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
#     "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
# }
#
# ALLOWED_IPS = [
#     "80.241.44.238",
#     "178.88.188.42",
#     "217.11.77.164",
#     "157.167.85.180",
# ]
#
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = "adexa343@gmail.com"
# EMAIL_HOST_PASSWORD = "sabeoraywzwgbisv"
