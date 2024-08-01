from django.shortcuts import get_object_or_404, render

from app.models import *

def home(request):
    return render(request, 'home.html', )

def hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels.html', {'hotels':hotels})



def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    rooms = Room.objects.filter(hotel_id=pk)
    return render(request, 'hotelPage.html', {'hotel': hotel, 'rooms': rooms})

