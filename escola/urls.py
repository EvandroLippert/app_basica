"""escola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from cursos_v2.urls import router


"""
Importante na criação da rota para a API especificar o versionamento dela,

é uma boa prática especificar qual versão está sendo desenvolvida, pois, após uma atualização,
pode haver clientes que permaneçam por mais tempo utilizando a versão antiga até se adaptarem a nova.

"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include('cursos.urls')),
    path('api/v2/', include(router.urls)),
]
