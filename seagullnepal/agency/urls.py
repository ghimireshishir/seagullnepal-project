from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('package/<int:package_id>/', views.package_detail, name='package_detail'),
    path('package/<int:package_id>/book/', views.book_package, name='book_package'),
]
