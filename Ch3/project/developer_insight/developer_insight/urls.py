"""developer_insight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from index.views import DDC_Sitemap, Static_URL, DDC_Feed
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'board':DDC_Sitemap(),
    'static':Static_URL()
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('', include('board.urls')),
    path('', include('send.urls')),
    path('api/', include('core.urls')),
    path('summernote/', include('django_summernote.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    path('feed/rss/',DDC_Feed() ),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)