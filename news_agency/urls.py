from django.urls import path

from news_agency.views import (
    index,
    TopicListView,
    RedactorListView,
    NewspaperListView,
    RedactorDetailView,
    NewspaperDetailView,
    TopicCreateView,
    NewspaperCreateView,
    TopicDeleteView,
    TopicUpdateView,
    NewspaperDeleteView,
    RedactorDeleteView, RedactorUpdateView, RedactorCreateView,
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
    path(
        "newspapers/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),
    path(
        "newspapers/<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete"
    ),
    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-create"
    ),
    path(
        "redactors/<int:pk>/delete/",
        RedactorDeleteView.as_view(),
        name="redactor-delete"
    ),
    path(
        "redactors/<int:pk>/update/",
        RedactorUpdateView.as_view(),
        name="redactor-update"
    )
]

app_name = "news_agency"