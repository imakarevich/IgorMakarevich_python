from django.shortcuts import render
from django.urls import reverse_lazy
from . import models, forms
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
###########################CRUDL-PublishingHouse#################################
#CREATE 
class CreatePublishingHouse(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.PublishingHouse
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    form_class = forms.PublishingHouseForm
    template_name = 'app_reference_book/publishing_house_create.html'
    success_url = reverse_lazy('app_reference_book:publishing-house-list')

#READ
class ReadPublishingHouse(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = models.PublishingHouse
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    template_name = 'app_reference_book/publishing_house_read.html'

#UPDATE
class UpdatePublishingHouse(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.PublishingHouse
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    form_class = forms.PublishingHouseForm
    template_name = 'app_reference_book/publishing_house_update.html'
    success_url = reverse_lazy('app_reference_book:publishing-house-list')

#DELETE
class DeletePublishingHouse(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.PublishingHouse
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    template_name = 'app_reference_book/publishing_house_delete.html'
    success_url = reverse_lazy('app_reference_book:publishing-house-list')

#LIST
class ListPublishingHouse(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 15
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    model = models.PublishingHouse
    template_name = 'app_reference_book/publishing_house_list.html'

###########################CRUDL-Authors#################################
#CREATE 
class CreateAuthors(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('app_admin_portal:login')
    model = models.Authors
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    form_class = forms.AuthorsForm
    template_name = 'app_reference_book/authors_create.html'
    success_url = reverse_lazy('app_reference_book:authors-list')

#READ
class ReadAuthors(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = models.Authors
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    template_name = 'app_reference_book/authors_read.html'

#UPDATE
class UpdateAuthors(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('app_admin_portal:login')
    model = models.Authors
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    form_class = forms.AuthorsForm
    template_name = 'app_reference_book/authors_update.html'
    success_url = reverse_lazy('app_reference_book:authors-list')

#DELETE
class DeleteAuthors(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('app_admin_portal:login')
    model = models.Authors
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    template_name = 'app_reference_book/authors_delete.html'
    success_url = reverse_lazy('app_reference_book:authors-list')

#LIST
class ListAuthors(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 15
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    login_url = reverse_lazy('app_admin_portal:login')
    model = models.Authors
    template_name = 'app_reference_book/Authors_list.html'

###########################CRUDL-Genres#################################
#CREATE 
class CreateGenres(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Genres
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    form_class = forms.GenresForm
    template_name = 'app_reference_book/genres_create.html'
    success_url = reverse_lazy('app_reference_book:genres-list')

#READ
class ReadGenres(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = models.Genres
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    template_name = 'app_reference_book/genres_read.html'

#UPDATE
class UpdateGenres(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Genres
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    form_class = forms.GenresForm
    template_name = 'app_reference_book/genres_update.html'
    success_url = reverse_lazy('app_reference_book:genres-list')

#DELETE
class DeleteGenres(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Genres
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    template_name = 'app_reference_book/genres_delete.html'
    success_url = reverse_lazy('app_reference_book:genres-list')

#LIST
class ListGenres(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 15
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    model = models.Genres
    template_name = 'app_reference_book/genres_list.html'

###########################CRUDL-Series#################################
#CREATE 
class CreateSeries(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Series
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    form_class = forms.SeriesForm
    template_name = 'app_reference_book/series_create.html'
    success_url = reverse_lazy('app_reference_book:series-list')

#READ
class ReadSeries(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = models.Series
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    template_name = 'app_reference_book/series_read.html'

#UPDATE
class UpdateSeries(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Series
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    form_class = forms.SeriesForm
    template_name = 'app_reference_book/series_update.html'
    success_url = reverse_lazy('app_reference_book:series-list')

#DELETE
class DeleteSeries(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Series
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    template_name = 'app_reference_book/series_delete.html'
    success_url = reverse_lazy('app_reference_book:series-list')

#LIST
class ListSeries(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 15
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    model = models.Series
    template_name = 'app_reference_book/series_list.html'

###########################CRUDL-Status#################################
#CREATE 
class CreateStatus(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Status
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    form_class = forms.StatusForm
    template_name = 'app_reference_book/status_create.html'
    success_url = reverse_lazy('app_reference_book:status-list')

#READ
class ReadStatus(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = models.Status
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    template_name = 'app_reference_book/status_read.html'

#UPDATE
class UpdateStatus(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Status
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    form_class = forms.StatusForm
    template_name = 'app_reference_book/status_update.html'
    success_url = reverse_lazy('app_reference_book:status-list')

#DELETE
class DeleteStatus(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Status
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    template_name = 'app_reference_book/status_delete.html'
    success_url = reverse_lazy('app_reference_book:status-list')

#LIST
class ListStatus(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    paginate_by = 15
    login_url = reverse_lazy('app_admin_portal:login')
    permission_required = 'app_accounts.access_for_managers_admin'
    model = models.Status
    template_name = 'app_reference_book/status_list.html'
