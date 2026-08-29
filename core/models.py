from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


def unique_slug(instance, title, slug_field='slug'):
    """Generate a unique slug by appending a number if needed."""
    slug = slugify(title)
    ModelClass = instance.__class__
    unique = slug
    counter = 1
    while ModelClass.objects.filter(**{slug_field: unique}).exclude(
            pk=instance.pk).exists():
        unique = f"{slug}-{counter}"
        counter += 1
    return unique


# ============================================================
# ARTICLE
# ============================================================
class ArticleCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Article Categories"


class Article(models.Model):
    title        = models.CharField(max_length=300)
    slug         = models.SlugField(unique=True, blank=True)
    category     = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, blank=True)
    author       = models.CharField(max_length=150, default='Kenny Mercy')
    body         = RichTextUploadingField()
    cover_image  = models.ImageField(upload_to='articles/', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at   = models.DateTimeField(default=timezone.now)
    updated_at   = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


# ============================================================
# DEVOTIONAL
# ============================================================
class Devotional(models.Model):
    topic           = models.CharField(max_length=300)
    slug            = models.SlugField(unique=True, blank=True)
    scripture       = models.CharField(max_length=200, help_text="e.g. John 3:16")
    scripture_text  = RichTextUploadingField(help_text="The full scripture passage")
    life_nugget     = RichTextUploadingField(help_text="The main devotional body")
    prayer          = RichTextUploadingField()
    further_studies = models.CharField(max_length=300, blank=True,
                                       help_text="e.g. Psalm 23, Romans 8:1-11")
    cover_image     = models.ImageField(upload_to='devotionals/', blank=True, null=True)
    author          = models.CharField(max_length=150, default='Kenny Mercy')
    is_published    = models.BooleanField(default=False)
    date            = models.DateField(default=timezone.now)
    created_at      = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(self, self.topic)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} — {self.topic}"

    class Meta:
        ordering = ['-date']


# ============================================================
# MUSIC
# ============================================================
class MusicTrack(models.Model):
    MUSIC_TYPE = [
        ('music_video', 'Music Video'),
        ('lyrics_video', 'Lyrics Video'),
        ('audio', 'Audio'),
    ]
    title        = models.CharField(max_length=300)
    slug         = models.SlugField(unique=True, blank=True)
    artist       = models.CharField(max_length=150, default='Kenny Mercy')
    music_type   = models.CharField(max_length=20, choices=MUSIC_TYPE, default='audio')
    youtube_url  = models.URLField(blank=True, help_text="YouTube embed link")
    lyrics       = models.TextField(blank=True)
    chords       = models.TextField(blank=True, help_text="Chord notations")
    cover_image  = models.ImageField(upload_to='music/', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at   = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


# ============================================================
# VIDEO
# ============================================================
class Video(models.Model):
    VIDEO_TYPE = [
        ('sermon', 'Sermon'),
        ('testimony', 'Testimony'),
        ('music_video', 'Music Video'),
        ('broadcast', 'Broadcast'),
        ('other', 'Other'),
    ]
    title        = models.CharField(max_length=300)
    slug         = models.SlugField(unique=True, blank=True)
    video_type   = models.CharField(max_length=20, choices=VIDEO_TYPE, default='other')
    youtube_url  = models.URLField(help_text="YouTube embed link")
    description  = models.TextField(blank=True)
    thumbnail    = models.ImageField(upload_to='videos/', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at   = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


# ============================================================
# MISSION STORY
# ============================================================
class MissionStory(models.Model):
    title        = models.CharField(max_length=300)
    slug         = models.SlugField(unique=True, blank=True)
    location     = models.CharField(max_length=200, blank=True,
                                    help_text="e.g. Ogoni, Rivers State")
    body         = RichTextUploadingField()
    cover_image  = models.ImageField(upload_to='missions/', blank=True, null=True)
    author       = models.CharField(max_length=150, default='Kenny Mercy')
    is_published = models.BooleanField(default=False)
    created_at   = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Mission Stories"


# ============================================================
# BROADCAST
# ============================================================
class Broadcast(models.Model):
    BROADCAST_TYPE = [
        ('podcast', 'Podcast'),
        ('live', 'Live Broadcast'),
        ('recorded', 'Recorded Broadcast'),
    ]
    title          = models.CharField(max_length=300)
    slug           = models.SlugField(unique=True, blank=True)
    broadcast_type = models.CharField(max_length=20, choices=BROADCAST_TYPE,
                                      default='podcast')
    description    = models.TextField(blank=True)
    embed_url      = models.URLField(blank=True, help_text="YouTube, Spotify, or podcast link")
    cover_image    = models.ImageField(upload_to='broadcasts/', blank=True, null=True)
    is_published   = models.BooleanField(default=False)
    created_at     = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


# ============================================================
# CONTACT MESSAGE
# ============================================================
class ContactMessage(models.Model):
    name       = models.CharField(max_length=150)
    email      = models.EmailField()
    subject    = models.CharField(max_length=300, blank=True)
    message    = models.TextField()
    is_read    = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} — {self.subject or 'No subject'}"

    class Meta:
        ordering = ['-created_at']