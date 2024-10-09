from rest_framework import serializers
from .models import Teacher

# useing_model serializers
class TeacherSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields =['id','name','age'] 


# class TeacherSerilizer(serializers.Serializer):
#     name = serializers.CharField(max_length=40)
#     age = serializers.IntegerField()


#     def create(self,validated_data):
#         return Teacher.objects.create(**validated_data)
    


#     def update(self,instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.age = validated_data.get('age',instance.age)

#         instance.save()
#         return instance 
