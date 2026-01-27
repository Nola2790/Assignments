from django.urls import path
from . import views

urlpatterns = [
    # Home/About
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Contact
    path('contact/', views.contact, name='contact'),  # Contact form

    # Donors
    path('donors/', views.donor_list, name='donor_list'),
    path('donors/create/', views.donor_create, name='donor_create'),
    path('donors/<int:donor_id>/', views.donor_detail, name='donor_detail'),
    path('donors/update/<int:donor_id>/', views.donor_update, name='donor_update'),
    path('donors/delete/<int:donor_id>/', views.donor_delete, name='donor_delete'),

    # Recipients
    path('recipients/', views.recipient_list, name='recipient_list'),
    path('recipients/create/', views.recipient_create, name='recipient_create'),
    path('recipients/<int:recipient_id>/', views.recipient_detail, name='recipient_detail'),
    path('recipients/update/<int:recipient_id>/', views.recipient_update, name='recipient_update'),
    path('recipients/delete/<int:recipient_id>/', views.recipient_delete, name='recipient_delete'),

    # Donations
    path('donations/', views.donation_list, name='donation_list'),
    path('donations/create/', views.donation_create, name='donation_create'),

    # Events
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/delete/<int:event_id>/', views.event_delete
    
    
    , name='event_delete'),
    path('events/update/<int:event_id>/', views.event_update, name='event_update'),
    # Feedback
    path('feedbacks/', views.feedback_list, name='feedback_list'),
    path('feedbacks/create/', views.feedback_create, name='feedback_create'),
   
    # Branches
    path('branches/', views.branch_list, name='branch_list'),
    path('branches/create/', views.branch_create, name='branch_create'),
    path('branches/<int:branch_id>/', views.branch_detail, name='branch_detail'),
    path('branches/update/<int:branch_id>/', views.branch_update, name='branch_update'),
    path('branches/delete/<int:branch_id>/', views.branch_delete, name='branch_delete'),
    path('locations/', views.location_list, name='location_list'),
    path('locations/create/', views.location_create, name='location_create'),
    path('locations/<int:location_id>/', views.location_detail, name='location_detail'),
    path('locations/update/<int:location_id>/', views.location_update, name='location_update'),
    path('locations/delete/<int:location_id>/', views.location_delete, name='location_delete'),
        path('locations/create/', views.location_create, name='location_create'),
]