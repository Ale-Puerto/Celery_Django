from django.urls import path

from .views import GenerateRandomUserView, UserListView

urlpatterns = [
    path('', GenerateRandomUserView.as_view(), name='index'),
    path('listar/', UserListView.as_view(), name='user_list')
    
]