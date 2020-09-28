from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    phone = serializers.IntegerField(source='phone_number')
    # emailId = serializers.EmailField(source='email')
    role = serializers.CharField()
    userId = serializers.IntegerField(source='id', required=False)


    class Meta:
        model = Member
        # fields = ['userId', 'firstName', 'lastName', 'phone', 'role', 'emailId']
        fields = ['userId', 'firstName', 'lastName', 'phone', 'role']
        read_only_fields = ['userId']

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
        # instance.email = validated_data.get('emailId', instance.email)

        instance.save()
        return instance