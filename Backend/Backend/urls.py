"""
URL configuration for Backend project.

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
from API import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',views.First.as_view()),
    path('Category/',views.CategoryList.as_view()),
    path('full/',views.Detailview.as_view()),
    path('Edit/',views.Editview.as_view()),
    path('trending/',views.Trending.as_view()),
    path('Delete/',views.Delete.as_view()),
    path('Listofblog/',views.listofblog.as_view()),
    path('RelatedCategory/',views.CategoryName.as_view()),
    path('putEditView/',views.putEditView.as_view()),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
