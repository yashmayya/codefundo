from django.shortcuts import render, redirect
from .forms import UserdataForm, UpdateForm
from django.views.generic import TemplateView, UpdateView, FormView
from django.core import serializers
from .models import UserData
from .kmeans import cluster_funct
import json
from django.http import JsonResponse


# Create your views here.
clustsize = 50

def new_userdata(request):

    if request.method == "POST":
        form = UserdataForm(request.POST)
        if form.is_valid():
            details = form.save()
            num = UserData.objects.filter().count()

            if(num % clustsize == 0):
                data = UserData.objects.values('latitude', 'longitude')

                inp = []

                for item in data:
                    tmp = [item['latitude'], item['longitude']]
                    inp.append(tmp)

                clusters = cluster_funct(inp, int(num/clustsize)+1)

                with open('/home/yash/localserver/codefundo/clustercentres.json', 'w') as outfile:
                    json.dump(clusters.tolist(), outfile)

            data = UserData.objects.values('latitude', 'longitude')

            inp = []

            for item in data:
                tmp = [float(item['latitude']), float(item['longitude'])]
                inp.append(tmp)

            with open('/home/yash/localserver/codefundo/data.json', 'w') as outfile:
                json.dump(inp, outfile)

            # data = {'latitude':float(details.latitude), 'longitude':float(details.longitude)}
            # with open('data.txt', 'a') as outfile:
            #     json.dump(data, outfile)


            return redirect('thanks')


    else:
        form = UserdataForm()

    return render(request, 'register.html', {'form':form})



def listall(request):
    data = UserData.objects.values('latitude', 'longitude')
    return render(request, 'listmodel.html', {'data':data})

class ThanksView(TemplateView):
    template_name = "thanks.html"

class HomeView(TemplateView):
    template_name = "home.html"
