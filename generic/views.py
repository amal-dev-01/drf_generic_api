from django.shortcuts import render
from generic.serializers import StudentSerializer
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from generic.models import Student

class StudentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)


class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

class StudentDestory(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
    