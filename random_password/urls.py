from django.urls import path, include

urlpatterns = [
    path('', include('password_app.urls')),
]
