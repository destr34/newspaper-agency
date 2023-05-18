from django.urls import path

from news_agency.views import index, TopicListView, RedactorListView

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/", RedactorListView.as_view(), name="redactor-list"),
]

app_name = "newsagency"