from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import UploadFileModel
# Create your views here.
def home(request):
    file1=UploadFileModel.objects
    return render(request,'home.html',{'file1':file1})