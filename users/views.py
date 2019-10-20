from django.template import loader
from django.http import HttpResponse
from .models import Weeb
from django.core import serializers

# Create your views here.
def index(request):
    users_list = serializers.serialize('json', Weeb.objects.all())
    # template = loader.get_template('users/index.html')
    # context = {
    #     'users_list': users_list,
    # }
    # return HttpResponse(template.render(context, request))
    return HttpResponse(users_list, content_type="application/json")