from rest_framework.permissions import BasePermission


class IsArtist(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.artist == request.user