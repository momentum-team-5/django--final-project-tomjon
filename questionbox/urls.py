"""questionbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from questions import views as question_views
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', question_views.questions_list, name='questions_list'),
    path('questionbox/<int:pk>/', question_views.questions_detail, name='questions_detail'),
    path('questionbox/add/', question_views.questions_add, name='questions_add'),
    path('questionbox/<int:pk>/delete/', question_views.questions_delete, name='questions_delete'),
    path('questionbox/favorite/<int:pk>/<int:user_pk>/', question_views.add_favorite, name='add_favorite')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
