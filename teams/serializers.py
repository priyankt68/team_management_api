from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    # TODO - Convert this integer field to limited 10 digit char field
    phone_number = serializers.IntegerField()
    role = serializers.CharField()
    id = serializers.IntegerField()

    def create(self, validated_data):
        return Member.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # TODO  - Implement update
        """
        NOTE - We should only update those fields which are
        sent as in request
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance