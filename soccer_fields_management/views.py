from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import SoccerField, Rental
from .forms import RentalForm
from datetime import date
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import pdb

class IndexView(ListView):
    template_name = 'soccer_fields_management/soccer_field_list.html'
    queryset = SoccerField.objects.order_by('name')
    context_object_name = 'soccer_fields'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['amenities_soccer_fields'] = SoccerField.objects.filter(syntehtic_grass=True)
        context['locker_room'] = SoccerField.objects.filter(locker_room=True)
        return context

class SoccerFieldDetail(DetailView):
    model = SoccerField
    template_name = 'soccer_fields_management/soccer_field_detail.html'
    context_object_name = 'soccer_field'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rentals'] = self.object.rental_set.order_by('-rental_date')[:20]
        return context


class NewRental(CreateView):
    model = Rental
    success_url = reverse_lazy('soccer_fields_list')
    form_class = RentalForm
    object = None
    template_name = 'soccer_fields_management/new_rental.html'

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.get_form_class())
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.get_form_class())
        self.object = None
        if form.is_valid():
            return self.form_valid(form)
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        rental = form.save(commit=False)
        rental.rental_date = date.today()
        if not rental.has_got_for():
            rental.save()
            return HttpResponseRedirect(self.success_url)
        else:
            form.errors["turn"] = {"Turno ocupado"}
            return self.render_to_response(self.get_context_data(form=form))

class UpdateRental(UpdateView):
    model = Rental
    success_url = reverse_lazy('soccer_fields_list')
    form_class = RentalForm
    template_name = 'soccer_fields_management/edit_rental.html'
    object = None

    def get_object(self, queryset=None):
        self.object = super(UpdateRental, self).get_object()
        return self.object

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.get_form_class())
        form.instance = self.get_object()
        form.initial = self.object.__dict__
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.get_form_class())
        form.data = request.POST
        form.instance = self.get_object()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        rental = form.save(commit=False)
        if rental.has_got_for_update():
            form.errors["turn"] = {"Turno ocupado"}
            return self.render_to_response(self.get_context_data(form=form))
        else:
            rental.save()
            return HttpResponseRedirect(self.get_success_url())



class DeleteRental(DeleteView):
    model = Rental
    success_url = reverse_lazy('soccer_fields_list')