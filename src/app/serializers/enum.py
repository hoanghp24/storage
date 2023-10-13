from rest_framework import serializers

# Create your serializers here.

#Enum Choice
#----------------------------------------------------------------
class EnumChoiceSerializer(serializers.Serializer):
    value = serializers.CharField()
    display_name = serializers.CharField()
