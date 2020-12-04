from rest_framework import serializers


class ReadSerializer(serializers.Serializer):
    """Weather request serializer"""
    city = serializers.CharField()
    numberOfDays = serializers.IntegerField(min_value=1, max_value=5)

