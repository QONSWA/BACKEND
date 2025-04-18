from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('about/', include('about.urls')),
  path('projects/', include('projects.urls')),
  path('technologies/', include('technologies.urls')),
  path('testimonials/', include('testimonials.urls')),
  path('contact/', include('contact.urls')),
  path('hero/', include('hero.urls')),
  path('footer/', include('footer.urls')),
]



if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
