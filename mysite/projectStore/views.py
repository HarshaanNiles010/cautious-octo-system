from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#request Handler
#User doesn't see this
def trial_messaage(request):
    #return HttpResponse('This is a Trial Message')
    return render(request, 'index.html', {'name':'Harshaan'})
