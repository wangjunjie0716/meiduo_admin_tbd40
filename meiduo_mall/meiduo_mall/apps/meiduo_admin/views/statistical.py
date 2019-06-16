from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import User
from orders.models import OrderInfo
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

class IncrementView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        now_date = date.today()
        count = User.objects.filter(is_staff=False,date_joined__gte=now_date    ).count()
        return Response(
            {
                'count': count,
                'today': now_date
            }
        )
class UserActiveCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        day_active = date.today()
        count = User.objects.filter(is_staff=False, last_login__gte=day_active).count()
        return Response(
            {
                'count': count,
                'today': day_active
            }
        )

class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        day_ordered = date.today()
        count = User.objects.filter(orders__create_time__gte = day_ordered).count()
        return Response(
            {
                'count': count,
                'today': day_ordered
            }
        )
