from django.urls import path
from . import views
#urlpatterns는 없으면 에러 발생
urlpatterns = [
    path('',views.readDocument, name='readDocument'),
    path('createDocument',views.createDocument, name='createDocument'),
    path('<int:pk>/updateDocument',views.updateDocument, name='updateDocument'),
    path('<int:pk>/deleteDocument',views.deleteDocument, name='deleteDocument')
]