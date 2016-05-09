from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from registration.backends.hmac.views import RegistrationView
from tastypie.api import Api

from teachdentistry.main.api import DentalEducatorResource, InstitutionResource
from teachdentistry.main.forms import UserProfileForm
from teachdentistry.main.views import ReportView


v1_api = Api(api_name='v1')
v1_api.register(DentalEducatorResource())
v1_api.register(InstitutionResource())

admin.autodiscover()

urlpatterns = patterns(
    '',
    ('^accounts/', include('djangowind.urls')),
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
    url(r'^accounts/reset/done/$',
        auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'^accounts/', include('registration.backends.hmac.urls')),

    (r'^logout/$',
     'django.contrib.auth.views.logout',
     {'next_page': '/'}),
    (r'^$', 'teachdentistry.main.views.index'),
    (r'^_pagetree/', include('pagetree.urls')),
    (r'^_quiz/', include('quizblock.urls')),
    (r'^_main/api/', include(v1_api.urls)),
    (r'^admin/', include(admin.site.urls)),
    (r'^stats/$', TemplateView.as_view(template_name="stats.html")),
    (r'smoketest/', include('smoketest.urls')),
    (r'^uploads/(?P<path>.*)$',
     'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^_pagetree/', include('pagetree.urls')),
    (r'^_quiz/', include('quizblock.urls')),
    url(r'^profile/(?P<educator_id>\d+)/$',
        'teachdentistry.main.views.profile',
        name='profile-view'),
    (r'^instructor/(?P<path>.*)$',
     'teachdentistry.main.views.instructor_page'),
    (r'^edit/(?P<path>.*)$', 'teachdentistry.main.views.edit_page',
     {}, 'edit-page'),
    (r'^pages/', include('django.contrib.flatpages.urls')),
    (r'^jsi18n', 'django.views.i18n.javascript_catalog'),
    (r'^report/$', ReportView.as_view()),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^favicon.ico$',
                             'django.views.static.serve',
                             {'document_root': '../media/img/favicon.ico'}),)

urlpatterns += patterns(
    '',
    (r'^(?P<path>.*)$', 'teachdentistry.main.views.page'),
)
