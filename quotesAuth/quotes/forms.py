from socket import fromshare
from django.forms import ModelForm

from .models import *



class QuoteForm(ModelForm):

    class Meta:

        model=Quote
        fields=['quote']
        exclude=['user']


