from django.urls import path
from . import views


app_name = 'upload'

urlpatterns = [
    path ('add_publication/', views.add_publication, name='add_publication'),
    path ('', views.publication_list, name='publication_list'),
    path ('publications/upload', views.upload_publication, name='upload_publication'),
    path ('details/<int:id>/<slug:Issn>',
        views.upload_details, name='upload_details'),
    path ('delete_publication/<id>', views.delete_publication, name='delete_publication'),
    path ('like/', views.like_public, name='like_public'),
]
