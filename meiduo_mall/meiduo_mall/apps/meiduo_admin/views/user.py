from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from meiduo_admin.serializers.user import UserSerializer
from meiduo_admin.utils.pagination import MeiduoPagination
from users.models import User


class UserView(APIView):
    def get(self,request):
        #permission_classes = [IsAuthenticated]
        queryset = User.objects.filter(is_staff=False)
        keyword = request.query_params.get('keyword')
        if keyword:
            queryset = User.objects.filter(is_staff=False,username__contains=keyword).order_by('-id')
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data)
    pagination_class = MeiduoPagination

    def post(self,request):
        #先从request请求对象中获取数据，使用request.data
        param_dict  = request.data
        #然后使用反序列化器，需要将参数传递给data,与序列化器不一样
        serializer = UserSerializer(data=param_dict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return  Response(serializer.errors)




"""
上面的简写
"""
#class UserView(APIView):
#   def get_queryset(self):
#     # self.request,self.args,self.kwargs
#     # 普通会员
#     queryset = User.objects.filter(is_staff=False)
#     # 查询用户名条件
#     keyword = self.request.query_params.get('keyword')
#     if keyword:
#         queryset = queryset.filter(username__contains=keyword)
#     # 排序：最新的放在最前面
#     queryset = queryset.order_by('-id')
#     # 返回查询集
#     return queryset
#
# serializer_class = UserSerializer

