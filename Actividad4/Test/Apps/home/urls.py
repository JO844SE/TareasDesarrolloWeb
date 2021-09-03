from django.contrib import admin
from django.urls import path
from django.urls import path,include
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
  path('index/', HomeView.as_view(), name='home'),
]