from rest_framework import serializers
from rest_framework.fields import empty
from .models import *

class CustomDateTimeField(serializers.DateTimeField):
    def to_representation(self, value):
        # Convert the datetime to the desired format
        return value.strftime('%Y-%m-%d %H:%M:%S')

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = ['id','Category_Name']

class getBlogSerializers(serializers.ModelSerializer):
    Category =serializers.StringRelatedField( source = 'Category.Category_Name')

    class Meta:
        model = BlogCreate
        fields =['id','Title' ,'Content','Status','Create_Time','Image','Category','Trending','Slug']

class ListBlogSerializers(serializers.ModelSerializer):
    Category =serializers.StringRelatedField( source = 'Category.Category_Name')
    Create_Time = CustomDateTimeField()
    class Meta:
        model = BlogCreate
        fields =['id','Title' ,'Content','Status','Create_Time','Image','Category','Trending']




class BlogSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = BlogCreate
        fields =['Title' ,'Content','Status','Create_Time','Image','Category','Trending','Slug','description','Key_Word']

class detailserialaizer(serializers.ModelSerializer):
     Category_Name =serializers.StringRelatedField(source = "Category.Category_Name")
     Create_Time = CustomDateTimeField()
     class Meta:
          model = BlogCreate
          fields = ['id','Title' ,'Content','Create_Time','Category','Image','Slug','Category_Name','description','Key_Word']

class EditSerialaizer(serializers.ModelSerializer):

    class Meta:
        model = BlogCreate
        fields = ['id','Title' ,'Content','Status','Create_Time','Image','Category','Trending','description','Key_Word']


class onEditSerialaizer(serializers.ModelSerializer):

    class Meta:
        model = BlogCreate
        fields = ['id','Title','Content','Status','Create_Time','Image','Category','Trending','Slug','description','Key_Word']


class TrendingSerilizer(serializers.ModelSerializer):

    class Meta:
        model = BlogCreate
        fields = ['id','Title','Content','Status','Image','Category','Trending']

class CategorynameSerializer(serializers.ModelSerializer):
    Category_Name = serializers.StringRelatedField(source = 'Category.Category_Name')
    class Meta :
        model = BlogCreate 
        fields =["Category_Name",'id','Title','Content','Status','Image','Category','Trending' ,'Slug']