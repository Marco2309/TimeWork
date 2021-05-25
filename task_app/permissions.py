from rest_framework import permissions
from rest_framework.permissions import BasePermission


class TaskPermissions(BasePermission):
    # Message if you don't have permissions
    message = "Sorry but you don't have permissions"

    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT']:
            if request.data['user'] == request.user.id:
                return True
            else:
                return False
        return True

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
