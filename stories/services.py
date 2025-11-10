# import requests
# from django.conf import settings
# from django.core.cache import cache
# from datetime import datetime
# from .models import NewsStory


# class NewsService:
#     def __init__(self):
#         self.api_key = settings.NEWSDATA_API_KEY
#         self.base_url = settings.NEWSDATA_BASE_URL

#     def fetch_india_news(self, category=None, page=1):
#         """Fetch latest news from India using NewsData.io"""
#         cache_key = f'india_news_{category}_{page}'
#         cached_data = cache.get(cache_key)
#         if cached_data:
#             return cached_data

#         # ✅ NewsData.io does NOT allow some category-country combos
#         # So handle category separately
#         params = {
#             'apikey': self.api_key,
#             'language': 'en',
#             'country': 'in',
#             'page': page
#         }

#         # NewsData.io allows only a few valid categories
#         valid_categories = ['business', 'entertainment', 'health', 'science', 'sports', 'technology', 'top']
#         if category and category in valid_categories:
#             params['category'] = category
#         else:
#             params.pop('category', None)

#         try:
#             response = requests.get(self.base_url, params=params, timeout=10)
#             data = response.json()

#             if response.status_code == 200 and data.get('results'):
#                 articles = data['results']
#                 cache.set(cache_key, articles, 1800)
#                 return articles
#             else:
#                 print(f"⚠️ No results or API error: {data}")
#                 return []
#         except Exception as e:
#             print(f"Error fetching news: {e}")
#             return []

#     def search_news(self, query, page=1):
#         """Search news by keyword using NewsData.io"""
#         cache_key = f'search_news_{query}_{page}'
#         cached_data = cache.get(cache_key)
#         if cached_data:
#             return cached_data

#         params = {
#             'apikey': self.api_key,
#             'q': query,
#             'language': 'en',
#             'page': page
#         }

#         try:
#             response = requests.get(self.base_url, params=params, timeout=10)
#             data = response.json()

#             if response.status_code == 200 and data.get('results'):
#                 articles = data['results']
#                 cache.set(cache_key, articles, 1800)
#                 return articles
#             else:
#                 print(f"⚠️ No results found for query '{query}': {data}")
#                 return []
#         except Exception as e:
#             print(f"Error searching news: {e}")
#             return []

#     def save_article_to_db(self, article):
#         """Save article to database if it doesn't exist"""
#         try:
#             url = article.get('link', '')
#             if not url:
#                 return None

#             if NewsStory.objects.filter(url=url).exists():
#                 return NewsStory.objects.get(url=url)

#             published_str = article.get('pubDate', '')
#             try:
#                 published_at = datetime.fromisoformat(published_str.replace('Z', '+00:00'))
#             except Exception:
#                 published_at = datetime.now()

#             story = NewsStory.objects.create(
#                 title=article.get('title', 'No Title'),
#                 source=article.get('source_id', 'Unknown'),
#                 url=url,
#                 published_at=published_at,
#                 summary=article.get('description', 'No description available'),
#                 content=article.get('content', ''),
#                 image_url=article.get('image_url', ''),
#                 author=(
#                     article.get('creator', [''])[0]
#                     if isinstance(article.get('creator'), list)
#                     else article.get('creator', '')
#                 ),
#                 is_live=True
#             )
#             return story
#         except Exception as e:
#             print(f"Error saving article: {e}")
#             return None















# stories/services.py

import requests

class NewsService:
    BASE_URL = "https://newsdata.io/api/1/news"
    API_KEY = "pub_553ede84a44b4b2a8ca925fa37eb3baa"  # replace with your real key if needed

    def fetch_india_news(self, category=None):
        """Fetch latest India news"""
        params = {
            "apikey": self.API_KEY,
            "country": "in",
            "language": "en",
        }
        if category:
            params["category"] = category

        try:
            response = requests.get(self.BASE_URL, params=params)
            data = response.json()
            if data.get("status") == "success" and "results" in data:
                return data["results"]
            else:
                print("⚠️ No results or API error:", data)
                return []
        except requests.exceptions.RequestException as e:
            print("Error fetching news:", e)
            return []

    def search_news(self, query):
        """Search for news articles by keyword"""
        params = {
            "apikey": self.API_KEY,
            "language": "en",
            "q": query,
        }

        try:
            response = requests.get(self.BASE_URL, params=params)
            data = response.json()
            if data.get("status") == "success" and "results" in data:
                return data["results"]
            else:
                print("⚠️ No results or API error:", data)
                return []
        except requests.exceptions.RequestException as e:
            print("Error searching news:", e)
            return []
