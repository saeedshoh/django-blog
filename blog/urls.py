
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('category/<str:slug>/', PostCategoryView.as_view(), name='categories.show'),   
    path('posts/<str:slug>/', PostDetailView.as_view(), name='posts.show'),   
    path('tag/<str:slug>/', TagDetailView.as_view(), name='tags.show'),   
]