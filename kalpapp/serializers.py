from rest_framework import serializers
from kalpapp.models import Number,Manager,Staff,Client

class NumberSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Number
        fields = "__all__"


class ManagerSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    number = NumberSerializer()
    class Meta: 
        model = Manager
        fields = "__all__"

    def create(self, validated_data):
        number_data = validated_data.pop('number')
        number_instance, _ = Number.objects.get_or_create(**number_data)
        manager_instance = Manager.objects.create(number=number_instance, **validated_data)
        return manager_instance
    
    def update(self, instance, validated_data):
        number_data = validated_data.pop('number', None)

        if number_data:
            number_instance, _ = Number.objects.get_or_create(**number_data)
            instance.number = number_instance

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        return instance


class StaffSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    number = NumberSerializer()
    class Meta:
        model = Staff
        fields = "__all__"

    
    def create(self, validated_data):
        number_data = validated_data.pop('number')
        number_instance, _ = Number.objects.get_or_create(**number_data)
        staff_instance = Staff.objects.create(number=number_instance, **validated_data)
        return staff_instance
    
    def update(self, instance, validated_data):
        number_data = validated_data.pop('number', None)

        if number_data:
            number_instance, _ = Number.objects.get_or_create(**number_data)
            instance.number = number_instance

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        return instance



class ClientSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    number = NumberSerializer()
    class Meta:
        model = Client
        fields = "__all__"

    def create(self, validated_data):
        number_data = validated_data.pop('number')
        number_instance, _ = Number.objects.get_or_create(**number_data)
        client_instance = Client.objects.create(number=number_instance, **validated_data)
        return client_instance
    
    def update(self, instance, validated_data):
        number_data = validated_data.pop('number', None)

        if number_data:
            number_instance, _ = Number.objects.get_or_create(**number_data)
            instance.number = number_instance

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        return instance
