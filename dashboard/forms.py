from django import forms
from app.models import Bookings, Room, Hotel


class BookingForm(forms.ModelForm):
    check_in = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    check_out = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Bookings
        exclude = ['hotel', 'user', 'amount', 'date']

class HotelForm(forms.ModelForm):
     class Meta:
         model = Hotel
         exclude = ['admin']

class RoomForm(forms.ModelForm):
     class Meta:
         model = Room
         exclude = ['hotel']


