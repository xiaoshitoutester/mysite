from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Poll,Choice

# Create your views here.
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_data')[:5]
    return render(request, 'polls/index.html', {'latest_poll_list':latest_poll_list})

def detail(request, poll_id):
    return HttpResponse('投票问题详情{0}'.format(poll_id))

def results(request, poll_id):
    return HttpResponse('投票问题结果{0}'.format(poll_id))

def vote(request, poll_id):
    return HttpResponse('投票页面{0}'.format(poll_id))

