from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('data/',views.createTeacher.as_view()),
    path('data/<int:pk>/',views.createTeacher.as_view()),
    
    # path('create/',views.teacher_create),
]
