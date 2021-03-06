from rest_framework.permissions import BasePermission


class TaskPermissions(BasePermission):
    # Message if you don't have permissions
    message = "Sorry but you don't have permissions"

    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH']:
            if request.data['user'] == request.user.id:
                return True
            else:
                return False
        return True

    def has_object_permission(self, request, view, obj):
        print(obj.user.id)
        if obj.user.id == request.user.id:
            return True
        return False
