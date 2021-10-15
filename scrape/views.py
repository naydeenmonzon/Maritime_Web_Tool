from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.base import TemplateResponseMixin, TemplateView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template.response import TemplateResponse
from .models import TOOLS


class HomePageView(TemplateView):
    template_name = "base.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TOOLS.objects.all()
        return context

class TemplateResponse(TemplateResponseMixin, TOOLS):
    template_name = 'index.html'
    def get_template_names(self) -> TOOLS:
        return super().get_template_names()

class IndexView(TemplateView):
    template_name = 'scrape/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TOOLS.objects.all()
        return {'context': context}

class BlankSailingView(IndexView):


    template_name = 'scrape/blanksailing.html'

class VesselRouteView(IndexView):

    template_name = 'scrape/vesselroute.html'






def index(request):
    
    return render(request, 'scrape/index.html')


def blanksailing(request):

    return render(request,'scrape/blanksailing.html')

def vesselroute(request):
    tools = TOOLS.objects.all()
    return render(request,'scrape/vesselroute.html',{'tools':tools})
