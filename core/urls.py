from django.urls import path
from django.conf import settings
from core.views import home_page
urlpatterns = [
    path("", home_page, name=settings.HOME_PAGE_URL_NAME)
]
