import django_filters
from .models import Teachers

CHOICES =[
        ["last_name", "от А до Я"],
        #["-last_name", "от Я до А"],
        ["email", "по почте а-я"],
        ["-email", "по почте я-а"]
]

class TeachersFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(name='last_name', lookup_expr='icontains')
	email__gt = django_filters.CharFilter(name='email', lookup_expr='gt')
    email__lt = django_filters.CharFilter(name='email', lookup_expr='lt')
	ordering = django_filters.OrderingFilter(choices=CHOICES, required=True, empty_label=None,)
    
    class Meta:
        model = Teachers
        exclude = [field.name for field in Teachers._meta.fields]
        order_by_field = 'last_name'