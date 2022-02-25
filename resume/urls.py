from django.urls import path,include
from rest_framework import routers
from resume import views

router = routers.DefaultRouter()
router.register('resume', views.ResumeModelViewSet,basename="resume")

urlpatterns = [
    path('', include(router.urls)),
    path('get-chain/',views.GetUserChain.as_view())
]