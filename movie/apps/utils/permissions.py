from rest_framework import permissions
from rest_framework.permissions import BasePermission


class CustomPermissionClass(BasePermission):
    def has_permission(self, request, view):
        return True

    # todo:
    # 1. create User
    # 2. create Roles (admin, premium, )


