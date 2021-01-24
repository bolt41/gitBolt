from django.contrib import admin
from .models import Users, SourceMoney, TransType, Trans

admin.site.register(Users)
admin.site.register(SourceMoney)
admin.site.register(TransType)
admin.site.register(Trans)
