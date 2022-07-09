from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("""<html> 
                <title>Increase The Peace</title>
                <h1>Increase The Peace</h1> 
            </html>""")
