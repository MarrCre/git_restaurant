from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'name':'bratari'}
    return render(request, r'main\home.html', context)
