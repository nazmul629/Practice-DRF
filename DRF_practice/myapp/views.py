from django.shortcuts import render, HttpResponse
from .models import Teacher
from .serializers import TeacherSerilizer

# from rest_framework.renderers import JSONRenderer
# from django.views.decorators.csrf import csrf_exempt
# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view 
# from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def teacehr_info(request, pk=None):
    if request.method =="GET":
        id = pk
        if id is not None:
            teacher = Teacher.objects.get(id=id)

            serializer = TeacherSerilizer(teacher)
            return Response(serializer.data)
        else:
            teacher = Teacher.objects.all()
            serializer = TeacherSerilizer(teacher, many=True)
            return Response(serializer.data)

















# def teacehr_info(request):

#     all = Teacher.objects.all()
    
#     serilaze = TeacherSerilizer(all, many=True)

#     json_data = JSONRenderer().render(serilaze.data)

#     return HttpResponse(json_data, content_type = 'application/json')

# def singl_techer(request,pk):

#     teacher = Teacher.objects.get(id = pk)

#     serilaze = TeacherSerilizer(teacher)

#     json_data = JSONRenderer().render(serilaze.data)

#     return HttpResponse(json_data, content_type = 'application/json')



# @csrf_exempt
# def teacher_create(request):
#     if request.method =="POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data =  JSONParser().parse(stream)
#         serizlizer =TeacherSerilizer(data = python_data)

#         if serizlizer.is_valid():
#             serizlizer.save()
#             res = {'msg':'Successfully save'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = 'application.json')
        
#         json_data =JSONRenderer().render(serizlizer.errors)
#         return HttpResponse(json_data,content_type = 'application.json')

#     if request.method == "PUT":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
        
#         # Use JSONParser instead of JSONRenderer
#         python_data = JSONParser().parse(stream)

#         id = python_data.get('id')
#         teacher = Teacher.objects.get(id=id)
#         serizlizer = TeacherSerilizer(teacher, data=python_data, partial =True)
        
#         if serizlizer.is_valid():
#             serizlizer.save()
#             res = {'msg':'Successfully Update'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = 'application.json')
        
#         json_data =JSONRenderer().render(serizlizer.errors)
#         return HttpResponse(json_data,content_type = 'application.json')
        


#     if request.method =="DELETE":
#         json_data = request.body
#         stream = io.BytesIO(json_data)

#         python_data = JSONParser().parse(stream)
#         id = python_data.get("id")
#         teacher = Teacher.objects.get(id =id )
#         teacher.delete()
#         res = {'meg':'successfull delete'}
#         json_data = JSONRenderer().render(res)
        
#         return HttpResponse(json_data,content_type = 'application.json')
    

          
