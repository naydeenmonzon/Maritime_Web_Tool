from django.urls import path
from django.conf import settings
from django.conf.urls import static
from django.urls.conf import re_path
from . import  views
from scrape.views import filter, blanksailing


app_name = 'scrape'


urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('blanksailing/',blanksailing, name='blanksailing'),
#    path('blanksailing/',views.BlankSailingView.as_view(), name='blanksailing'),
    path('filter/<slug:slug>',filter,name='filter'),
#    path('<int:yr>/filter/',views.filter,name='filter'),
#    path(r'filter/(?P<yyyy:year>)/(?P<month>)/$',views.filter),
    path('vesselroute/',views.VesselRouteView.as_view(), name='vesselroute'),
]
#+ static(settings.STATIC_URL,document_root='../Maritime_Web_Tool/scrape/static')



