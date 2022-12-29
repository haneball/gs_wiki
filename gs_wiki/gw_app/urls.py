from django.urls import path
from gw_app import views

app_name = 'gw_app'
urlpatterns = [
    path('api/queryChar/kw=<keyword>', views.query_char),
    path('api/queryWeapon/kw=<keyword>', views.query_weapon),
    path('api/getCharList', views.get_char_list),
    path('api/getCharDetail/id=<int:id>', views.get_char_detail),
    path('api/getWeaponList', views.get_weapon_list),
    path('api/getWeaponDetail/id=<int:id>', views.get_weapon_detail),
]
