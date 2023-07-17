from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api_gateway.helper.base_request import request_service

class ItemServiceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            data_response = request_service(
                service='item', 
                user_id=request.user.id, 
                method='create_item', 
                params=[request.data]
            )
            return Response(data_response['result'])
        except Exception as e:
            return e

    def get(self, request, *args, **kwargs):
        try:
            data_response = request_service(
                service='item', 
                user_id=request.user.id, 
                method='find_all_item', 
                params=[]
            )
            return Response(data_response)
        except Exception as e:
            return e

class ItemServiceRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, item_uuid, *args, **kwargs):
        try:
            data_response = request_service(
                service='item', 
                user_id=request.user.id, 
                method='find_item_by_uuid', 
                params=[item_uuid]
            )
            return Response(data_response)
        except Exception as e:
            return e

    def patch(self, request, item_uuid, *args, **kwargs):
        try:
            data_response = request_service(
                service='item', 
                user_id=request.user.id, 
                method='update_item_by_uuid', 
                params=[item_uuid, request.data]
            )
            return Response(data_response)
        except Exception as e:
            return e
    
    def delete(self, request, item_uuid, *args, **kwargs):
        try:
            data_response = request_service(
                service='item', 
                user_id=request.user.id, 
                method='delete_item_by_uuid', 
                params=[item_uuid]
            )
            return Response(data_response['result'])
        except Exception as e:
            return e