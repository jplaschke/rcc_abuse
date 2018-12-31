from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dioceselist/<int:pk>/', views.DioceseDetailView.as_view(), name='dioceselist'),
    path('priestlist/', views.priest, name='priestlist'),
    path('priestlist/<int:pk>/', views.DioPriestListView.as_view(), name='diocesepriestlist'),
    path('archpriestlist/<int:pk>/', views.ArchPriestListView.as_view(), name='archdiocesepriestlist'),
   path('alldiocesepriestlist/<int:pk>/', views.ArchDioPriestListView.as_view(), name='dioceselist'),
 
]