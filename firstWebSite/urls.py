from django.contrib import admin
from django.urls import path
from firstWebSite.common_views import about_me, init_attempt, claim_date,calculate_age

urlpatterns = [
    path('admin/', admin.site.urls),
    path('init/aboutme/',about_me),
    path('init/',init_attempt),
    path('calc/<int:age_now>/<int:agno>', calculate_age),
    path('init/date/', claim_date),
]
