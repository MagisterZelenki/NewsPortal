from django_filters import FilterSet, DateFilter
from .models import Post
import django.forms


class PostFilter(FilterSet):
    dateCreation = DateFilter(lookup_expr='gt', widget=django.forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = {
            'postTitle': ['icontains'],
            'rating': [
                'lt',  # цена должна быть меньше или равна указанной
                'gt',  # цена должна быть больше или равна указанной
            ],
        }