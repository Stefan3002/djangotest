from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
                  path("january", views.indexViews.as_view()),
                  path('february/<int:pk>', views.februaryView.as_view())
              ]
