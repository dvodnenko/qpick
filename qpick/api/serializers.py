from rest_framework import serializers
from store.models import Headphone, Cover


class HeadphoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Headphone
        fields = '__all__'


class CoverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cover
        fields = '__all__'
