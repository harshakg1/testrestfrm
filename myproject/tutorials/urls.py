from django.urls import path 
from tutorials import views 
 
urlpatterns = [ 
    path(r'^api/tutorials', views.TutorialList.as_view(), name='tutorials'),
   
] 
#path(r'^api/tutorials', views.tutorial_list),

#path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
 #   path(r'^api/tutorials/published$', views.tutorial_list_published)