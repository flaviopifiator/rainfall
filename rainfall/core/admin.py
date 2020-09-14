from django.contrib import admin


class PermissionsActionsAdmin(object):
    add_permission = True
    change_permission = True
    delete_permission = True

    def has_add_permission(self, request):
        return self.add_permission

    def has_change_permission(self, request, obj=None):
        return self.change_permission

    def has_delete_permission(self, request, obj=None):
        return self.delete_permission


class SingletonAdmin(PermissionsActionsAdmin):
    add_permission = False
    delete_permission = False