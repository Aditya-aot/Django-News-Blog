
from django.shortcuts import render
from .models import task_model
from .forms import TaskForm
from django.http import HttpResponseRedirect

from bs4 import BeautifulSoup
import pandas as pd
import requests
# Create your views here.

def home(request):
    form = TaskForm()
    task_data = task_model.objects.all()

    if request.method == 'POST' :
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()


    #  
    url='https://www.bbc.com/news/world/asia'
    page = requests.get(url)
    page
    page.text
    soup = BeautifulSoup(page.text,'html.parser')

    asia_news = soup.find_all("div", {"class": "gs-c-promo gs-t-News nw-c-promo gs-o-faux-block-link gs-u-pb gs-u-pb+@m nw-p-default gs-c-promo--inline gs-c-promo--stacked@m gs-c-promo--flex"})
    news_site = {}
    n=0 
    for news in asia_news :
        url='https://www.bbc.com/news/world/asia'
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        
        heading = news.find('h3', {'class': 'gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text'}).text
        link =    news.find('a', {'class': 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'}).get('href')
        n=1+n
        news_site[n] = [heading,link]


    context = { 'form':form ,
                'task_data' : task_data[::-1] ,
                'news' : news_site ,

    }


    return render(request, 'home.html', context)


#creating delete view
def delete_view(request , task_id) :
    task_to_delete = task_model.objects.get(id=task_id)
    task_to_delete.delete()
    return HttpResponseRedirect('/task/') 



#to be coming 
#any idea 
