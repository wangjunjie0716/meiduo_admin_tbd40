from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import User
from datetime import date

class TotalView(APIView):
    #验证是否登录
    permission_classes = [IsAuthenticated]
    def get(self,request):
        count = User.objects.filter(is_staff=False).count()
        today = date.today()
        return  Response (
            {
                'count': count,
                'today':today
            }
        )