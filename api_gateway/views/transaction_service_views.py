import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api_gateway.helper.base_request import request_service

class TransactionServiceView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        try:
            data_response = request_service(
                service='transaction',
                user_id=request.user.id,
                method='create_transaction',
                params=[request.data]
            )
            return Response(data_response['result'])
        except Exception as e:
            return e