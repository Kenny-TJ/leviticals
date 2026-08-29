from django.shortcuts import render, get_object_or_404
from .models import (
    Article, ArticleCategory,
    Devotional,
    MusicTrack,
    Video,
    MissionStory,
    Broadcast,
    ContactMessage,
)

# ============================================================
# HOME
# ============================================================
def home(request):
    recent_articles    = Article.objects.filter(is_published=True)[:3]
    recent_devotionals = Devotional.objects.filter(is_published=True)[:1]
    recent_music       = MusicTrack.objects.filter(is_published=True)[:3]
    recent_videos      = Video.objects.filter(is_published=True)[:3]
    context = {
        'recent_articles':    recent_articles,
        'recent_devotionals': recent_devotionals,
        'recent_music':       recent_music,
        'recent_videos':      recent_videos,
    }
    return render(request, 'core/home.html', context)


# ============================================================
# ARTICLES
# ============================================================
def article_list(request):
    category_slug = request.GET.get('category')
    categories    = ArticleCategory.objects.all()
    articles      = Article.objects.filter(is_published=True)

    if category_slug:
        articles = articles.filter(category__slug=category_slug)

    context = {
        'articles':        articles,
        'categories':      categories,
        'active_category': category_slug,
    }
    return render(request, 'core/article_list.html', context)


def article_detail(request, slug):
    article          = get_object_or_404(Article, slug=slug, is_published=True)
    related_articles = Article.objects.filter(
        is_published=True,
        category=article.category
    ).exclude(slug=slug)[:3]
    context = {
        'article':          article,
        'related_articles': related_articles,
    }
    return render(request, 'core/article_detail.html', context)


# ============================================================
# DEVOTIONALS
# ============================================================
def devotional_list(request):
    devotionals = Devotional.objects.filter(is_published=True)
    context = {'devotionals': devotionals}
    return render(request, 'core/devotional_list.html', context)


def devotional_detail(request, slug):
    devotional      = get_object_or_404(Devotional, slug=slug, is_published=True)
    all_devotionals = Devotional.objects.filter(is_published=True)
    prev_dev = all_devotionals.filter(date__lt=devotional.date).first()
    next_dev = all_devotionals.filter(date__gt=devotional.date).last()
    context = {
        'devotional': devotional,
        'prev_dev':   prev_dev,
        'next_dev':   next_dev,
    }
    return render(request, 'core/devotional_detail.html', context)


# ============================================================
# MUSIC
# ============================================================
def music_list(request):
    music_type = request.GET.get('type')
    tracks     = MusicTrack.objects.filter(is_published=True)

    if music_type:
        tracks = tracks.filter(music_type=music_type)

    context = {
        'tracks':           tracks,
        'active_type':      music_type,
        'music_type_choices': MusicTrack.MUSIC_TYPE,
    }
    return render(request, 'core/music_list.html', context)


def music_detail(request, slug):
    track           = get_object_or_404(MusicTrack, slug=slug, is_published=True)
    related_tracks  = MusicTrack.objects.filter(
        is_published=True
    ).exclude(slug=slug)[:4]
    context = {
        'track':          track,
        'related_tracks': related_tracks,
    }
    return render(request, 'core/music_detail.html', context)


# ============================================================
# VIDEOS
# ============================================================
def video_list(request):
    video_type = request.GET.get('type')
    videos     = Video.objects.filter(is_published=True)

    if video_type:
        videos = videos.filter(video_type=video_type)

    context = {
        'videos':             videos,
        'active_type':        video_type,
        'video_type_choices': Video.VIDEO_TYPE,
    }
    return render(request, 'core/video_list.html', context)


def video_detail(request, slug):
    video          = get_object_or_404(Video, slug=slug, is_published=True)
    related_videos = Video.objects.filter(
        is_published=True
    ).exclude(slug=slug)[:4]
    context = {
        'video':          video,
        'related_videos': related_videos,
    }
    return render(request, 'core/video_detail.html', context)


# ============================================================
# MISSIONS
# ============================================================
def mission_list(request):
    missions = MissionStory.objects.filter(is_published=True)
    context  = {'missions': missions}
    return render(request, 'core/mission_list.html', context)


def mission_detail(request, slug):
    mission          = get_object_or_404(MissionStory, slug=slug, is_published=True)
    related_missions = MissionStory.objects.filter(
        is_published=True
    ).exclude(slug=slug)[:3]
    context = {
        'mission':          mission,
        'related_missions': related_missions,
    }
    return render(request, 'core/mission_detail.html', context)
    
    from django.contrib import messages


# ============================================================
# ABOUT
# ============================================================
def about(request):
    return render(request, 'core/about.html')


# ============================================================
# CONTACT
# ============================================================
def contact(request):
    if request.method == 'POST':
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            # We'll store it in the database — no email server needed
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            messages.success(request,
                'Thank you for reaching out, {}. We will get back to you soon.'.format(name))
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all required fields.')

    return render(request, 'core/contact.html')
    
# ============================================================
# BROADCAST
# ============================================================
def broadcast_list(request):
    broadcast_type = request.GET.get('type')
    broadcasts     = Broadcast.objects.filter(is_published=True)

    if broadcast_type:
        broadcasts = broadcasts.filter(broadcast_type=broadcast_type)

    context = {
        'broadcasts':             broadcasts,
        'active_type':            broadcast_type,
        'broadcast_type_choices': Broadcast.BROADCAST_TYPE,
    }
    return render(request, 'core/broadcast_list.html', context)


def broadcast_detail(request, slug):
    broadcast          = get_object_or_404(Broadcast, slug=slug, is_published=True)
    related_broadcasts = Broadcast.objects.filter(
        is_published=True
    ).exclude(slug=slug)[:4]
    context = {
        'broadcast':          broadcast,
        'related_broadcasts': related_broadcasts,
    }
    return render(request, 'core/broadcast_detail.html', context)
    
# ============================================================
# GIVE
# ============================================================
def give(request):
    return render(request, 'core/give.html')