from rest_framework import serializers 
from .models import Student 

class TestSerializers(serializers.Serializer): 
    name = serializers.CharField(error_messages = {"blank":"Name Can not be Blank."}) 
    address = serializers.CharField()
    age = serializers.IntegerField() 
    mobile_number = serializers.CharField() 
    
    def create(self, validated_data):
        print('validate date',validated_data)
        return Student.objects.create(**validated_data)  
    
    def update(self, instance, validated_data):
        validated_data = {"name":"Kusum","address": "Itahari", 'age':24}
        instance.name = validated_data.get('name', instance.names)
        
    def validate_age(self,age):
        if age>100 or age<0:
            raise serializers.ValidationError("Age must be valid in range 1 to 100")  
        return age 
    def validate_mobile_number(self, value):      #value=mobile_number 
        if Student.objects.filter(mobile_number = value).exists():
            raise serializers.ValidationError("Mobile Numner is already Exist !")
        return value 
    