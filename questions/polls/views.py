from django.shortcuts import render
from django.views import generic

from .models import Question
from .mixins import RequireLoginMixin

# Create your views here.


class IndexView(RequireLoginMixin, generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


"""
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

"""

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class DeleteView(generic.DetailView):
    model = Question
    success_url = "/polls/"
