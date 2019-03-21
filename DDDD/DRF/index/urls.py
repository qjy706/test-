from django.conf.urls import url
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter




urlpatterns = [
    url(r'^index/$',view),
    url(r'^aaa/$',aaa)

]

router = DefaultRouter()
router.register(r'teachers',TeachersInfoViewSet)


urlpatterns += router.urls