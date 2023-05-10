from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from account.models import User,FriendList


class MakeTokenView(APIView):
    permission_classes = [IsAuthenticated,]
    
    def post(self, request):
        user_id = request.data['user_id']

        try:
            user = User.objects.get(id=user_id)
            friedlist = FriendList.objects.filter(user_id=user_id)
            
            print(friedlist)

            return Response('ok')
        except User.DoesNotExist:
            return Response('error')