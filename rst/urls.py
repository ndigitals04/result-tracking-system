from django.urls import path
from . import views

app_name = "rst"
urlpatterns = [
    path('', views.index, name="index"),
    path('admin-dashboard/', views.adminDashboard, name="adminPage"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('admin-dashboard/upload-result/', views.search, name="search"),
    path('admin-dashboard/upload-result/<int:student_id>/', views.upload_result, name="upload"),
    path('view_result/', views.view_result, name="view_result"),
    path('view_result/<level>/<semester>/', views.view_level_result, name="view_level_result"),
]
