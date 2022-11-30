from django.shortcuts import render
from django.urls import reverse_lazy
from . import models, forms
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
###########################CRUDL-PublishingHouse#################################
#CREATE 
class CreatePublishingHouse(generic.CreateView):
    model = models.PublishingHouse
    form_class = forms.PublishingHouseForm
    template_name = 'app_reference_book/publishing_house_create.html'
    success_url = reverse_lazy('app_reference_book:publishing-house-list')

#READ
class ReadPublishingHouse(generic.DetailView):
    model = models.PublishingHouse
    template_name = 'app_reference_book/publishing_house_read.html'

#UPDATE
class UpdatePublishingHouse(generic.UpdateView):
    model = models.PublishingHouse
    form_class = forms.PublishingHouseForm
    template_name = 'app_reference_book/publishing_house_update.html'
    success_url = reverse_lazy('app_reference_book:publishing-house-list')

#DELETE
class DeletePublishingHouse(generic.DeleteView):
    model = models.PublishingHouse
    template_name = 'app_reference_book/publishing_house_delete.html'
    success_url = reverse_lazy('app_reference_book:publishing-house-list')

#LIST
class ListPublishingHouse(generic.ListView):
    paginate_by = 15
    model = models.PublishingHouse
    template_name = 'app_reference_book/publishing_house_list.html'

###########################CRUDL-Authors#################################
#CREATE 
class CreateAuthors(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('app_admin_portal:login')
    model = models.Authors
    form_class = forms.AuthorsForm
    template_name = 'app_reference_book/authors_create.html'
    success_url = reverse_lazy('app_reference_book:authors-list')

#READ
class ReadAuthors(generic.DetailView):
    model = models.Authors
    template_name = 'app_reference_book/authors_read.html'

#UPDATE
class UpdateAuthors(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('app_admin_portal:login')
    model = models.Authors
    form_class = forms.AuthorsForm
    template_name = 'app_reference_book/authors_update.html'
    success_url = reverse_lazy('app_reference_book:authors-list')

#DELETE
class DeleteAuthors(LoginRequiredMixin, generic.DeleteView):
    login_url = reverse_lazy('app_admin_portal:login')
    model = models.Authors
    template_name = 'app_reference_book/authors_delete.html'
    success_url = reverse_lazy('app_reference_book:authors-list')

#LIST
class ListAuthors(LoginRequiredMixin, generic.ListView):
    paginate_by = 15
    login_url = reverse_lazy('app_admin_portal:login')
    model = models.Authors
    template_name = 'app_reference_book/Authors_list.html'

###########################CRUDL-Genres#################################
#CREATE 
class CreateGenres(generic.CreateView):
    model = models.Genres
    form_class = forms.GenresForm
    template_name = 'app_reference_book/genres_create.html'
    success_url = reverse_lazy('app_reference_book:genres-list')

#READ
class ReadGenres(generic.DetailView):
    model = models.Genres
    template_name = 'app_reference_book/genres_read.html'

#UPDATE
class UpdateGenres(generic.UpdateView):
    model = models.Genres
    form_class = forms.GenresForm
    template_name = 'app_reference_book/genres_update.html'
    success_url = reverse_lazy('app_reference_book:genres-list')

#DELETE
class DeleteGenres(generic.DeleteView):
    model = models.Genres
    template_name = 'app_reference_book/genres_delete.html'
    success_url = reverse_lazy('app_reference_book:genres-list')

#LIST
class ListGenres(generic.ListView):
    paginate_by = 15
    model = models.Genres
    template_name = 'app_reference_book/genres_list.html'

###########################CRUDL-Series#################################
#CREATE 
class CreateSeries(generic.CreateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'app_reference_book/series_create.html'
    success_url = reverse_lazy('app_reference_book:series-list')

#READ
class ReadSeries(generic.DetailView):
    model = models.Series
    template_name = 'app_reference_book/series_read.html'

#UPDATE
class UpdateSeries(generic.UpdateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'app_reference_book/series_update.html'
    success_url = reverse_lazy('app_reference_book:series-list')

#DELETE
class DeleteSeries(generic.DeleteView):
    model = models.Series
    template_name = 'app_reference_book/series_delete.html'
    success_url = reverse_lazy('app_reference_book:series-list')

#LIST
class ListSeries(generic.ListView):
    paginate_by = 15
    model = models.Series
    template_name = 'app_reference_book/series_list.html'

###########################CRUDL-Status#################################
#CREATE 
class CreateStatus(generic.CreateView):
    model = models.Status
    form_class = forms.StatusForm
    template_name = 'app_reference_book/status_create.html'
    success_url = reverse_lazy('app_reference_book:status-list')

#READ
class ReadStatus(generic.DetailView):
    model = models.Status
    template_name = 'app_reference_book/status_read.html'

#UPDATE
class UpdateStatus(generic.UpdateView):
    model = models.Status
    form_class = forms.StatusForm
    template_name = 'app_reference_book/status_update.html'
    success_url = reverse_lazy('app_reference_book:status-list')

#DELETE
class DeleteStatus(generic.DeleteView):
    model = models.Status
    template_name = 'app_reference_book/status_delete.html'
    success_url = reverse_lazy('app_reference_book:status-list')

#LIST
class ListStatus(generic.ListView):
    paginate_by = 15
    model = models.Status
    template_name = 'app_reference_book/status_list.html'
