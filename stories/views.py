# # stories/views.py

# from django.shortcuts import render, get_object_or_404, redirect
# from django.core.paginator import Paginator
# from django.contrib import messages
# from .models import NewsStory
# from .services import NewsService


# def story_list(request):
#     """Display list of all stories (from DB + live API)"""
#     category = request.GET.get('category', '')
#     search_query = request.GET.get('q', '')
#     page = int(request.GET.get('page', 1))

#     news_service = NewsService()

#     # Fetch live news
#     if search_query:
#         live_articles = news_service.search_news(search_query, page)
#     else:
#         live_articles = news_service.fetch_india_news(category, page)

#     # Fetch DB stories
#     db_stories = NewsStory.objects.all()

#     if category:
#         db_stories = db_stories.filter(category__icontains=category)
#     if search_query:
#         db_stories = db_stories.filter(title__icontains=search_query)

#     context = {
#         'live_articles': live_articles,
#         'db_stories': db_stories,
#         'category': category,
#         'search_query': search_query,
#         'categories': [
#             'business',
#             'entertainment',
#             'general',
#             'health',
#             'science',
#             'sports',
#             'technology',
#         ],
#     }

#     return render(request, 'stories/story_list.html', context)


# def story_detail(request, story_id):
#     """Display detailed news story from the database"""
#     story = get_object_or_404(NewsStory, pk=story_id)
#     feedbacks = story.feedbacks.all().order_by('-created_at')

#     total_feedbacks = feedbacks.count()
#     avg_rating = round(sum([f.rating for f in feedbacks]) / total_feedbacks, 1) if total_feedbacks > 0 else 0

#     context = {
#         'story': story,
#         'feedbacks': feedbacks,
#         'total_feedbacks': total_feedbacks,
#         'avg_rating': avg_rating,
#     }

#     return render(request, 'stories/story_detail.html', context)


# def live_article_detail(request):
#     """Display live article fetched from API and save to DB"""
#     url = request.GET.get('url', '')
#     title = request.GET.get('title', '')
#     source = request.GET.get('source', '')
#     description = request.GET.get('description', '')
#     image = request.GET.get('image', '')
#     author = request.GET.get('author', '')
#     published = request.GET.get('published', '')
#     content = request.GET.get('content', '')

#     if not url:
#         messages.error(request, 'Invalid article URL.')
#         return redirect('stories:story_list')

#     story = NewsStory.objects.filter(url=url).first()

#     if not story:
#         from datetime import datetime
#         try:
#             published_at = datetime.fromisoformat(published.replace('Z', '+00:00'))
#         except:
#             published_at = datetime.now()

#         story = NewsStory.objects.create(
#             title=title,
#             source=source,
#             url=url,
#             published_at=published_at,
#             summary=description,
#             content=content,
#             image_url=image,
#             author=author,
#             is_live=True,
#         )

#     return redirect('stories:story_detail', story_id=story.id)











# # stories/views.py

# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib import messages
# from .models import NewsStory
# from .services import NewsService


# def story_list(request):
#     """Display list of all stories (from DB + live API)"""
#     category = request.GET.get('category', '')
#     search_query = request.GET.get('q', '')

#     news_service = NewsService()

#     # ✅ Fetch live news correctly (no page argument)
#     if search_query:
#         live_articles = news_service.search_news(search_query)
#     else:
#         live_articles = news_service.fetch_india_news(category)

#     # ✅ Fetch DB stories
#     db_stories = NewsStory.objects.all()
#     if category:
#         db_stories = db_stories.filter(category__icontains=category)
#     if search_query:
#         db_stories = db_stories.filter(title__icontains=search_query)

#     context = {
#         'live_articles': live_articles,
#         'db_stories': db_stories,
#         'category': category,
#         'search_query': search_query,
#         'categories': [
#             'business',
#             'entertainment',
#             'general',
#             'health',
#             'science',
#             'sports',
#             'technology',
#         ],
#     }

#     return render(request, 'stories/story_list.html', context)


# def story_detail(request, story_id):
#     """Display detailed news story from the database"""
#     story = get_object_or_404(NewsStory, pk=story_id)
#     feedbacks = story.feedbacks.all().order_by('-created_at')

#     total_feedbacks = feedbacks.count()
#     avg_rating = round(sum([f.rating for f in feedbacks]) / total_feedbacks, 1) if total_feedbacks > 0 else 0

