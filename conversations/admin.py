from statistics import mode
from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """ """
    filter_horizontal = [
        "participants",
    ]

    list_display = (
        "__str__",
        "count_messages",
        "count_participants",
        "created_at",
    )


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """ """
    list_display = [
        "__str__",
        "created_at"
    ]

