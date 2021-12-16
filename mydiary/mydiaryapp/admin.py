from django.contrib import admin
from .models import DiaryNote, DiaryImage, Conversation, Message


# Register your models here.

class DiaryNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'date')
    list_filter = ('title', 'desc')
    list_display_links = ('title',)
    search_fields = ('title', 'desc')


class DiaryImageAdmin(admin.ModelAdmin):
    list_display = ('s3key', 's3url', 'diarynote')
    list_filter = ('s3key', 's3url', 'diarynote')
    list_display_links = ('s3key',)


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('date', 'creator')
    list_display_links = ('date', 'creator')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('text',)
    list_display_links = ('text',)


admin.site.register(DiaryNote, DiaryNoteAdmin)
admin.site.register(DiaryImage, DiaryImageAdmin)
admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Message, MessageAdmin)
