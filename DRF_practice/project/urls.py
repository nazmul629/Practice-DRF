from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('data/',views.teacehr_info),
    path('data/<int:pk>/',views.singl_techer),
    path('create/',views.teacher_create),
]
