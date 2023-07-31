from django_filters import rest_framework as filters
from users.models import User


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'last_login',
                  'date_joined',)
