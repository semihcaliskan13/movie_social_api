from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class ListMoviesPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.has_perm('quote.list_quotes')
        return False
class IsMemberOfGroup(BasePermission):
    def has_permission(self, request, view):
        group_name = 'a'  # İzin vermek istediğiniz grup adı
        return request.user.groups.filter(name=group_name).exists()
