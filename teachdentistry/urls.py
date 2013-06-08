from django.conf.urls.defaults import patterns, include
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template
import os.path
admin.autodiscover()
import staticmedia

site_media_root = os.path.join(os.path.dirname(__file__), "../media")

urlpatterns = patterns(
    '',
    ('^accounts/', include('djangowind.urls')),
    (r'^logout/$',
     'django.contrib.auth.views.logout',
     {'next_page': '/'}),
    (r'^$', 'teachdentistry.main.views.index'),
    (r'^_pagetree/', include('pagetree.urls')),
    (r'^_quiz/', include('quizblock.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^munin/', include('munin.urls')),
    (r'^stats/', direct_to_template, {'template': 'stats.html'}),
    (r'smoketest/', include('smoketest.urls')),
    (r'^site_media/(?P<path>.*)$',
     'django.views.static.serve', {'document_root': site_media_root}),
    (r'^uploads/(?P<path>.*)$',
     'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^_pagetree/', include('pagetree.urls')),
    (r'^_quiz/', include('quizblock.urls')),
    (r'^edit/(?P<path>.*)$', 'teachdentistry.main.views.edit_page',
     {}, 'edit-page'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^favicon.ico$',
                             'django.views.static.serve',
                             {'document_root': '../media/img/favicon.ico'}),)

urlpatterns += patterns(
    '',
    (r'^(?P<path>.*)$', 'teachdentistry.main.views.page'),
) + staticmedia.serve()
