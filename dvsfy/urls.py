
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView

from diversify.views import landing_page_view

urlpatterns = [
    path('', landing_page_view),
    path('', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    re_path('app/', include('diversify.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

