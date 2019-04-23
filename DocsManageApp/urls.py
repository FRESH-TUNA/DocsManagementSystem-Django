from django.urls import path
from . import views
#urlpatterns는 없으면 에러 발생
urlpatterns = [
    path('',views.readDocument, name='readDocument')
]