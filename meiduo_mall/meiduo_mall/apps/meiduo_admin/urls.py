from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from meiduo_admin.views  import statistical

urlpatterns = [
    url('^authorizations/$', obtain_jwt_token),
    url('^statistical/total_count/$', statistical.TotalView.as_view()),
    url('^statistical/day_increment/$', statistical.IncrementView.as_view()),
    url('^statistical/day_active/$', statistical.IncrementView.as_view()),
    url('^statistical/day_orders/$', statistical.OrderView.as_view()),

]

