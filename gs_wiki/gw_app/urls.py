from django.urls import path
from gw_app import views

app_name = 'gw_app'
urlpatterns = [
    path('api/char/list', views.get_char_list),
    path('api/weapon/list', views.get_weapon_list),
    path('api/version', views.get_version),
    path('api/gacha_pool', views.get_gacha_pool),
    path('api/comming_brith', views.get_comming_brith),
    path('api/search', views.query_search),
    path('api/char/detail', views.query_char),
    path('api/weapon/detail', views.query_weapon),
    path('api/material', views.query_material),
    path('api/timer', views.query_timer),
]
