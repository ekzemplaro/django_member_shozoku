from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.MemberListView.as_view(), name='members'),
    path('member/<int:pk>', views.MemberDetailView.as_view(), name='member-detail'),
    path('syozokus/', views.SyozokuListView.as_view(), name='syozokus'),
    path('syozoku/<int:pk>', views.SyozokuDetailView.as_view(), name='syozoku-detail'),
]
