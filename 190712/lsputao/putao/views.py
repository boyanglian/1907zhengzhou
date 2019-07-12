from django.shortcuts import render

# Create your views here.
# 后台视图

def admin_login(request):
    return render(request, 'admin/admin_login.html')