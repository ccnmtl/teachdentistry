from tastypie import fields
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource
from teachdentistry.main.models import DentalEducator, Institution


class LoggedInAuthentication(Authentication):
    # All users must be logged in before accessing the json API
    def is_authenticated(self, request, **kwargs):
        return request.user.is_authenticated()


class InstitutionResource(ModelResource):
    class Meta:
        queryset = Institution.objects.all()
        allowed_methods = ['get']
        authentication = LoggedInAuthentication()


class DentalEducatorResource(ModelResource):
    institution = fields.ForeignKey(InstitutionResource,
                                    'institution', full=True)

    class Meta:
        queryset = DentalEducator.objects.all()
        resource_name = 'educator'
        allowed_methods = ['get']
        excludes = ['display_name', 'first_name', 'last_name']
        authentication = LoggedInAuthentication()

    def dehydrate(self, bundle):
        bundle.data['name'] = bundle.obj.educator_display_name()
        return bundle
