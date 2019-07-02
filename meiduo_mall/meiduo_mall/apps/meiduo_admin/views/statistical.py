from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from goods.models import GoodsVisitCount
from users.models import User
from orders.models import OrderInfo
from datetime import date,timedelta
from meiduo_admin.serializers.statistical import GoodsVisitCountModelSerializer

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


class MonthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 月增用户统计：在过去的一个月，每天有多少新增用户
        today = date.today()
        # 定义列表，存在每天的人数
        month_list = []
        # 计算一个月（30天）中的第一天
        month_day1 = today - timedelta(days=29)
        # 遍历，30天
        for i in range(30):  # [0,29]
            # 某天的开始、结束
            begin_date = month_day1 + timedelta(days=i)
            end_date = month_day1 + timedelta(days=i + 1)
            # 统计某天的新增人数
            count = User.objects.filter(is_staff=False, date_joined__gte=begin_date, date_joined__lt=end_date).count()
            month_list.append({
                'count': count,
                'date': begin_date
            })

        return Response(month_list)


class GoodsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 日分类商品访问量===>GoodsVisitCount
        today = date.today()
        # 今天，每个分类的访问次数
        visit_list = GoodsVisitCount.objects.filter(date=today)

        serializer = GoodsVisitCountModelSerializer(visit_list, many=True)

        return Response(serializer.data)

"""
增加用户:１.对数据库进行增加操作 ;2.使用put方法，3.定义视图，路由，序列化器

思路：

"""
