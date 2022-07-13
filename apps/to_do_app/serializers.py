from rest_framework import serializers

from to_do_app.models import Exercise

class TaskSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Exercise
        fields = (
            'user',
            'description',
        )