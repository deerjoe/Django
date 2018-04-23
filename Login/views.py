from django.shortcuts import render


def index(request):
    context = {'user': 'Jason','password': 'Jason'}

    return render(request, 'Login/login-1.html', context)
# Create your views here.
