from django import forms
from .models import Game, Developer, Platform

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = '__all__'

class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = '__all__'
