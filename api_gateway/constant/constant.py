from django.conf import settings

SERVICE_LIST = ["user", "item", "transaction"]

SERVICE_URL = {
    "user": settings.USER_SERVICE_URL,
    "item": settings.ITEM_SERVICE_URL,
    "transaction": settings.TRANSACTION_SERVICE_URL
}