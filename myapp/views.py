from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.status import *
from rest_framework.response import Response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny



class RegisterApiView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registered Successfully"}, status=HTTP_200_OK)
        else:
            return Response({"error":serializer.errors}, status=HTTP_400_BAD_REQUEST)

class RegisterApiView1(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = RegisterSerializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registered Successfully"}, status=HTTP_200_OK)
        else:
            return Response({"error":serializer.errors}, status=HTTP_400_BAD_REQUEST)

# class LoignView(APIView):
#     permission_classes = [AllowAny, ]

#     def post(self, request):
#         serializer = LoginSer(data=request.data)
#         if serializer.is_valid():
#             return Response({'Success': 'login successfully', 'data': serializer.data}, status=HTTP_200_OK)
#         return Response({'Error': 'login unsuccesfull', 'data': serializer.data},status=HTTP_400_BAD_REQUEST)
        
#     def post(self , request):
#         username = request.data['username']
#         password = request.data['password']
#         user = User(username=username)
#         user.set_password(password)
#         refresh = RefreshToken.for_user(user)  
        
#         return Response(
#             {
#                 "status":"success" ,
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token)
#             })

    


class AddNotesApiView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        # print(request.headers)
        serializer = AddNotesSerializer(data=request.data,context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "added Successfully"}, status=HTTP_200_OK)
        else:
            return Response({"error":serializer.errors}, status=HTTP_400_BAD_REQUEST)


    def get(self, request):
        if request.user.is_staff==True:         
            notes=Notes.objects.all().order_by("-id")
            serializer=ViewNotesSerializer(notes,many=True)
            return Response({"data":serializer.data}, status=HTTP_200_OK)
        else:
            notes=Notes.objects.filter(user=request.user).order_by("-id")
            serializer=ViewNotesSerializer(notes,many=True)
            return Response({"data":serializer.data}, status=HTTP_200_OK)



    def delete(self,request,*args,**kwargs):
        if request.user.is_staff==True:
            note_id=request.GET.get("id")
            if Notes.objects.get(pk=note_id).exists():
                n=Notes.objects.get(pk=note_id)
                n.delete()
                return Response({"message": "delete Successfully"}, status=HTTP_200_OK)
            else:
                return Response({"error":"Note is not exist"}, status=HTTP_400_BAD_REQUEST)
            
        else:
            note_id=request.GET.get("id")
            if Notes.objects.filter(user=request.user,pk=note_id).exists():
                n=Notes.objects.get(user=request.user,pk=note_id)
                n.delete()
                return Response({"message": "delete Successfully"}, status=HTTP_200_OK)
            else:
                return Response({"error":"Note is not exist"}, status=HTTP_400_BAD_REQUEST)
            
            


    def update(self,request,*args,**kwargs):
        if request.user.is_staff==True:
            note_id=request.GET.get("id")
            if Notes.objects.filter(pk=note_id).exists():
                notes=Notes.objects.get(pk=note_id)
                serializer=AddNotesSerializer(notes,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "update Successfully"}, status=HTTP_200_OK)
                else:
                    return Response({"error":serializer.errors}, status=HTTP_400_BAD_REQUEST)	
            else:
                return Response({"error":"Note is not exist"}, status=HTTP_400_BAD_REQUEST)
            
        else:
             note_id=request.GET.get("id")
        if Notes.objects.filter(user=request.user,pk=note_id).exists():
            notes=Notes.objects.get(user=request.user,pk=note_id)
            serializer=AddNotesSerializer(notes,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "update Successfully"}, status=HTTP_200_OK)
            else:
                return Response({"error":serializer.errors}, status=HTTP_400_BAD_REQUEST)	
        else:
            return Response({"error":"Note"})


   
class ProfileAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None, format=None):
        if request.user.is_staff==True:
            stu = Profile.objects.get(pk=id)
            serializer = ProfileSerializer(stu)
            return Response(serializer.data)
        else:           
            stu = Profile.objects.filter(user=request.user)
            serializer = ProfileSerializer(stu, many=True)
            return Response(serializer.data)
    
    def post(self, request, format=None):
        user=request.user
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk, format=None):
        if request.user.is_staff==True:                
            stu = Profile.objects.get(pk=id, user=request.user)
            serializer = ProfileSerializer(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Complete Data Updated'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            stu = Profile.objects.get(pk=id, user=request.user)
            serializer = ProfileSerializer(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Complete Data Updated'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

    def delete(self, request, pk, format=None):
        if request.user.is_staff==True:       
            stu = Profile.objects.get(pk=id, user=request.user)
            stu.delete()
            return Response({'msg':'Data Deleted'})
        
        else:    
            stu = Profile.objects.get(pk=id, user=request.user)
            stu.delete()
            return Response({'msg':'Data Deleted'})
        
        
        
