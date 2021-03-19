from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):

    """Determina as permissões para uso da API"""


    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True
