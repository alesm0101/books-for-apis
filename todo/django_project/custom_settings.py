from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


CUSTOM_INSTALLED_APPS = [
    # 3rd party
    "rest_framework",
    "whitenoise.runserver_nostatic",  # <- whitenoise
    "corsheaders",
    # local
    "todos.apps.TodosConfig",
]

# whitenoise
OWN_MIDDLEWARE = ["whitenoise.middleware.WhiteNoiseMiddleware"]
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(BASE_DIR.joinpath("static"))]
STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

OWN_ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

OWN_MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
]
CORS_ALLOWED_ORIGINS = ("http://localhost:3000", "http://localhost:8000")
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]
