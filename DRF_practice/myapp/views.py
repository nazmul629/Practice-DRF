from email.mime import base
from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Teacher
from .serializers import TeacherSerilizer

# from rest_framework.renderers import JSONRenderer
# from django.views.decorators.csrf import csrf_exempt
# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view 
# from rest_framework.response import Response

# for function base View

# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class createTeacher(APIView):

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            teacher = Teacher.objects.get(id=id)
            serializer = TeacherSerilizer(teacher)
            return Response(serializer.data)       
        
        teacher = Teacher.objects.all()
        serializer = TeacherSerilizer(teacher, many=True) 
        return Response(serializer.data)
    
    def post(self, request,format=None):
        serializer = TeacherSerilizer(data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Successfully insert Data"})
        return  Response(serializer.errors)
    
    def put(self, request,pk=None, format=None):
        id = pk
        teacher = Teacher.objects.get(id =id)
        serializer = TeacherSerilizer(teacher,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data Updated"})
        return Response(serializer.errors)   
    
    def patch(self, request,pk=None, format=None):
        id = pk
        teacher = Teacher.objects.get(id =id)
        serializer = TeacherSerilizer(teacher, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data Partialy updated"})
        print(serializer.errors)
        return Response(serializer.errors)
    def delete(self, request,pk=None, format=None):
        id = pk
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        res = {'msg':' Successfullly Delete'}
        return Response(res)
    
    
    
    


        








# function base View

# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def teacehr_info(request, pk=None):
#     if request.method =="GET":
#         id = pk
#         if id is not None:
#             teacher = Teacher.objects.get(id=id)

#             serializer = TeacherSerilizer(teacher)
#             return Response(serializer.data)
#         else:
#             teacher = Teacher.objects.all()
#             serializer = TeacherSerilizer(teacher, many=True)
#             return Response(serializer.data)
        

#     if request.method =="POST":
#         serializer = TeacherSerilizer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res={ 'msg': 'successfully insert'}
#             return Response(res)
#         return Response(serializer.errors)
    
#     if request.method =="PUT":
#         id =pk
#         teacher = Teacher.objects.get(id=id)
#         serializer = TeacherSerilizer(teacher,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':"Full Data Updated"}
#             return Response(res) 
#         return Response(serializer.errors) 
        

#     if request.method =="PATCH":
#         id =pk
#         teacher = Teacher.objects.get(id=id)
#         serializer = TeacherSerilizer(teacher, data = request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':"Partial Data Updated"}
#             return Response(res)
#         return Response(serializer.errors)
    
#     if request.method =="DELETE":
#         id =pk
#         treacher = Teacher.objects.get(id=id)
#         treacher.delete()
#         res = {'msg':' Successfullly Delete'}
#         return Response(res)
#     return Response()




















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
    

          
