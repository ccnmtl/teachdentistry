import debug_toolbar
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
import django.contrib.auth.views
from django.views.generic import TemplateView
import django.views.i18n
import django.views.static
from registration.backends.hmac.views import RegistrationView
from tastypie.api import Api

from teachdentistry.main.api import DentalEducatorResource, InstitutionResource
from teachdentistry.main.forms import UserProfileForm
from teachdentistry.main.views import (
    ReportView, index, profile, instructor_page, edit_page, page
)


v1_api = Api(api_name='v1')
v1_api.register(DentalEducatorResource())
v1_api.register(InstitutionResource())

admin.autodiscover()

urlpatterns = [
    url('^accounts/', include('djangowind.urls')),
    url(r'^accounts/register/$', RegistrationView.as_view(
        form_class=UserProfileForm), name='registration_register'),

    url(r'^accounts/password_change/$',
        auth_views.password_change, name='password_change'),
    url(r'^accounts/password_change/done/$',
        auth_views.password_change_done, name='password_change_done'),
    url(r'^accounts/password_reset/$',
        auth_views.password_reset, name='password_reset'),
    url(r'^accounts/password_reset/done/$',
        auth_views.password_reset_done, name='password_reset_done'),
    url(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^accounts/reset/done/$', auth_views.password_reset_complete,
        name='password_reset_complete'),

    url(r'^accounts/', include('registration.backends.hmac.urls')),

    url(r'^logout/$', django.contrib.auth.views.logout, {'next_page': '/'}),
    url(r'^$', index),
    url(r'^_pagetree/', include('pagetree.urls')),
    url(r'^_quiz/', include('quizblock.urls')),
    url(r'^_main/api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stats/$', TemplateView.as_view(template_name="stats.html")),
    url(r'smoketest/', include('smoketest.urls')),
    url(r'^uploads/(?P<path>.*)$', django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^_pagetree/', include('pagetree.urls')),
    url(r'^_quiz/', include('quizblock.urls')),
    url(r'^profile/(?P<educator_id>\d+)/$', profile, name='profile-view'),
    url(r'^instructor/(?P<path>.*)$', instructor_page),
    url(r'^edit/(?P<path>.*)$', edit_page, {}, 'edit-page'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^jsi18n', django.views.i18n.javascript_catalog),
    url(r'^report/$', ReportView.as_view()),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^favicon.ico$', django.views.static.serve,
            {'document_root': '../media/img/favicon.ico'}),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += [
    url(r'^(?P<path>.*)$', page),
]
