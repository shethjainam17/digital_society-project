from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name')

# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Chairman,UserAdmin)
admin.site.register(Member,UserAdmin)
admin.site.register(Watchman,UserAdmin)
admin.site.register(Event)
admin.site.register(Complain)
admin.site.register(Notice)
admin.site.register(Visitors)
admin.site.register(photos)
admin.site.register(Suggestion)
admin.site.register(Video)






