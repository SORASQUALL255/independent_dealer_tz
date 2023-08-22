from rest_framework import serializers
from .models import DealerCenter, Vehicle
from django.contrib.auth.models import User


class DealerCenterSerializer(serializers.ModelSerializer):
    dealer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = DealerCenter
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    dealer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Vehicle
        fields = '__all__'
