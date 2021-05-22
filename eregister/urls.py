from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from eregister import settings

urlpatterns = [
    path('', include('events.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "E-Register Admin"
admin.site.site_title = "E-Register Admin Portal"
admin.site.index_title = "Welcome to E-Register Portal"
