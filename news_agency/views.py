from django.shortcuts import render
from django.views import generic

from news_agency.models import Topic, Redactor, Newspaper


def index(request):
    count_topic = Topic.objects.count()
    count_redactor = Redactor.objects.count()
    count_newspaper = Newspaper.objects.count()

    context = {
        "count_topic": count_topic,
        "count_redactor": count_redactor,
        "count_newspaper": count_newspaper
    }

    return render(request, "news_agency/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "news_agency/topic_list.html"
    paginate_by = 5


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 5
    template_name = "news_agency/redactor_list.html"


class NewspaperListView(generic.ListView):
    model = Newspaper
    paginate_by = 5
