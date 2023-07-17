from django.urls import path
from api_gateway.views.item_service_views import ItemServiceView, ItemServiceRetrieveUpdateDeleteView
from api_gateway.views.user_service_views import UserServiceView, UserServiceRetrieveUpdateDeleteView
from api_gateway.views.transaction_service_views import TransactionServiceView

urlpatterns = [
    path("/item-service", ItemServiceView.as_view(), name="item-service"),
    path("/item-service/<item_uuid>", ItemServiceRetrieveUpdateDeleteView.as_view(), name="modify-item-by-uuid"),
    path("/user-service", UserServiceView.as_view(), name="user-service"),
    path("/user-service/<user_uuid>", UserServiceRetrieveUpdateDeleteView.as_view(), name="modify-user-by-uuid"),
    path("/transaction-service", TransactionServiceView.as_view(), name="transaction-service")
]
