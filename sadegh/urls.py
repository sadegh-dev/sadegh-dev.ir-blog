from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from fadevelop import views

urlpatterns = [
    path('secret :) /', admin.site.urls),
    path('', views.gohome, name='gohome'),
    path('fa-develop/', include('fadevelop.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] 
#+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 