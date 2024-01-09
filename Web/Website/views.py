from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.contrib import messages
import bleach
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

# Crimport requestseate your views here.

def Index(request):
        datas =requests.get(url="http://127.0.0.1:8000/trending/").json()
        
        return render(request,"Index.html" ,{"data":datas})

def Bloglist(request):
    data = requests.get(url="http://127.0.0.1:8000/create/").json()
    return render(request ,"Bloglist.html",{"data":data})

def Blogs(request,name):
    if request.method == "GET":
        paramss= {"name":name}
        datas = requests.get(url=f"http://127.0.0.1:8000/full/",params=paramss).json()
        return render(request , "Blog.html" , {"data":datas})
    

def Createblob(request):
    data = requests.get(url="http://127.0.0.1:8000/Category/").json()
    return render(request ,'Create.html',{'data':data})
    
def categorycreate(request):
     if request.method == "POST":
        Category =request.POST.get('Category')
        urls = "http://127.0.0.1:8000/create/"
        result = requests.post(url=urls,data={'Category_Name':Category}).json()
        return JsonResponse(result ,safe=False)
def create(request):
        if request.method == "POST":
            Comp_Type = request.POST.get('title')
            image =request.FILES.get('Image')
            editer =request.POST.get('textarea')
            Category =request.POST.get('Category')
            Status = request.POST.get('Status')
            Trending=request.POST.get("Trending")
            Key_Word=request.POST.get("Key")
            Description=request.POST.get("Description")

            data = {
                "Title":Comp_Type,
                "Content":editer ,
                "Status":Status,
                "Category ":Category,
                "Trending":Trending,
                "Key_Word":Key_Word,
                "description":Description
                }
            
            img = {'Image':image}
            urls = "http://127.0.0.1:8000/create/"
            result = requests.post(url=urls,data=data ,files=img).json()
            print(result)
            return JsonResponse(result,safe=False)
        
def EditBlog(request,id):
    
    if request.method == "GET": 
        params={"id":id}
        data = requests.get(url="http://127.0.0.1:8000/Edit/",params=params).json()
        return render(request , 'Editblog.html',{"data":data})


       
        
    

def Listofblog(request):
    data = requests.get(url="http://127.0.0.1:8000/Listofblog/").json()
    return render(request ,"Listofblog.html",{"data":data})

def Editput(request ,id):
    
    
    params={"id":id}
    Title = request.POST.get('title')
    image =request.FILES.get('Image')
    editer =request.POST.get('textarea')
    Category =request.POST.get('Category')
    Status = request.POST.get('Status')
    Trending=request.POST.get('Trending')
    Key_Word=request.POST.get("Key")
    Description=request.POST.get("Description")
    data = {
            "Title":Title,
            "Content":editer,
            "Status":Status,
            "Category ":Category,
            "Trending":Trending,
            "Key_Word":Key_Word,
            "description":Description
            }
     
    img = {'Image':image}
    data = requests.put(url="http://127.0.0.1:8000/putEditView/",data=data,files=img,params=params).json()
    print(data)
    return redirect("Listofblogs")
        # return HttpResponse("Hello, World!")

def deletebyid(request ,id):
    print(5555555)
    try: 
        params={"id":id}
        one=requests.delete(url="http://127.0.0.1:8000/Delete/",params=params).json()
        meaagae = "deleteed"
        print(one)
        message ="hello"
        return JsonResponse({"message": message})
    except requests.exceptions.RequestException as e:
        # Handle network or request-related errors
        return JsonResponse({"message": "Error: " + str(e)})
    
def catrgory(request ,name):
    print("hello")
    paramss ={"Cname":name}
    data = requests.get(url="http://127.0.0.1:8000/RelatedCategory/",params=paramss).json()
    return JsonResponse(data,safe=False)


         
      
