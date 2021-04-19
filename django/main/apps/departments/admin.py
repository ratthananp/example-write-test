# from django.contrib import admin
# from model_controller.admins import ModelControllerAdmin
# from reversion.admin import VersionAdmin

# from memo.apps.departments.models import MemoDepartment
#
#
# @admin.register(MemoDepartment)
# class MemoDepartmentAdmin(VersionAdmin, ModelControllerAdmin):
#     list_display = (
#         'id', 'code', 'name', 'original_name'
#     )
#     search_fields = (
#         'id', 'code', 'name', 'original_name'
#     )
#     list_filter = ('id', 'code', 'name', 'original_name')
