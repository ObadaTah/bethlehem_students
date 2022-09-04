from django.urls import path
from .views import uploader, add, view, course_view, upload_view, download_file

urlpatterns = [
    path('uploader', uploader, name="uploader") ,
    path('add', add, name="add") ,
    path('', view, name="home") ,
    path('course', course_view, name="course") ,
    path('upload_view/<int:upload_id>', upload_view, name="upload_view") ,
    path('download_file/<str:filepath>/', download_file, name="download_file") ,
    
]