from django.conf.locale import fa
from rest_framework import serializers
from config.api.models import Category, Exercise

class ExerciseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField(max_length=255, source="category.name", required=False, read_only=True) 
    name = serializers.CharField(max_length=255, required=False)
    category_id = serializers.PrimaryKeyRelatedField(source= "category", queryset= Category.objects.all(), write_only= True, required= False)

    def create (self, validated_data):
        return Exercise.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.category= validated_data.get("category", instance.category)
        instance.name= validated_data.get("name", instance.name)
        instance.save()
        return instance