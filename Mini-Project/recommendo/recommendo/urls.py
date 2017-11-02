"""recommendo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movieDesc/$', views.movieDesc, name='movieDesc'),
    url(r'^ff/$', views.ff, name='ff'),
    url(r'^mdS/$', views.mdS, name='mdS'),
    url(r'^mdB$', views.mdB, name='mdB'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^gtky/$', views.gtky, name='gtky'),
    url(r'^todo_list/$', views.todo_list, name='todo_list'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^prof/$', views.prof, name='prof'),
    url(r'^index/$', views.index, name='index'),
    #url(r'^signup/$', views.signup, name='signup'),
    #url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^add-user/$',views.add_user, name='add_user'),
    url(r'^login/$',views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^add-user/$', views.add_user, name='add-user'),
    url(r'^dashboard/$',views.dashboard, name='dashboard'),
    url(r'^send-choices/$',views.send_choices,name='send-choices')

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)