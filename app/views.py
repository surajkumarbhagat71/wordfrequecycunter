from django.shortcuts import render , render_to_response
from .models import *
from django.views.generic import View, TemplateView
from .froms import *
import urllib3
import re
from bs4 import BeautifulSoup


def keywordSearch(url):
    http = urllib3.PoolManager()
    response = http.request('GET',url)

    soup = BeautifulSoup(response.data,"html.parser")
    data = re.sub("[^\w]", " ",  soup.text.lower()).split()

    #result = []
    for x in data:
        for y in ['is','are','and','an','if','you','the','on','in','a','of','to','no','it','s',' the']:
            if x == y:
                data.remove(x)

    freq = {}
    for item in data:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1


    a = sorted(freq.items(), key=lambda x: x[1],reverse=True)

    return a


# Create your views here.

class Homepage(TemplateView):
    template_name = 'home.html'


class Home(View):
    def get(self,request):
        form = WordStockForm()
        return render(request,'frequency.html',{"form":form})



class WordFinder(View):
    def post(self,request):
        list = []
        url = request.POST.get('word')

        a = keywordSearch(url)

        count = 1
        form = WordStockForm(request.POST or None)
        for word, value in a:
            if count > 10:
                break
            try:
                WordStok.objects.get(word=word)
            except:
                a = WordStok(word=word).save()

            x = WordStok.objects.get(word=word)
            list.append(x.word_id)

            count+=1

        context  = []
        for foo in list:
            context += WordStok.objects.filter(word_id = foo)

        return render(request,'result.html',{"words":context})

    #data = {"words": a[:11]}




















