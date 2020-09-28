from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View

from .models import Member
from .serializers import MemberSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

class MemberList(APIView):

    def get(self, request, format=None):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return HttpResponse(json.dumps(serializer.data))

    def post(self, request, format=None):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps(serializer.data), status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MemberDetail(APIView):

    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        memberobject = self.get_object(pk)
        serializers = MemberSerializer(memberobject)
        return HttpResponse(json.dumps(serializers.data))
    
    def put(self, request, pk, format=None):
        memberobject = self.get_object(pk)
        serializer = MemberSerializer(memberobject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps(serializer.data))
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        memberobject = self.get_object(pk)
        memberobject.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)