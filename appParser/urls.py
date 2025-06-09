from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.contract_view, name='dashboard'),
    path('logStatus', views.status_view, name='logStatus'),
    path('show-config/<int:config_id>/', views.show_config, name='show_config'),
    path('show-stats/<int:log_id>/', views.show_stats, name='show_stats'),
    path('importConfig/', views.import_config_data, name='importConfig'),
    path('importLogStatus/', views.import_status_data, name='importLogStatus'),
    path('download/', views.download_file_view, name='download_file'),

    
    # path('projectParser/', views.projectParser, name='projectParser'),
    # path('projectParser/result/', views.parserResult, name='parserResult'),
]
