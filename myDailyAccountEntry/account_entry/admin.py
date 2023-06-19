from django.contrib import admin

# Register your models here.

from .models import account_database
admin.site.register(account_database)
from .models import category_list
admin.site.register(category_list)
from .models import balance_sheet
admin.site.register(balance_sheet)
