from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.MemberListView.as_view(), name='members'),
    path('member/<int:pk>', views.MemberDetailView.as_view(), name='member-detail'),
    path('syozokus/', views.SyozokuListView.as_view(), name='syozokus'),
    path('syozoku/<int:pk>', views.SyozokuDetailView.as_view(), name='syozoku-detail'),
]
#
urlpatterns += [  
    path('member/create/', views.MemberCreate.as_view(), name='member_create'),
    path('member/<int:pk>/update/', views.MemberUpdate.as_view(), name='member_update'),
    path('member/<int:pk>/delete/', views.MemberDelete.as_view(), name='member_delete'),
]
#
