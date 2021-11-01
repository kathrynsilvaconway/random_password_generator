from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('generate_password', views.generate_password),
    path('regenerate_password/<int:length>', views.regenerate_password),
    path('render_password', views.render_password)
]
