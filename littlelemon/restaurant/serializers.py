from rest_framework import serializers
from .models import Booking,Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'title', 'price','inventory')