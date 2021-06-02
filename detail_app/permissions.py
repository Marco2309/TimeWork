from rest_framework.permissions import BasePermission


class DetailPermissions(BasePermission):
    # Message if you don't have permissions
    message = "Sorry but you don't have permissions"

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if obj.id == request.user.id:
            return True
        return False
