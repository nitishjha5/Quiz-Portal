from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'quiz', views.QuizViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'option', views.OptionViewSet)
router.register(r'batch', views.BatchViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'Attempt', views.AttemptViewSet)
router.register(r'Perfomance', views.PerfomanceViewSet)
router.register(r'User', views.UserViewSet)




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]