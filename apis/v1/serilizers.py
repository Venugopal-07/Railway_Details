from rest_framework.serializers import ModelSerializer
from Details.models import Train_Details

class Trains(ModelSerializer):
    class Meta:
        model=Train_Details
        fields='__all__'
