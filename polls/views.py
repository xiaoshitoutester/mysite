from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Poll, Choice

# Create your views here.
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_data')[:5]

    return render(request, 'polls/index.html', {'latest_poll_list':latest_poll_list})

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)

    return render(request, 'polls/detail.html', {'poll':poll})

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)

    return render(request, 'polls/results.html', {'poll':poll})

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'poll':poll,
            'error_msg':'请选择一个有效的选项。'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))



