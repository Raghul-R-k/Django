from django.urls import path
from .views import land_page, second_page, detail_page, About_us, post_page_view,commentCreateView

urlpatterns = [
    path('Index', land_page, name='land_page'),
    path('Card_detail/<slug:slug>/', detail_page, name='detail_page'),
    path('cards', second_page, name='second_page'),
    path('About', About_us, name='About_us'),
    path('Add_Cards', post_page_view.as_view(), name='simple_form'),
    path('comments', commentCreateView.as_view(), name='commentCreateView'),
]
