from django.contrib import admin
from django.urls import path, include
from manager import views as admin

urlpatterns = [
    # 通用路由
    # 文件上传
    path('fileupload/', admin.fileupload),

    # 后台登录
    path('admin/login/', admin.login),
    path('admin/logOut/', admin.logOut),
    path('verify/', admin.get_verify),

    # 后台管理

    # 后台首页
    path('admin/index/', admin.index),

    # 管理员管理
    path('admin/manager/', admin.manager),
    # 添加管理员
    path('admin/manager_add/', admin.manager_add),
    # 改变管理员状态
    path('admin/manager_change_state/', admin.manager_change_state),
    # 删除管理员
    path('admin/manager_del/', admin.manager_del),
    # 管理员编辑
    path('admin/manager_edit/', admin.manager_edit),

    # 栏目管理
    path('admin/category/', admin.category),
    # 栏目添加
    path('admin/category_add/', admin.category_add),
    # 栏目删除
    path('admin/category_del/', admin.category_del),
    # 栏目修改
    path('admin/category_edit/', admin.category_edit),

    # 文章管理
    path('admin/article/', admin.article),
    # 文章添加
    path('admin/article_add/', admin.article_add),
    # 文章删除
    path('admin/article_del/', admin.article_del),
    # 文章修改
    path('admin/article_edit/', admin.article_edit),


    # 友情链接管理
    path('admin/links/', admin.links),
]
