from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Member
from .serializers import MemberSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

def index(request):
    return HttpResponse("index url")

class MemberList(APIView):

    def get(self, request, format=None):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return HttpResponse(serializer.data)

    def post(self, request, format=None):
        serializer = MemberSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.error, status=status.HTTP_400_BAD_REQUEST)

# class MemberList(ListView):
#     model = Member

# class MemberDetail(DetailView):
#     model = Member

# class MemberUpdate(UpdateView):
#     model = Member

# class MemberDelete(DeleteView):
#     model = Member
