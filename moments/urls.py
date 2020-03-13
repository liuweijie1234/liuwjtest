# -*- coding: utf-8 -*-
from django.conf.urls import url
from moments.views import show_user, show_status, show_post, register, update_user, like
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin

urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^$', LoginView.as_view(template_name="homepage.html")),
    url(r'^user/$', show_user),
    url(r'^status/$', show_status),
    url(r'^post/$', show_post),
    url(r'^exit/$', LogoutView.as_view(next_page="/")),

    url(r'^register$', register),
    url(r'^user/update$', update_user),
    url(r'^like$', like)

    # url(r'^$', views.home),
    # url(r'^dev-guide/$', views.dev_guide),
    # url(r'^contact/$', views.contact),
)
