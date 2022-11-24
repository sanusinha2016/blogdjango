from django.urls import path
from .views import BlogListView , BlogDetailsView

urlpatterns = [
    path('post/<int:pk>/' , BlogDetailsView.as_view() , name = 'post_detail'), # new
    path('' , BlogListView.as_view(),name="home") , 
]
# http://127.0.0.1:8000/post/1/