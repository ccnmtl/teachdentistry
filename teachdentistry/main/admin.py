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

# SUGGESTED_TRAINEE_VALUES =
#     [("Predoctoral dental students",
#         "Predoctoral dental students"),
#     ("Postgraduate (Residents/Fellows)",
#         "Postgraduate (Residents/Fellows)"),
#     ("Dental Hygienists",
#         "Dental Hygienists"),
#     ("Other Health Care Professionals (medical, nursing, nutrition, etc",
#         "Other Health Care Professionals (medical, nursing, nutrition, etc")]



# class AcademicTitleWidget(widgets.MultiWidget):
#     def __init__(self, attrs=None):
#         # create choices for days, months, years
#         # example below, the rest snipped for brevity.
#         SUGGESTED_TITLES = [("Instructor/Lecturer", "Instructor/Lecturer"),
#                             ("Assistant Professor", "Assistant Professor"),
#                             ("Associate Professor", "Associate Professor"),
#                             ("Professor", "Professor")]
#
#         _widgets = (
#             widgets.TextInput(),
#             widgets.Select(attrs=attrs, choices=SUGGESTED_TITLES)
#         )
#         super(widgets.MultiWidget, self).__init__(_widgets, attrs)
#
#     def decompress(self, value):
#         if value:
#             return [value.day, value.month, value.year]
#         return [None, None, None]
#
#     def format_output(self, rendered_widgets):
#         return u''.join(rendered_widgets)
#
#     def value_from_datadict(self, data, files, name):
#         datelist = [
#             widget.value_from_datadict(data, files, name + '_%s' % i)
#             for i, widget in enumerate(self.widgets)]
#         try:
#             D = date(day=int(datelist[0]), month=int(datelist[1]),
#                     year=int(datelist[2]))
#         except ValueError:
#             return ''
#         else:
#             return str(D)
#
# class AcademicTitleAdminForm(forms.ModelForm):
#     class Meta:
#         model = AcademicTitle
#         widgets = {
#             'academic_title': AcademicTitleWidget
#         }

#class ProductAdmin(admin.ModelAdmin):
#    form = ProductAdminForm

#class AcademicTitleAdmin(admin.ModelAdmin):
