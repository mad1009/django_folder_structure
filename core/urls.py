from django.urls import path, include
from django.conf import settings
from core.views import home_page
urlpatterns = [
    path("api/", include("core.api.api_urls")),
    path("", home_page, name=settings.HOME_PAGE_URL_NAME),

]
