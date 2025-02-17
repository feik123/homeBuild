from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'homeBuild.accounts'

    def ready(self):
        import homeBuild.accounts.signals
