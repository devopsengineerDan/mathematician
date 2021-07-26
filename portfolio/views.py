from django.shortcuts import render
from .models import Skill, Project
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.conf import settings
import simplejson as json
from django.http import JsonResponse
import requests

from django.contrib.auth import authenticate, login
# from django.template import RequestContex

from django.shortcuts import render
 
from django.template.context_processors import csrf


import django
from django.core.mail import send_mail
from django.conf import settings

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' It is great choosing to work with a team of perfectionists'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('redirect to a new page')



# context = {}
# context.update(csrf(request))
# @csrf_exempt
# def my_view(request):

#     @csrf_protect
#     def protected_path(request):
#         do_something()

#     if some_condition():
#        return protected_path(request)
#     else:
#        do_something_else()


# def contact(request,registration_id):
#    t = loader.get_template('registration/contact.html') 
#    try:
#          registration=Registration.objects.get(pk=registration_id)
#    except Registration.DoesNotExist:
#         #  return render_to_response("login.html",{"registration_id":registration_id})
#          return render(request, "contact.html", context)
#          context_instance=RequestContext(request)

# def home(request,registration_id):
#     if request.method == "POST":
#       name = request.POST.get('name')
#       email = request.POST.get('email')
#       message = request.POST.get('message')
#       user = authenticate(name=name, email=email, message=message)
#       if user is not None:
#         if user.is_active:
#           login(request, user)
#         # success
#         else:
#          #user was not active
#            return redirect('q/',context_instance=RequestContext(user))
#       else:
#         # not a valid user
#            return redirect('q/',context_instance=RequestContext(user))
#     else:
#        # URL was accessed directly
#            return redirect('q/',context_instance=RequestContext(user))

# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from django.contrib.auth.models import User

# from .emails import send_activation_email
# from .tokens import account_activation_token

# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt, csrf_protect



# Create your views here.
def home(request):
    title = ' Home'
    projects = Project.get_all()

    return render(request, 'index.html',{
        'title': title,
        'projects':projects,
    })

def all_repos(request):
    title = 'Repos'

    all_repos = requests.get('https://api.github.com/user/repos?sort=asc&access_token={}'.format(settings.GITHUB_API))
    repos = json.loads(all_repos.content)
    # print(repos)

    return render(request, 'repos.html', {
        'title':title,
        'repos':repos
    })


def check_contact(request):
    title = 'Contact'

    check_contact = requests.get('https://api.github.com/user/contact?sort=asc&access_token={}'.format(settings.GITHUB_API))
    repos = json.loads(check_contact.content)
    # print(contact)

    return render(request, 'contact.html', {
        'title':title,
        'contact':contact
    })