from datetime import datetime
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from .models import MONTH_DICT, MONTH_LIST, YEARS,CARRIER_LIST
from .forms import BSfilterForm




class HomePageView(TemplateView):
    template_name = "base.html"

class IndexView(TemplateView):
    template_name = 'scrape/index.html'

class VesselRouteView(IndexView):
    template_name = 'scrape/vesselroute.html'



def index(request):
    return render(request, 'scrape/index.html')




def blanksailing(request):
    inital_data = {
        'monthF':datetime.now().month,
        'monthT':datetime.now().month
    }
    form = BSfilterForm(request.GET or None, initial=inital_data)
    if request.method =='POST':
        form = BSfilterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form':form,
        'months':MONTH_DICT
        }
    return render(request,'scrape/blanksailing.html',context)



def vesselroute(request):

    return render(request,'scrape/vesselroute.html')



def filter(request):
    form = BSfilterForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {'form':form}
    return render(request,'scrape/filter.html',context)


# class BlankSailingView(ListView):
#     blanksailing()
#     template_name = 'scrape/blanksailing.html'
