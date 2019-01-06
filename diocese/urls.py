from django.urls import path

from . import views

urlpatterns = [
    path('priestlist/<int:pk>/', views.DioPriestListView.as_view(), name='diocesepriestlist'),
    path('archpriestlist/<int:pk>/', views.ArchPriestListView.as_view(), name='archdiocesepriestlist'),
    path('orderalphapriestlist/<str:letter>/', views.orderpriestlist_view, name="orderpriestlist_view"),
    path('alphapriestlist/<str:letter>/', views.priestlist_view, name="priestlist_view"),
    path('orderalphapriestlist/', views.alpha_orderpriestlist, name="alpha_orderpriestlist"),
    path('alphapriestlist/', views.alpha_priestlist, name="alpha_priestlist"),
    path('alldiocesepriestlist/<int:pk>/', views.ArchDioPriestListView.as_view(), name='dioceselist'),
    path('priestlist/', views.priest, name='priestlist'),
    path('dioceselist/<int:pk>/', views.DioceseDetailView.as_view(), name='dioceselist'),
    path('', views.index, name='index'),
 
]