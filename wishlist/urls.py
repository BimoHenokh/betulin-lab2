from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import receive_request
from wishlist.views import request_json
from wishlist.views import show_xml_by_id
from wishlist.views import show_json_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', receive_request, name='receive_request'),
    path('json/', request_json, name='request_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]