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
		dob = request.POST.get('dob')
		print dob
		location = request.POST.get('location')
		print location
		email_id = request.POST.get('email_id')
		print email_id
		self_description = request.POST.get('self_description')
		print self_description
		achievements = request.POST.get('achivements')
		print achievements
		project_name = request.POST.get('project_name')
		print project_name
		project_link = request.POST.get('project_link')
		print project_link
		project_Description = request.POST.get('project_description')
		print project_Description
		skills_used = request.POST.get('skills')
		print skills_used
		try:
			memberregister = contestant_info.objects.create(university=university,username=username,dob=dob,location=location,email_id=email_id,self_description=self_description,achievements=achievements,project_name=project_name,project_link=project_link,project_Description=project_Description,skills_used=skills_used)
		except Exception as e:
			print e
	return render_to_response('register.html', content, context_instance=RequestContext(request))


# def register(request):
# 	content = {}
# 	content['err_msg'] = "Register Here !!!"
# 	role1 = role.objects.get(rolename='User')
# 	form = MemberForm(request.POST or None)
# 	if form.is_valid():
# 		content.update(csrf(request))
# 		form = MemberForm(request.POST or None)
# 	if request.method == 'POST':
# 		username = request.POST.get('username')
# 		gender = request.POST.get('gender')
# 		user_id = request.POST.get('user_id')
# 		password = request.POST.get('password')
# 		email_id = request.POST.get('email_id')
# 		resident_location = request.POST.get('resident_location')
# 		contact_no = request.POST.get('contact')
# 		print form.errors
# 		try:
# 			memberregister = members.objects.create(username=username,gender=gender,user_id=user_id,password=password,email_id=email_id,resident_location=resident_location,contact_no=contact_no,status='Active',role=role1)
# 			msg = "Registered successfully"
# 			content['err_msg'] = msg
# 			return render_to_response('login.html',content,context_instance=RequestContext(request)) 
# 		except:
# 			msg = "Registration Failed"
# 			content['err_msg'] = msg
# 			return render_to_response('register.html',content,context_instance=RequestContext(request))
# 	return render_to_response('register.html',content, context_instance=RequestContext(request))