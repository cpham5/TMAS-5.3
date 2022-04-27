from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), #Add index, main page, to urlpatterns
    path('add/', views.add, name='add'), #Add add, story addition form, to urlpatterns
    path('addStory/', views.addStory, name='addStory'), #Add add, story addition page, to urlpatterns
    path('edit<int:storyID>', views.edit, name='edit'), # add edit, edit story page, to url patterns
    path('editstory<int:storyID>', views.editReplace, name='editReplace'), # add editReplace, edit story form, to urlpatterns
    path('deleteStory<int:storyID>', views.deleteStory, name='deleteStory'),
    path('adminPage/', views.adminPage, name='adminPage'),
    path('admin/', views.admin, name='admin'),
    path('delete/', views.delete, name='delete'),
]