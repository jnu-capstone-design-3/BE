import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from account.models import User,FriendList


class MakeTokenView(APIView):
    permission_classes = [AllowAny,]
    
    def post(self, request):

        try:
            user = User.objects.get(id = request.data["user_id"])

            if user:
                unique_id = str(uuid.uuid4()).replace("-", "")

                dict = {
                    "user": user.id,
                    "room_id": unique_id
                }
                
                return Response(dict)
            
        except User.DoesNotExist:
            return Response("ㅠㅠ")