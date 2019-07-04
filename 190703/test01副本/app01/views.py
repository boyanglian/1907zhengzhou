from django.shortcuts import render, HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.http import JsonResponse
import time
import time
import os
import  os
from django.conf import settings
from django.conf import settings
from django.conf import settings
# Create your views here.
def abc(request, **kwargs):
    print('abc')
    # 主动抛出异常错误
    raise ValueError('值不对！')
    return HttpResponse('ab')

def home(request):
def home(request):
    return render(request, 'home.html')
    return render(request, 'home.html')

def jisuan(request):
def jisuan(request):
    print(request.is_ajax())
    print(request.is_ajax())
    print(request.POST)
    print(request.POST)
    num1 = request.POST.get('num1')
    num1 = request.POST.get('num1')
    num2 = request.POST.get('num2')
    num2 = request.POST.get('num2')
    count = int(num1) + int(num2)
    count = int(num1) + int(num2)
    return HttpResponse(count)
    return HttpResponse(count)


def upload(request):
def upload(request):
def upload(request):
    """
    展示上传页面和处理上传文件
    展示上传页面和处理上传文件
    :param request:
    :return:
    """
    if request.is_ajax():
    if request.is_ajax():
    if request.is_ajax():
        # 获取图片参数
        file = request.FILES.get('up_image')
        file = request.FILES.get('up_image')
        # 获取图片参数
        file = request.FILES.get('up_image')
        # 从文件名中获取 扩展名
        ext = file.name.split('.')[-1]
        # 从文件名中获取 扩展名
        ext = file.name.split('.')[-1]
        ext = file.name.split('.')[-1]
        # 要不保存的新文件          os.path.sep 当前系统的目录分隔符
        #                        os.path.seq 当前系统的目录分隔符
        file_name = os.path.sep + time.strftime('%Y%m%d%H%M%S') + '.' + ext    # 201907031116.png
        file_name = os.path.seq + time.strftime('%Y%m%d%H%M%S') + '.' + ext
        # 真实要保存文件的物理路径
        # filePath = settings.BASE_DIR + 'uploads' + file_name  # 绝对物理路径
        filePath = settings.BASE_DIR + 'uploads' + file_name # 绝对物理路径
        filePath = 'uploads' + file_name  # 相对物理路径
        filePath = 'uploads' + file_name  # 相对物理路径
        with open(filePath, 'ab+') as f:
        with open(filePath, 'ab+') as f:
            # file.chunks 从上传文件中（一块一块的循环）读取内容
            # file.chunks 从上传文件中（一块一块的循环）读取内容
            for chunk in file.chunks():
            for chunk in file.chunks():
            for chunk in file.chunks():
                # 把上传文件的内容 分块写入到新文件中
                f.write(chunk)
                f.write(chunk)
                f.write(chunk)
        # 上传成功以后返回的json字符串                                 '/static' + file_name  url访问时url路径
        return JsonResponse({'msg': 'success', 'code': 0, 'data': ['/static' + file_name]})
        return JsonResponse({'msg': 'success', 'code': 0, 'data': ['/static' + file_name]})
    return render(request, 'upload.html')
    return render(request, 'upload.html')