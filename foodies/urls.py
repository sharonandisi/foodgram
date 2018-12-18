from django.conf.urls import url
from django.conf import settings
from django.conf.urls import .static import static
from . import views

urlpatterns=[
    url('^$',views.index, name='present'),
    url(r'^search/', views.search_results, name='search_results')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)