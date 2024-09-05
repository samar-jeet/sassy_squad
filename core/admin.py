

# from django.contrib import admin
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import Profile, Member
# from django.core.mail import send_mail

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False

# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline,)

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.register(Member)



# class MemberAdmin(admin.ModelAdmin):
#     list_display = ('user', 'approved')
#     actions = ['approve_members']

#     def approve_members(self, request, queryset):
#         queryset.update(approved=True)
#         for member in queryset:
#             member.user.is_active = True
#             member.user.save()
#             # Notify user via email
#             send_mail(
#                 'Your account has been approved',
#                 'Congratulations! Your account has been approved.',
#                 'your_email@example.com',
#                 [member.user.email],
#                 fail_silently=False,
#             )

#     approve_members.short_description = "Approve selected members"

# admin.site.register(Member, MemberAdmin)






