from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.

def layout(request):
    return render(request, 'learn/layout.html')

def index(request):
    return render(request, 'learn/index.html')

texts = [
    "So you have heard of quantum technology and how it is going to revolutionize, well, everything. How do we know that and how does it work? Jump in here to find out!", 
    "This skill introduces the superposition principle. You'll gain insight into where this principle comes from, why it is necessary, and what you can do with it.", 
    "Start with some fundamentals in how we represent information and by the end of this skill you'll understand how we can encode and process information using quantum physics!"
]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")