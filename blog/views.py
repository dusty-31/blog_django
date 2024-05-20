from django.views.generic import TemplateView, DetailView, CreateView, UpdateView

from blog.models import Post


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DjangoBlog'
        context['posts'] = Post.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'DjangoBlog - {self.object.title}'
        return context


class PostCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'context']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['title', 'context']

    def form_valid(self, form):
        return super().form_valid(form)
