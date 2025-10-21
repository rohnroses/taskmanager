from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 


router = DefaultRouter() 
router.register(r'tasks', views.TaskViewSet, basename='task')

urlpatterns = [
    path('', views.TaskHome.as_view(), name='home'),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls')),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_task/', views.AddTask.as_view(), name='add_task'), 
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
]
