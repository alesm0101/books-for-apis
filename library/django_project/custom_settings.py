from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


OWN_INSTALLED_APPS = [
    # 3rd party
    "rest_framework",
    "whitenoise.runserver_nostatic",  # <- whitenoise
    # local
    "books.apps.BooksConfig",
    "apis.apps.ApisConfig",
]

# whitenoise
OWN_MIDDLEWARE = ["whitenoise.middleware.WhiteNoiseMiddleware"]
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(BASE_DIR.joinpath("static"))]
STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ALLOWED_HOSTS = [".onrender.com", "localhost", "127.0.0.1"]