#     context = {
#         'story': story,
#         'feedbacks': feedbacks,
#         'total_feedbacks': total_feedbacks,
#         'avg_rating': avg_rating,
#     }

#     return render(request, 'stories/story_detail.html', context)


# def live_article_detail(request):
#     """Display live article fetched from API and save to DB"""
#     url = request.GET.get('url', '')
#     title = request.GET.get('title', '')
#     source = request.GET.get('source', '')
#     description = request.GET.get('description', '')
#     image = request.GET.get('image', '')
#     author = request.GET.get('author', '')
#     published = request.GET.get('published', '')
#     content = request.GET.get('content', '')

#     if not url:
#         messages.error(request, 'Invalid article URL.')
#         return redirect('stories:story_list')

#     story = NewsStory.objects.filter(url=url).first()

#     if not story:
#         from datetime import datetime
#         try:
#             published_at = datetime.fromisoformat(published.replace('Z', '+00:00'))
#         except:
#             published_at = datetime.now()

#         story = NewsStory.objects.create(
#             title=title,
#             source=source,
#             url=url,
#             published_at=published_at,
#             summary=description,
#             content=content,
#             image_url=image,
#             author=author,
#             is_live=True,
#         )

#     return redirect('stories:story_detail', story_id=story.id)














# stories/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import NewsStory
from .services import NewsService


def story_list(request):
    """Display list of all stories (from DB + live API)"""
    category = request.GET.get('category', '')
    search_query = request.GET.get('q', '')

    news_service = NewsService()

    # ✅ Fetch live news correctly (no page argument)
    if search_query:
        live_articles = news_service.search_news(search_query)
    else:
        live_articles = news_service.fetch_india_news(category)

    # ✅ Fetch DB stories
    db_stories = NewsStory.objects.all()
    if category:
        db_stories = db_stories.filter(category__icontains=category)
    if search_query:
        db_stories = db_stories.filter(title__icontains=search_query)

    context = {
        'live_articles': live_articles,
        'db_stories': db_stories,
        'category': category,
        'search_query': search_query,
        'categories': [
            'business',
            'entertainment',
            'general',
            'health',
            'science',
            'sports',
            'technology',
        ],
    }

    return render(request, 'stories/story_list.html', context)


def story_detail(request, story_id):
    """Display detailed news story from the database"""
    story = get_object_or_404(NewsStory, pk=story_id)
    feedbacks = story.feedbacks.all().order_by('-created_at')

    total_feedbacks = feedbacks.count()
    avg_rating = round(sum([f.rating for f in feedbacks]) / total_feedbacks, 1) if total_feedbacks > 0 else 0

    context = {
        'story': story,
        'feedbacks': feedbacks,
        'total_feedbacks': total_feedbacks,
        'avg_rating': avg_rating,
    }

    return render(request, 'stories/story_detail.html', context)


def live_article_detail(request):
    """Display live article fetched from API and save to DB"""
    url = request.GET.get('url', '')
    title = request.GET.get('title', '')
    source = request.GET.get('source', '')
    description = request.GET.get('description', '')
    image = request.GET.get('image', '')
    author = request.GET.get('author', '')
    published = request.GET.get('published', '')
    content = request.GET.get('content', '')

    # ✅ If URL missing, generate a fallback one
    if not url:
        from django.utils.text import slugify
        slug_title = slugify(title)[:50] if title else "article"
        url = f"https://news360india.local/{slug_title}"

    # ✅ Now proceed normally
    story = NewsStory.objects.filter(url=url).first()

    if not story:
        from datetime import datetime
        try:
            published_at = datetime.fromisoformat(published.replace('Z', '+00:00'))
        except:
            published_at = datetime.now()

        story = NewsStory.objects.create(
            title=title or "Untitled Article",
            source=source or "Unknown Source",
            url=url,
            published_at=published_at,
            summary=description or "No description available.",
            content=content or "Content not available.",
            image_url=image or "",
            author=author or "Unknown",
            is_live=True,
        )

    return redirect('stories:story_detail', story_id=story.id)


# ✅ Add this for debugging API response
def debug_api(request):
    """Debug view to check API response"""
    from .services import NewsService
    import json

    news_service = NewsService()
    articles = news_service.fetch_india_news()

    debug_info = {
        'total_articles': len(articles),
        'first_article': articles[0] if articles else None
    }

    return render(request, 'stories/debug.html', {
        'debug_info': json.dumps(debug_info, indent=2)
    })
