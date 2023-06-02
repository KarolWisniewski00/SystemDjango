from django.urls import path
from . import views
urlpatterns = [
    path('',views.getRoutes),
    path('times/',views.getTimes),
    path('times/create/',views.createTime),
    path('times/<str:id>/',views.getTime),
    path('times/update/<str:id>/',views.updateTime),
    path('times/delete/<str:id>/',views.deleteTime),
]