from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.

class listofblog(APIView):
    def get(self ,request):
        info = BlogCreate.objects.select_related('Category')
        seri = ListBlogSerializers(info , many=True ,context={'request':request})
        return Response(seri.data ,status=status.HTTP_200_OK)

class First(APIView):
    
    def get(self , request):
        info = BlogCreate.objects.select_related('Category').filter(Status=True)
        seri = getBlogSerializers(info , many=True ,context={'request':request})
        return Response(seri.data ,status=status.HTTP_200_OK)

    def post(self,request):
        print("coming")
        if 'Category_Name' in request.data:
            print(222222222222222222222222222222)
            datas =CategorySerializers(data=request.data)
            if datas.is_valid():
                datas.save()
                return Response(datas.data ,status=status.HTTP_201_CREATED)
        
        elif 'Title'in request.data:
            print(111111111111111111111111111)
            datas = BlogSerializers(data=request.data)
            if datas.is_valid():
                datas.save()
                return Response(datas.data , status=status.HTTP_201_CREATED)
        else:
            print("noooooooooooooooooooooooo")

class CategoryList(APIView):
    def get(self , request):
        info = Category.objects.all()
        seri = CategorySerializers(info , many=True)
        return Response(seri.data ,status=status.HTTP_200_OK)
     
    def post(self , request):
        save = CategorySerializers(data=request.data)
        if save.is_valid():
            save.save()
            return Response(save.data ,status=status.HTTP_201_CREATED)

class Detailview(APIView):

    def get(self,request):
        print("in")
        name=request.query_params.get("name")
        # datas =get_object_or_404(BlogCreate,slug=name)
        datas = BlogCreate.objects.filter(Slug=name).select_related("Category")
        serializer = detailserialaizer(datas,many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)

class Editview(APIView):

    def get(self ,request):
        id=request.query_params.get("id")
        model = BlogCreate.objects.filter(pk=id)
        serializer = EditSerialaizer(instance=model , many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    
class putEditView(APIView):
    def put(self ,request):
        print("GET")
        try:
            id=request.query_params.get("id")
            print(id)
            model = BlogCreate.objects.get(pk=id)
            print(request.data)
            serializer = EditSerialaizer(instance=model,data=request.data)
            if serializer.is_valid():
                serializer.save() 
                return Response(serializer.data ,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
                           
        except:
            print("error")

class Trending(APIView):
    def get(self ,request):
        data = BlogCreate.objects.filter(Trending=True,Status=True)
        serializerr =getBlogSerializers(instance=data,many=True,context={'request':request})
        return Response(serializerr.data ,status=status.HTTP_200_OK)
    
class Delete(APIView):
    print(55)
    def delete(self ,request):
        print(55)
        id=request.query_params.get("id")
        model = BlogCreate.objects.get(pk=id)
        model.delete()
        return HttpResponse({"data":"Delete success"})

class CategoryName(APIView):
     def get(self ,request):
        Cname=request.query_params.get("Cname")
        data = BlogCreate.objects.select_related("Category").filter(Category=Cname,Status=True)
        serializerss =CategorynameSerializer(data,many=True,context={'request':request})
        return Response(serializerss.data ,status=status.HTTP_200_OK)



