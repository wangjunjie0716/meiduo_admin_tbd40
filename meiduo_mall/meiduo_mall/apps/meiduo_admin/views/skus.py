from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from goods.models import SKU
from meiduo_admin.serializers.skus import SkuModelSerializer
from meiduo_admin.utils.pagination import MeiduoPagination


class SkuModelViewSet(ModelViewSet):
    def get_queryset(self):
        queryset = SKU.objects
        keyword = self.request.query_params.get('keyword')
        if keyword:
            queryset = queryset.filter(Q(name__contain = keyword)| Q(caption__contain = keyword))
            return queryset

        else:
            return SKU.objects.all().order_by('-id')

    serializer_class = SkuModelSerializer
    pagination_class = MeiduoPagination

