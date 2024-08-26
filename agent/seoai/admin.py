from django.contrib import admin
from .models import ChatSession, Message

class MessageInline(admin.TabularInline):
    model = Message
    extra = 1
    fields = ('message_type', 'content', 'timestamp')
    readonly_fields = ('timestamp',)
    show_change_link = True

@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'flow_id', 'created_at', 'updated_at')
    search_fields = ('session_id', 'flow_id')
    list_filter = ('created_at', 'updated_at')
    inlines = [MessageInline]
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('session', 'message_type', 'content_preview', 'timestamp', 'created_at', 'updated_at')
    search_fields = ('session__session_id', 'content')
    list_filter = ('message_type', 'timestamp', 'created_at', 'updated_at')
    readonly_fields = ('timestamp', 'created_at', 'updated_at')

    def content_preview(self, obj):
        return obj.content[:50]
    content_preview.short_description = 'Content Preview'

