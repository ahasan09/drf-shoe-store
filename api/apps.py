from django.apps import AppConfig


class ApiConfig(AppConfig):
    # Keep AutoField (the pre-Django-3.2 default) so existing migrations and
    # databases don't need a BigAutoField migration.
    default_auto_field = 'django.db.models.AutoField'
    name = 'api'
