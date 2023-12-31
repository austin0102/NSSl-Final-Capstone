"""
URL configuration for parkfit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import include
from rest_framework import routers
from parkfitapi.views import login_user, register_user, CommentView, TrainerView, athleteClassesView, DifficultyView, UserView, ClassesView, TokenView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'classes', ClassesView, 'class')
router.register(r'tokens', TokenView, 'token')
router.register(r'difficulties', DifficultyView, 'difficulty')
router.register(r'athleteclasses', athleteClassesView, 'athleteclass')
router.register(r'trainers', TrainerView, 'trainer')
router.register(r'comments', CommentView, 'comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('register', register_user),
    path('', include(router.urls)),  # Include the router's URLs
]
