from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """Home page for learning_logs"""
    return render(request, 'learning_logs/index.html')  ## Here render() uses 'learning_logs/index.html' template to build page.

@login_required             ## checks if a user is logged in & django runs the code in topics only if they are. Else will be redirected to login page.
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required               ## checks if a user is logged in & django runs the code in
def topic(request, topic_id):
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    ## Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic"""  ## user initially requests a blank form using a GET request, browser submits filled form using POST request.
    if request.method != 'POST':                    ## Checks if request method is GET or POST
        ## No data submitted; create a blank form.
        form = TopicForm()          ## django creates a blank form
    else:
        ## POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')  ## Redirects user back to the topic page after they submit their topic
    
    ## Display blank or invalid form.
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        ## No data submitted, create a blank form
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)  ##Tells Django to create new_entry obj & assign it to new_entry, without saving it to database yet. 
            new_entry.topic = topic
            new_entry.save()                    ## save the new_entry to the database
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    ## Displays a blank or invalid form    
    context = {'topic': topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request, entry_id):
    """Edit an exiting entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        ## Initial request; pre-fill form with the current entry
        form = EntryForm(instance=entry)
    else:
        ## POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learningLogs:topic', topic_id=topic.id)

    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)        

## View func() takes in info from request, prepares data needed to generate a page with help of a template, and then sends the data back to the browser.