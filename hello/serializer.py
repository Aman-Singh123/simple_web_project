from rest_framework import serializers 
from .models import LogMessage
class LogMessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields=("message","log_date")
        model=LogMessage
      

