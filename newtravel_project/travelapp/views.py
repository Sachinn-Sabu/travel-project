from django.shortcuts import render
from travelapp.models import Place, Members


# Create your views here.
def home(request):
    obj = Place.objects.all()
    obj1 = Members.objects.all()
    return render(request, 'index.html', {'result': obj,'res':obj1})
