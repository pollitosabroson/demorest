from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from books.views import LibroViewSet, AutorViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'libros', LibroViewSet)
router.register(r'autores', AutorViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
