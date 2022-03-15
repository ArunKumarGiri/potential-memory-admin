from .models import *
from rest_framework import serializers
from .views import *
from rest_framework.serializers import *
from django.contrib.auth.models import User


class RegisterSerializer(Serializer):
    first_name = CharField(error_messages={"required": "first name Key is required", "blank": "first name is required"},max_length=400)
    last_name=CharField(error_messages={"required": "last name Key is required", "blank": "last name is required"},max_length=400)
    email = CharField(error_messages={"required": "Email Key is required", "blank": "Email is required"},max_length=100)
    username = CharField(error_messages={"required": "username key is required", "blank": "username is required"},max_length=100)
    password = CharField(error_messages={"required": "password key is required", "blank": "password is required"},max_length=100)
    def validate(self,data):
        username=data.get('username')
        email=data.get('email')
        if User.objects.filter(username=username).exists():
            raise ValidationError("username is already exists.")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already exists. ")	
        return data
    def create(self, validated_data):
        first_name=validated_data.get('first_name')
        last_name=validated_data.get('last_name')
        email=validated_data.get('email')
        username=validated_data.get('username')
        password=validated_data.get('password')
        user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
        user.set_password(password)
        user.save()
        refresh = RefreshToken.for_user(user)
      
        return validated_data

class RegisterSerializer1(Serializer):
    first_name = CharField(error_messages={"required": "first name Key is required", "blank": "first name is required"},max_length=400)
    last_name=CharField(error_messages={"required": "last name Key is required", "blank": "last name is required"},max_length=400)
    email = CharField(error_messages={"required": "Email Key is required", "blank": "Email is required"},max_length=100)
    username = CharField(error_messages={"required": "username key is required", "blank": "username is required"},max_length=100)
    password = CharField(error_messages={"required": "password key is required", "blank": "password is required"},max_length=100)
    def validate(self,data):
        username=data.get('username')
        email=data.get('email')
        if User.objects.filter(username=username).exists():
            raise ValidationError("username is already exists.")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already exists. ")	
        return data
    def create(self, validated_data):
        user=User.objects.create_user(email=validated_data.get('email'),is_staff=True,username=validated_data.get('username'))

        first_name=validated_data.get('first_name')
        last_name=validated_data.get('last_name')
        email=validated_data.get('email')
        username=validated_data.get('username')
        password=validated_data.get('password')
        user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
        user.set_password(password)
        user.save()        
        return validated_data
    
    
# class LoginSer(Serializer):
#     username=CharField(error_messages={'required':'username key is required','blank':'username is required'})
#     password=CharField(error_messages={'required':'Password key is required','blank':'Password is required'})
#     token=CharField(read_only=True, required=False)

#     def validate(self,data):
#         qs=User.objects.filter(username=data.get('username'))
#         if not qs.exists():
#             raise ValidationError('No account with this username')
#         user=qs.first()
#         if user.check_password(data.get('password'))==False:
#             raise ValidationError('Invalid Password')        
#         return data


class AddNotesSerializer(Serializer):
    name = CharField(error_messages={"required": "Notes name Key is required", "blank": "Notes name can not empty"},max_length=400)
    description = CharField(error_messages={"required": "Notes name Key is required", "blank": "Notes name is required"},max_length=10000)
    def create(self,validated_data):
        name=validated_data.get('name')
        description=validated_data.get("description")
        user=self.context.get('request').user
        notes=Notes.objects.create(user=user)
        notes.name=name
        notes.description=description
        notes.save()
        return validated_data
    def update(self,instance,validated_data):
        name=validated_data.get('name')
        description=validated_data.get("description")
        instance.name=name
        instance.description=description
        instance.save()
        return validated_data
			


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        
