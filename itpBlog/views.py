from django.shortcuts import render
#from django.http import HttpResponse

def blog_page(request):
    context = {}
    return render(request, "blog_page.html", context)