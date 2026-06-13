from rest_framework.permissions import BasePermission

class IsAnonymous(BasePermission):
    """Only unauthenticated users are allowed"""
    
    def has_permission(self, request, view):
        return not request.user.is_authenticated
