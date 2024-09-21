from django import forms
from .models import VideoGame, Rental, Platform


class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['name']

class VideoGameForm(forms.ModelForm):
    class Meta:
        model = VideoGame
        fields = ['title', 'platform', 'genre', 'stock']

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['renter_name', 'video_game', 'rental_date', 'return_date']