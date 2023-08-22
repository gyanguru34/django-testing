from rest_framework import serializers
from .models import Profile


class ProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model= Profile
        fields= "__all__"
    
    def create(self,validated_data):
        return Profile.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.number = validated_data.get('number', instance.number)
        instance.city = validated_data.get('city', instance.city)
        
        instance.save()
        return instance
  