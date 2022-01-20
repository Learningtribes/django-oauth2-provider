from django.contrib import admin

from provider.oauth2.models import AccessToken, Grant, Client, RefreshToken


@admin.register(AccessToken)
class AccessTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'token', 'expires', 'scope',)
    raw_id_fields = ('user',)


@admin.register(Grant)
class GrantAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'code', 'expires',)
    raw_id_fields = ('user',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('url', 'user', 'redirect_uri', 'client_id', 'client_type')
    raw_id_fields = ('user',)

    def get_queryset(self, request):
        qs = super(ClientAdmin, self).get_queryset(request)
        return qs.exclude(user__username__in=["lms_catalog_service_user", "veda_service_user"])


admin.site.register(RefreshToken)
