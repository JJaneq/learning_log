"""Defining URL addresses templates for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Main page
    path('', views.index, name='index'),
    #Displaying all topics
    path('topics/', views.topics, name='topics'),
    #Page about specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page to creating new topics
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page to creating new entries
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page to editing entries
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
