from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.base import TemplateResponseMixin, TemplateView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template.response import TemplateResponse

from .forms import DashboardFilter

class HomePageView(TemplateView):
    template_name = "base.html"


class IndexView(TemplateView):
    template_name = 'scrape/index.html'


class BlankSailingView(IndexView):


    template_name = 'scrape/blanksailing.html'

class VesselRouteView(IndexView):

    template_name = 'scrape/vesselroute.html'





def index(request):
    
    return render(request, 'scrape/index.html')


def blanksailing(request):

    return render(request,'scrape/blanksailing.html')

def vesselroute(request):

    return render(request,'scrape/vesselroute.html')
