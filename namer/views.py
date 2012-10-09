from django.http import HttpResponse




from django.contrib.auth.models import Permission
from django.core.urlresolvers import reverse


from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, Template, Context
from django.template.loader import get_template
from django.core.context_processors import csrf
from models import *
from forms import *
from django.db.models import Q
# Create your views here.

@login_required 
def index(request):
    #show table with computer groups
    groups = ComputerGroup.objects.all()
    c = {'user': request.user, 'groups':groups, }
    return render_to_response('namer/index.html', c, context_instance=RequestContext(request)) 
    
    
#new computer group
@login_required
def new_computer_group(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = ComputerGroupForm(request.POST)
        if form.is_valid():
            new_computer_group = form.save(commit=False)
            new_computer_group.save()
            return redirect('namer.views.show_group', new_computer_group.id)
    else:
        form = ComputerGroupForm()
    c = {'form': form,}
    return render_to_response('forms/new_computer_group.html', c, context_instance=RequestContext(request))

#edit computer group
@login_required
def edit_computer_group(request, group_id):
    group = get_object_or_404(ComputerGroup, pk=group_id)
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = ComputerGroupForm(request.POST, instance=group)
        if form.is_valid():
            new_computer_group = form.save(commit=False)
            new_computer_group.save()
            return redirect('namer.views.show_group', new_computer_group.id)
    else:
        form = ComputerGroupForm(instance=grpup)
    c = {'form': form,}
    return render_to_response('forms/new_computer_group.html', c, context_instance=RequestContext(request))

#new computer

#edit computer

#show computer group
@login_required
def show_group(request, group_id):
    group = get_object_or_404(ComputerGroup, pk=group_id)
    c = { 'user': request.user, 'group':group }
    return render_to_response('namer/show_group.html', c, context_instance=RequestContext(request))