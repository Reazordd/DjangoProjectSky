"""
URL configuration for DjangoProjectSky project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from vacancies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('vacancy/', views.VacancyView.as_view()),  # Для списка и создания вакансий
    path('vacancy/<int:vacancy_id>/', views.VacancyDetailView.as_view(), name='vacancy-detail'),
]
