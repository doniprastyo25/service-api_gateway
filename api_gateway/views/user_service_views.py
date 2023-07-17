from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api_gateway.helper.base_request import request_service

class UserServiceView(APIView):
    permission_classes= [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            data_response = request_service(
                service='user',
                user_id=request.user.id,
                method='create_user',
                params=[request.data]
            )
            return Response(data_response['result'])
        except Exception as e:
            return e
    
    def get(self, request, *args, **kwargs):
        try:
            data_response = request_service(
                service='user',
                user_id=request.user.id,
                method='find_all_user',
                params=[]
            )
            return Response(data_response['result'])
        except Exception as e:
            return e
    

class UserServiceRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_uuid, *args, **kwargs):
        try:
            data_response = request_service(
                service='user',
                user_id=request.user.id,
                method='find_user_by_uuid',
                params=[user_uuid]
            )
            return Response(data_response)
        except Exception as e:
            return e
    
    def patch(self, request, user_uuid, *args, **kwargs):
        try:
            data_response = request_service(
                service='user',
                user_id=request.user.id,
                method='update_user_by_id',
                params=[user_uuid, request.data]
            )
            return Response(data_response)
        except Exception as e:
            return e
    
    def delete(self, request, user_uuid, *args, **kwargs):
        try:
            data_response = request_service(
                service='user',
                user_id=request.user.id,
                method='delete_user_by_id',
                params=[user_uuid]
            )
            return Response(data_response)
        except Exception as e:
            return e
    