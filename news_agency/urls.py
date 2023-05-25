from django.urls import path

from news_agency.views import (
    index,
    TopicListView,
    RedactorListView,
    NewspaperListView,
    RedactorDetailView,
    NewspaperDetailView, TopicCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name='redactor-detail'
    ),
    path(
        "newspapers/<int:pk>/",
        NewspaperDetailView.as_view(),
        name='newspaper-detail'
    ),
    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topic-create"
    ),
]

app_name = "newsagency"