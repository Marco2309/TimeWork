from rest_framework import permissions
from rest_framework.permissions import BasePermission


class TaskPermissions(BasePermission):
    # Message if you don't have permissions
    message = "Sorry but you don't have permissions"

    def has_permission(self, request, view):
        return True
        # if request.method == 'POST':
        #     if request.data['user'] == request.user.id:
        #         return True
        # if view.action == 'retrieve':
        #     return True
        # return False

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
