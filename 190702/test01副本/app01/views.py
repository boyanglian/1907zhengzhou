from django.shortcuts import render, HttpResponse

# Create your views here.
def abc(request, **kwargs):
def abc(request, **kwargs):
    print('abc')
    print('abc')
    # 主动抛出异常错误
    raise ValueError('值不对！')
    raise ValueError('值不对！')
    return HttpResponse('ab')
    return HttpResponse('ab')