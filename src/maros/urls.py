



from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'presentation.views.home', name='home'),
    url(r'^dokonania/', 'presentation.views.dokonania', name='dokonania'),
    url(r'^kontakt/', 'presentation.views.kontakt', name='kontakt'),
    url(r'^oferta/', 'presentation.views.oferta', name='oferta'),
    url(r'^ofirmie/', 'presentation.views.ofirmie', name='ofirmie'),
    url(r'^referencje/', 'presentation.views.referencje', name='referencje'),
    url(r'^tabor/', 'presentation.views.tabor', name='tabor'),

    url(r'^admin/', include(admin.site.urls)),
] 
#to będzie kiedy przejdziemy do produkcji
if settings.DEBUG:

	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)