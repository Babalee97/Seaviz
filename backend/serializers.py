from rest_framework import serializers
from .models import Visual

class VisualsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visual
        fields = '__all__'