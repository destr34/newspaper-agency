from django.urls import path

from news_agency.views import (
    index,
    TopicListView,
    RedactorListView,
    NewspaperListView,
    RedactorDetailView,
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
    )
]

app_name = "newsagency"