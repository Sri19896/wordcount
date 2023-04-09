from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    lw = fulltext.split()
    wd = {}
    for i in lw:
        if i in wd:
            wd[i] += 1
        else:
            wd[i] = 1
    sorteddc = sorted(wd.items(), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(lw), 'sorteddc': sorteddc})


def about(request):
    return render(request, 'about.html')
