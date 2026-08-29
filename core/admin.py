from django.contrib import admin
from .models import (
    Article, ArticleCategory,
    Devotional,
    MusicTrack,
    Video,
    MissionStory,
    Broadcast,
    ContactMessage,
)


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display  = ['title', 'category', 'author', 'is_published', 'created_at']
    list_filter   = ['is_published', 'category']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published']


@admin.register(Devotional)
class DevotionalAdmin(admin.ModelAdmin):
    list_display  = ['topic', 'date', 'author', 'is_published']
    list_filter   = ['is_published']
    search_fields = ['topic', 'life_nugget']
    prepopulated_fields = {'slug': ('topic',)}
    list_editable = ['is_published']


@admin.register(MusicTrack)
class MusicTrackAdmin(admin.ModelAdmin):
    list_display  = ['title', 'artist', 'music_type', 'is_published']
    list_filter   = ['is_published', 'music_type']
    search_fields = ['title', 'lyrics']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display  = ['title', 'video_type', 'is_published', 'created_at']
    list_filter   = ['is_published', 'video_type']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published']


@admin.register(MissionStory)
class MissionStoryAdmin(admin.ModelAdmin):
    list_display  = ['title', 'location', 'author', 'is_published']
    list_filter   = ['is_published']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published']


@admin.register(Broadcast)
class BroadcastAdmin(admin.ModelAdmin):
    list_display  = ['title', 'broadcast_type', 'is_published', 'created_at']
    list_filter   = ['is_published', 'broadcast_type']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display  = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter   = ['is_read']
    search_fields = ['name', 'email', 'subject']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']