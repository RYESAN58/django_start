from django.urls import path
from . import views


urlpatterns = [
    path('six/<int:my_val>', views.index),
    path('routed/', views.fromthesix),
    path('redirected_route', views.redirected_method),
]
