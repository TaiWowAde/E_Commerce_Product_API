"""
URL configuration for config project.

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import RedirectView
from products.views import ProductViewSet
from categories.views import CategoryViewSet
from users.views import RegisterView, ProfileView
from rest_framework.authtoken.views import obtain_auth_token
from dashboard import views as dash_views
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register("products", ProductViewSet, basename="product")
router.register("categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", RedirectView.as_view(url="/api/", permanent=False)), 
    path("admin/", admin.site.urls),
    path("api/auth/register/", RegisterView.as_view(), name="register"),
    path("api/auth/login/", obtain_auth_token, name="login"),
    path("api/users/profile/", ProfileView.as_view(), name="profile"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")), 
    path("dashboard/", dash_views.dashboard_home, name="dashboard_home"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="dashboard/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
]





