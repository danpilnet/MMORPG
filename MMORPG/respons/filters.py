from django_filters import FilterSet
from .models import Response


class ResponsFilter(FilterSet):

        class Meta:
            model = Response
            fields = ['text']
