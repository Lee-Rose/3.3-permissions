from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        """only the creator of an object can change it"""
        if request.method == 'GET':
            return True
        return request.user == obj.creator