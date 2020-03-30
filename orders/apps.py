from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'

    def ready(self):
        """
        importing signal module so it can be invoked when required
        """
        # noinspection PyUnresolvedReferences
        import orders.signals
