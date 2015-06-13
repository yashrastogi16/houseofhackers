from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from models import *
from forms import *
# Create your views here.
def dashboard(request):
	content = {}
	return render_to_response('index.html', content, context_instance=RequestContext(request))
def register(request):
	content = {}
	if request.method == 'POST':
		university = request.POST.get('university')
		print university
		username = request.POST.get('username')
		print username
		link_stockroom = request.POST.get('link_stockroom')
		print link_stockroom
		location = request.POST.get('location')
		print location
		email_id = request.POST.get('email_id')
		print email_id
		self_description = request.POST.get('self_description')
		print self_description
		achievements = request.POST.get('achivements')
		print achievements
		project = request.POST.get('project')
		print project
		try:
			memberregister = contestant_info.objects.create(university=university,username=username,link_stockroom=link_stockroom,location=location,email_id=email_id,self_description=self_description,achievements=achievements,project=project)
			return render_to_response('success.html', content, context_instance=RequestContext(request))
		except Exception as e:
			print e
			return render_to_response('register.html', content, context_instance=RequestContext(request))
	return render_to_response('register.html', content, context_instance=RequestContext(request))


