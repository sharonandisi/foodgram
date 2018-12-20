from django.conf.urls import url , include
from django.conf import settings
from django.conf.urls.static import static 
from . import views

urlpatterns=[
    url('^$',views.index, name='present'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^profile/([0-9]+)/$', views.profile, name='profile'),
    url(r'^profile_edit/([0-9]+)/$', views.profile_edit, name='profile_edit'),
    url(r'^comment/([0-9]+)/$', views.comment, name='comment'),
    url(r'^new/image/([0-9]+)/$', views.new_image, name='new-image'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)