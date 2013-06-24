from teachdentistry.main.models import UserVisited, UserProfile
from teachdentistry.main.models import Institution, DentalEducator, \
    CareerType, ClinicalField, Degree, Motivation, PrimaryTraineesType, \
    TeachingResponsibility, TimeCommitment
from django.contrib import admin

admin.site.register(UserProfile)


class UserVisitedAdmin(admin.ModelAdmin):
    class Meta:
        model = UserVisited

    search_fields = ["user__user__username"]
    list_display = ("user", "section", "visited_time")

admin.site.register(UserVisited, UserVisitedAdmin)

admin.site.register(Institution)

admin.site.register(DentalEducator)

admin.site.register(CareerType)

admin.site.register(ClinicalField)

admin.site.register(Degree)

admin.site.register(Motivation)

admin.site.register(PrimaryTraineesType)

admin.site.register(TeachingResponsibility)

admin.site.register(TimeCommitment)
