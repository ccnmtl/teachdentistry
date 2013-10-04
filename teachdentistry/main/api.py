from tastypie import fields
from tastypie.authentication import Authentication
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.resources import ModelResource
from teachdentistry.main.models import DentalEducator, Institution, \
    TeachingResponsibility, TimeCommitment


class LoggedInAuthentication(Authentication):
    # All users must be logged in before accessing the json API
    def is_authenticated(self, request, **kwargs):
        return request.user.is_authenticated()


class InstitutionResource(ModelResource):
    class Meta:
        queryset = Institution.objects.all()
        allowed_methods = ['get']
        authentication = LoggedInAuthentication()


class TeachingResponsibilityResource(ModelResource):
    class Meta:
        queryset = TeachingResponsibility.objects.all()
        allowed_methods = ['get']
        authentication = LoggedInAuthentication()
        filtering = {'id': ALL}


class TimeCommitmentResource(ModelResource):
    class Meta:
        queryset = TimeCommitment.objects.all()
        allowed_methods = ['get']
        authentication = LoggedInAuthentication()
        filtering = {'id': ALL}


class DentalEducatorResource(ModelResource):
    institution = fields.ForeignKey(InstitutionResource,
                                    'institution',
                                    full=True)

    teaching_responsibility = fields.ManyToManyField(
        TeachingResponsibilityResource,
        'teaching_responsibility',
        full=True)

    paid_time_commitment = fields.ForeignKey(TimeCommitmentResource,
                                             'paid_time_commitment',
                                             full=True)

    volunteer_time_commitment = fields.ForeignKey(TimeCommitmentResource,
                                                  'volunteer_time_commitment',
                                                  full=True)

    class Meta:
        limit = 256
        queryset = DentalEducator.objects.all()
        resource_name = 'educator'
        allowed_methods = ['get']
        excludes = ['display_name', 'first_name', 'last_name']
        authentication = LoggedInAuthentication()
        filtering = {
            'career_stage': ALL,
            'gender': ALL,
            'teaching_responsibility': ALL_WITH_RELATIONS,
            'paid_time_commitment': ALL_WITH_RELATIONS,
            'volunteer_time_commitment': ALL_WITH_RELATIONS
        }

    def dehydrate(self, bundle):
        bundle.data['name'] = bundle.obj.educator_display_name()
        return bundle
