from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from meiduo_admin.views  import statistical,user,skus

urlpatterns = [
    url('^authorizations/$', obtain_jwt_token),
    url('^statistical/total_count/$', statistical.TotalView.as_view()),
    url('^statistical/day_increment/$', statistical.IncrementView.as_view()),
    url('^statistical/day_active/$', statistical.IncrementView.as_view()),
    url('^statistical/day_orders/$', statistical.OrderView.as_view()),
    url('^statistical/month_increment/$', statistical.MonthView.as_view()),
    url('^statistical/goods_day_views/$', statistical.GoodsView.as_view()),
        url('^users/$', user.UserView.as_view()),
#     url('^skus/$',sku.SkuView.as_view()),
 ]

router = DefaultRouter()
#router.register('goods/specs', specs.SpecsModelViewSet, base_name='specs')
router.register('skus', skus.SkuModelViewSet, base_name='skus')


urlpatterns += router.urls