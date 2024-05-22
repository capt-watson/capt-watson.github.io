"""Define URL patterns for learning logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'  ## Tells django that following url belongs to this app_name.

urlpatterns = [
    ## Home page
    path('', views.index, name='index'),  ## Index or Home page URL which is blank
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    ## Page for adding new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    ## Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
## In the above code, path() func takes 3 arguments. 
## 1. Blank string which is the URL pattern for the home page.
## 2. It does this by searching all the URL patterns we've defined to find one that matches the current request. Once requested URL matched, Django calls index() func from views.py.
## 3. The name argument is used to give the URL a name. This name can be used to refer to the URL later in code.