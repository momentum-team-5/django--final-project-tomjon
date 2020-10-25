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
from questionbox import views as questionbox_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', questionbox_views.questions_list, name='questions_list'),
    path('questionbox/<int:pk>/', questionbox_views.questions_detail, name='questions_detail'),
    path('questionbox/add/', questionbox_views.add_question, name='add_poem'),
    path('questionbox/<int:pk>/delete/', questionbox_views.questions.delete, name='questions_delete'),
    path('questionbox/favorite/<int:pk>/<int:user_pk>/', questionbox_views.add_favorite, name='questions_add_favorite')
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
