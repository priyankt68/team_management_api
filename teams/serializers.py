from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    # TODO - Convert this integer field to limited 10 digit char field
    phone_number = serializers.IntegerField()
    role = serializers.CharField()
    # TODO- add a unique id to return for each member.

    def create(self, validated_data):
        return Member.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # TODO  - Implement update
        pass