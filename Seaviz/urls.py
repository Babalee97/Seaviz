from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static  import static
from rest_framework.urlpatterns import format_suffix_patterns

from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('visual/', views.PlottingView.as_view(), name = 'visual'),
    path('load_data/', views.DataLoadingView.as_view(), name = 'data_loading'),
    path('clear/', views.clear_user_data, name = 'clear_user')
]
urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
