from django.http import HttpResponse

def handler404(requst, exception):
    return HttpResponse("<h1>You need to be logged in to view the contents of each section.</h1>")
