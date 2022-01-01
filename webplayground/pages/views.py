from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import PageForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


class StaffRequiredMixin(object):
    ''' Este Mixin requerirá que el usuario sea miembro del staff '''

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_staff:
    #         return redirect(reverse_lazy('admin:login'))
    #     return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# def pages(request):
#     pages = get_list_or_404(Page)
#     return render(request, 'pages/pages.html', {'pages': pages})


class PageListView(ListView):
    model = Page


# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, 'pages/page.html', {'page': page})

class PageDetailView(DetailView):
    model = Page


@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')
    # def get_success_url(self):
    #     return reverse('pages:pages')


@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')





# class PageCreate(StaffRequiredMixin, CreateView):
#     model = Page
#     form_class = PageForm
#     # fields = ['title', 'content', 'order']
#     success_url = reverse_lazy('pages:pages')
#     # def get_success_url(self):
#     #     return reverse('pages:pages')
#
#
# class PageUpdate(StaffRequiredMixin, UpdateView):
#     model = Page
#     form_class = PageForm
#     # fields = ['title', 'content', 'order']
#     template_name_suffix = '_update_form'
#
#     def get_success_url(self):
#         return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
#
#
# class PageDelete(StaffRequiredMixin, DeleteView):
#     model = Page
#     success_url = reverse_lazy('pages:pages')
