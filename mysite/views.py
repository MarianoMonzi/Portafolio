from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def en_version(request):
    return render(request, 'en_version.html')