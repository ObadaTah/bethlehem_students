import platform
from django.http.response import HttpResponse
import mimetypes
import os
from project.settings import MEDIA_ROOT
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .uploader import handle_uploaded_file
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Create your views here.
from .models import *

ips_files = {}


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@csrf_protect
def uploader(request):
    if request.method == 'POST':
        
        try:
            directory, fileName, fileType = handle_uploaded_file(
                request.FILES['file'])
            file = Files(fileName=fileName, file_type=fileType,
                         directory=directory)
            file.save()
            ip = request.POST.get('csrfmiddlewaretoken')
            if ip in ips_files:
                ips_files[request.POST.get('csrfmiddlewaretoken')].append(file.id)
            else:
                ips_files[request.POST.get('csrfmiddlewaretoken')] = [file.id]
        except Exception as x:
            print(x)
            return HttpResponseRedirect('')  # error page
        return render(request, 'upload.html')

    return render(request, 'upload.html', {})


@csrf_protect
def add(request):
    if request.method == 'POST':
        upload = Upload(upload_name=request.POST['upload_name'], upload_description=request.POST['upload_description'],
                        upload_course_code=int(request.POST['upload_course_code']), upload_type=int(request.POST['upload_type']))
        upload.save()
        try:
            for i in ips_files[request.POST.get('csrfmiddlewaretoken')]:
                uploadsFiles = UploadsFiles(
                    uploadClass=upload, fileClass=Files.objects.get(id=i))
                uploadsFiles.save()
            del ips_files[request.POST.get('csrfmiddlewaretoken')]
        except Exception as x:
            print(x)

    return render(request, 'Home.html', {})


def view(request):
    return render(request, 'Home.html', {})


def course_view(request):
    uploads = Upload.objects.filter(
        upload_course_code=int(request.GET['course_index']))
    upload_list = []
    
    course_name = Upload.CHOICESC[int(request.GET['course_index'])][1]
    for upload in uploads:
        upload_list.append({'id': upload.id, 'upload_name': upload.upload_name, 'upload_description': upload.upload_description,
                            'upload_type': Upload.CHOICES[int(upload.upload_type)][1]})

    return render(request, 'course.html', {'uploads': upload_list, 'name': course_name})


def upload_view(request, upload_id):
    upload = Upload.objects.get(id=upload_id)
    files = UploadsFiles.objects.filter(uploadClass=upload)
    file_list = [] 
    new = ''
    upload = {'upload_name': upload.upload_name, 'upload_description': upload.upload_description, 'upload_course_code': Upload.CHOICESC[upload.upload_course_code][1],}
    if platform.system() == 'Windows':
        new = MEDIA_ROOT.replace('\\', '/')
    else:
        new = MEDIA_ROOT
    for file in files:
        directory = (new+'/'+file.fileClass.directory).replace('/', '(slash)')
        file_list.append({"file_name": file.fileClass.fileName,
                         "file_type": file.fileClass.file_type, "file_size": os.path.getsize(new+'/'+file.fileClass.directory), "directory": directory,})
    return render(request, 'upload_view.html', {'upload': upload, 'files': file_list})


def download_file(request, filepath):

    # Open the file for reading content
    filepath = filepath.replace('(slash)', '/')
    if os.path.exists(filepath):
        with open(filepath, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(filepath)
            return response
    else:
        raise Http404
