from rest_framework import serializers

class DescSerializer(serializers.Serializer):
    graph_name = serializers.CharField(max_length=120)
    x_axis_name = serializers.CharField(max_length=120)
    y_axis_name = serializers.CharField(max_length=120)