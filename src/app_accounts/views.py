from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import models, forms
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from app_home_page.templatetags.util import has_group
# Create your views here.

#UPDATE
def update_accounts(request, pk):
    if request.user.pk != pk and has_group(request.user, 'Customers'):
            print(request.user.pk)
            return redirect(reverse_lazy('app_accounts:accounts-update', args=[request.user.pk]))
    if request.method == 'POST':
        user_form = forms.UserForm(request.POST, instance=User.objects.get(pk=pk))
        extension_form = forms.UserExtensionForm(request.POST, instance=User.objects.get(pk=pk).extension)
        if user_form.is_valid() and extension_form.is_valid():
            user_form.save()
            extension_form.save()
            # messages.success(request, _('Ваш профиль был успешно обновлен!'))
            previous_page = request.session['previous_page']
            del request.session['previous_page']
            # print(previous_page)
            return redirect(previous_page or reverse_lazy('app_accounts:accounts-list'))
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибки.'))
    else:
        request.session['previous_page'] = request.META.get('HTTP_REFERER')
        user_form = forms.UserForm(instance=User.objects.get(pk=pk))
        extension_form = forms.UserExtensionForm(instance=User.objects.get(pk=pk).extension)
    return render(request, 'app_accounts/accounts_update.html', {
        'user_form': user_form,
        'profile_form': extension_form
    })

#READ
class DetailAccounts(generic.DetailView):
    model = User
    template_name = 'app_accounts/accounts_detail.html'
    def get(self, request, *args, **kwargs):
        if self.request.user.pk != self.kwargs.get(self.pk_url_kwarg) and has_group(self.request.user, 'Customers'):
            print(self.request.user.pk)
            return redirect(reverse_lazy('app_accounts:accounts-detail', args=[self.request.user.pk]))
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

        # if self.request.user.pk != self.kwargs.get(self.pk_url_kwarg) and has_group(self.request.user, 'Customers'):
        #     redirect(reverse_lazy('app_accounts:accounts-detail', args=[self.request.user.pk]))

# #DELETE
# class DeleteAuthors(LoginRequiredMixin, generic.DeleteView):
#     login_url = reverse_lazy('app_admin_portal:login')
#     model = models.Authors
#     template_name = 'app_reference_book/authors_delete.html'
#     success_url = reverse_lazy('app_reference_book:authors-list')

#LIST
class ListAccounts(generic.ListView):
    paginate_by = 10
    # login_url = reverse_lazy('app_admin_portal:login')
    model = User
    template_name = 'app_accounts/accounts_list.html'