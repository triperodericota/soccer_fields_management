from django.urls import path
from . import views

urlpatterns = [
    path('index', views.IndexView.as_view(), name='soccer_fields_list'),
    path('<int:pk>', views.SoccerFieldDetail.as_view(), name='soccer_field_detail'),
    path('new_rental', views.NewRental.as_view(), name='new_rental'),
    path('edit_rental/<int:pk>', views.UpdateRental.as_view(), name='edit_rental'),
    path('delete_rental/<int:pk>', views.DeleteRental.as_view(), name='delete_rental')

]