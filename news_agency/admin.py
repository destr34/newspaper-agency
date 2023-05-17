from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from news_agency.models import Topic, Newspaper, Redactor


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    search_fields = ["title"]


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ["title", "publishers"]
    list_display = ["title", "topic", "published_date"]


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    search_fields = ["first_name", "last_name"]
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                    )
                },
            ),
        )
    )
