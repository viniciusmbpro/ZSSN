from django.urls import path
from . import views

app_name = 'interface'

urlpatterns = [
    path('', views.survivors, name='survivors'),
    path('<int:pk>/', views.survivor_detail, name='survivor_detail'),
    
    path('<int:pk>/report_infected/', views.report_infected, name='report_infected'),
    path('<int:pk>/update_location/', views.update_location, name='update_location'),

    path('<int:pk>/make_trade/', views.make_trade, name='make_trade'),

    path('add_survivor/', views.add_survivor, name='add_survivor'),
    path('<int:pk>/delete_survivor/', views.delete_survivor, name='delete_survivor'),
    path('<int:pk>/update_location/', views.update_location, name='update_location'),

    path('resources_report/', views.resources_report, name='resources_report'),
]
