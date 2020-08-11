from django.urls import path, include

from knox.views import LogoutView

from .views import UserAPIView, RegisterAPIView, LoginAPIView

from rest_framework import routers
from . import views 

router = routers.DefaultRouter()
router.register(r'quiz', views.QuizViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'option', views.OptionViewSet)

urlpatterns = [
    path('', include('knox.urls')),
    path('', include(router.urls)),
    path('user', UserAPIView.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout')
]