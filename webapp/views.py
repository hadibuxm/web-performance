from django.shortcuts import render, HttpResponse
from . modules import makeconnection, functions
# Create your views here.
def index(request):
   
    return render(request, "webapp/index.html", )

def main(request):
    if request.method == "POST":
        if 'analyse' in request.POST:
            url = str(request.POST.get("url"))
            try:
                data = makeconnection.fetch_metrics(url)
            except:
                return HttpResponse("<h1>Server not respoding, try again in sometime</h1>")
            original_data = data
            cleaned_data = functions.create_context(data)
            #context = functions.create_context(data)
            #print(data['loadingExperience']['metrics'])
            print('loading experience keys')
            print(data['loadingExperience'].keys())
            print('overall_category')
            print(data['loadingExperience']['overall_category'])
            #print('loading experience metrics')
            # print(data['loadingExperience']['metrics'])
            #id = data['loadingExperience']['id']
            #loadingExperience = data['loadingExperience']
            #originalloadingexperience = data['originLoadingExperience']
            #lighthouseresult = data['lighthouseResult']
            #context = {'data': data,} #'loadingExperience': loadingExperience,
                       #'lighthouseresult': lighthouseresult, 'originalloadingexperience': originalloadingexperience}
            return render(request, "webapp/main.html", {'data': original_data, 'loadingExperience': cleaned_data['loadingExperience']})
    else:
        return render(request, "webapp/main.html")
