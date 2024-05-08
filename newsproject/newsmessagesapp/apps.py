from django.apps import AppConfig


class NewsmessagesappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsmessagesapp'

    def ready(self):
        import newsmessagesapp.signals
