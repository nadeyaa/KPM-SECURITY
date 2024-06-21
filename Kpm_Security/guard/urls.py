from django.urls import path
from .views import register, admin_view, guard_view

urlpatterns = [
    path('register/', register, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('guard/', guard_view, name='guard_view'),
]
