from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    if request.method == "POST":
        my_dict = {1: 'banana', 2: 'cereal', 3: 'protein'}
        key = int(request.POST['k'])

        return HttpResponse(json.dumps(my_dict[key]), content_type="application/json")

    else:
        return render(request, "myApp/index.html",{})
