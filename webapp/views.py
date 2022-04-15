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
            lighthouse_data = data['lighthouseResult']['audits']['diagnostics']
            cleaned_data = functions.create_context(data)
            print('SEE HERE')
            print(list(data['lighthouseResult']['audits'].keys()))
            #return render(request, "webapp/main.html", {'data': lighthouse_data, })
            return render(request, "webapp/main.html", cleaned_data)
    else:
        return render(request, "webapp/main.html")

def readmore(request):
    return render(request, 'webapp/readmore.html')