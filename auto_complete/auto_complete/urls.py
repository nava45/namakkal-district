from django.conf.urls import include, url
from django.contrib import admin

from district import views as district_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'auto_complete.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/places/', district_views.get_items, name='get_items'),
    url(r'^(?P<location>[\w-]+)/(?P<category>[\w-]+)/(?P<item>[\w-]+)/$', district_views.view_item_detail, name="detail"),
    url(r'^$', district_views.home, name="home_page"),
]

