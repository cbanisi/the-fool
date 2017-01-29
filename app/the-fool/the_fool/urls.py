"""
Definition of urls for the_fool.
"""

from django.conf.urls import include, url
from app import views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
#print("views", views.home)

urlpatterns = [
    # Examples:
    url(r'^$', views.current_datetime),
    url(r'^deck/', views.deck),
    url(r'^game/', views.game)
    # url(r'^the_fool/', include('the_fool.the_fool.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
