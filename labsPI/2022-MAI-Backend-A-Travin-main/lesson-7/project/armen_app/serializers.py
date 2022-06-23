from armen_app.models import Colors, Boots
from rest_framework import serializers

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ["color_id", "name"]

class BootsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boots
        fields = ["boots_id", "name", "description", "color", "countries"]
