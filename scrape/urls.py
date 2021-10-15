from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'scrape'
urlpatterns = [


    path('', views.IndexView.as_view(), name='index'),

    path('blanksailing/',views.BlankSailingView.as_view(), name='blanksailing'),

    path('vesselroute/',views.VesselRouteView.as_view(), name='vesselroute'),
]+ static(settings.STATIC_URL,document_root='../Maritime_Web_Tool/scrape/staticfiles')