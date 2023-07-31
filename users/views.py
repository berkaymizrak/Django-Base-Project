from django.shortcuts import render
from users import filters, models, serializers, permissions
from rest_framework import viewsets


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser]
    permission_classes = (permissions.UserPermission,)
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    serializer_action_classes = {
    }
    filterset_class = filters.UserFilter
    ordering_fields = ('id', 'first_name', 'last_name', 'email', 'last_login', 'date_joined',)
    ordering = ('-date_joined',)
