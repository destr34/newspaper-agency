from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from news_agency.forms import CreateRedactorForm, CreateNewspaperForm, \
    TopicSearchForm
from news_agency.models import Topic, Redactor, Newspaper


@login_required
def index(request):
    count_topic = Topic.objects.count()
    count_redactor = Redactor.objects.count()
    count_newspaper = Newspaper.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "count_topic": count_topic,
        "count_redactor": count_redactor,
        "count_newspaper": count_newspaper,
        "num_visits": num_visits + 1,
    }

    return render(request, "news_agency/index.html", context=context)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "news_agency/topic_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)

        name_topic = self.request.GET.get("name_topic", "")

        context["search_form"] = TopicSearchForm(initial={
            "name_topic": name_topic
        })

        return context

    def get_queryset(self):
        form = TopicSearchForm(self.request.GET)
        queryset = super(TopicListView, self).get_queryset()

        if form.is_valid():
            return queryset.filter(
                topic__icontains=form.cleaned_data["name_topic"]
            )

        return queryset


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("news-agency:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("news-agency:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("news-agency:topic-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 5
    template_name = "news_agency/redactor_list.html"
    queryset = Redactor.objects.prefetch_related("newspapers")


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = CreateRedactorForm
    success_url = reverse_lazy("news-agency:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    template_name = "news_agency/redactor_confirm_delete.html"
    success_url = reverse_lazy("news-agency:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = CreateRedactorForm
    success_url = reverse_lazy("news-agency:redactor-list")

    def get_success_url(self):
        return reverse(
            "news-agency:redactor-detail",
            kwargs={"pk": self.object.pk}
        )


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 5
    queryset = Newspaper.objects.select_related("topic")


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = CreateNewspaperForm
    success_url = reverse_lazy("news-agency:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = CreateNewspaperForm
    success_url = reverse_lazy("news-agency:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("news-agency:newspaper-list")
    queryset = Newspaper.objects.select_related("topic")
