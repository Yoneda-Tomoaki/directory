from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('member/list/',views.MembersListView.as_view(),name="MembersListView"),
    path('member/create/', views.MembersCreateView.as_view(), name="Members_create"),
    path('member/detail/<int:pk>',views.MembersDetailView.as_view(),name="Members_detail"),
    path('member/update/<int:pk>',views.MemberUpdateView.as_view(),name="Members_update"),
    path('member/delete/<int:pk>',views.MemberDeleteView.as_view(),name="Members_delete")
    ]