"""
URL configuration for Web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Website import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index , name="Index"),
    path('Blogs/',views.Bloglist,name="Bloglist"),
    path('CreateBlog/',views.Createblob,name="CreateBlog"),
    path('Create/',views.create,name="create"),
    path('EditBlog/<int:id>',views.EditBlog ,name="Editblog"),
    path('Listofblog/',views.Listofblog,name="Listofblogs"),
    path('Blogs/<slug:name>',views.Blogs,name="Blog"),
    path('categorycreate/',views.categorycreate,name="categorycreate"),
    path('Update/<int:id>',views.Editput,name="Update"),
    path('delete/<int:id>',views.deletebyid , name="Delete"),
    path("relatedCategory/<int:name>",views.catrgory,name="RelatedCategory")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
