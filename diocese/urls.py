from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dioceselist/<int:pk>/', views.DioceseDetailView.as_view(), name='dioceselist'),
    path('priestlist/', views.PriestList.as_view(), name='priestlist'),
]