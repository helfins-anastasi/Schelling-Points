from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import scenario.views

urlpatterns = [
    url(r'^$', scenario.views.scenario, name='Schelling Points'),
    url(r'^admin/', include(admin.site.urls)),
]
