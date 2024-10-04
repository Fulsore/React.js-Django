from rest_framework import serializers
from .models import FormData

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormData
        fields = ['id','name','password']
        
        