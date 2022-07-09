from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def news_page(request):
    return HttpResponse("""

            <html>
                <title>Increase The News</title>
                <h1>ITP News</h1>
            </html>

            """)