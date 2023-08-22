from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('dc/', views.DealerCenterList.as_view(), name='dc'),
    path('dc/<int:pk>/', views.DealerCenterDetail.as_view()),
    path('veh/', views.VehicleList.as_view(), name='veh'),
    path('veh/<int:pk>/', views.VehicleDetail.as_view()),
    path('', views.DealerCenterFront.as_view(), name='home'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]