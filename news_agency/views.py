from django.shortcuts import render

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