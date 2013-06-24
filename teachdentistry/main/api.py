from teachdentistry.main.models import DentalEducator
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource


class LoggedInAuthentication(Authentication):
    # All users must be logged in before accessing the json API
    def is_authenticated(self, request, **kwargs):
        return request.user.is_authenticated()


class DentalEducatorResource(ModelResource):
    class Meta:
        queryset = DentalEducator.objects.all()
        resource_name = 'educator'
        allowed_methods = ['get']
        authentication = LoggedInAuthentication()
