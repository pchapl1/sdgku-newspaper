from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from articles.forms import CreateArticleForm
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from articles.models import Article


class CreateArticle(LoginRequiredMixin, CreateView):
    template_name = 'articles/create_article.html'
    model = Article
    form_class = CreateArticleForm


class EditArticle(LoginRequiredMixin, UpdateView):
    template_name = 'articles/create_article.html'
    model = Article
    form_class = CreateArticleForm


class SingleArticleView(LoginRequiredMixin, DetailView):
    template_name = 'articles/read_article.html'
    model = Article
    context_object_name = 'article'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/confirm_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def get_success_url(self) -> str:
        return reverse_lazy('home')