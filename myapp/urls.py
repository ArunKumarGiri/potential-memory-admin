from django.urls import path, include
from .views import *
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    

)
urlpatterns = [
    
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path("RegisterApiView",RegisterApiView.as_view()),
    path("RegisterApiView1",RegisterApiView1.as_view()),
    # path('login' , LoignView.as_view()),
 
    path('profile/' , ProfileAPI.as_view()),
    path('profile/<int:pk>' , ProfileAPI.as_view()),
    
 	path("note/",AddNotesApiView.as_view()),
    
]