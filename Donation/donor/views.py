from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Donor, Recipient, Donation, Location, Event, Feedback, Branch, Contact


def home(request):
    return render(request, 'donor/home.html')


def about(request):
    return render(request, 'donor/about.html')


def contact(request):
    if request.method == 'POST':
        contact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
def contact(request):
    if request.method == 'POST':
# Create a new Contact object
     contact = Contact(
name=request.POST['name'],
email=request.POST['email'],
message=request.POST['message']
)
     contact.save() # Save the contact message to the database
     return redirect('home') # Redirect to the home page after saving
    return render(request, 'donor/contact.html')
 
# Donor Views
def donor_list(request):
    donors = Donor.objects.all()
    paginator = Paginator(donors, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'donor/donor_list.html', {'page_obj': page_obj})


def donor_detail(request, donor_id):
    donor = get_object_or_404(Donor, id=donor_id)
    feedbacks = donor.feedback_set.all()  # Get feedback related to this donor
    return render(request, 'donor/donor_detail.html', {'donor': donor, 'feedbacks': feedbacks})


def donor_create(request):
    if request.method == 'POST':
        donor = Donor(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            blood_type=request.POST['blood_type'],
            date_of_birth=request.POST['date_of_birth'],
            phone_number=request.POST['phone_number'],
            email=request.POST['email'],
            profile_picture=request.FILES.get('profile_picture')
        )
        donor.save()
        return redirect('donor_list')
    return render(request, 'donor/donor_form.html')


def donor_update(request, donor_id):
    donor = get_object_or_404(Donor, id=donor_id)
    if request.method == 'POST':
        donor.first_name = request.POST.get('first_name', donor.first_name)
        donor.last_name = request.POST.get('last_name', donor.last_name)
        donor.blood_type = request.POST.get('blood_type', donor.blood_type)
        donor.date_of_birth = request.POST.get('date_of_birth', donor.date_of_birth)
        donor.phone_number = request.POST.get('phone_number', donor.phone_number)
        donor.email = request.POST.get('email', donor.email)
        if request.FILES.get('profile_picture'):
            donor.profile_picture = request.FILES.get('profile_picture')
        donor.save()
        return redirect('donor_list')
    return render(request, 'donor/donor_form.html', {'donor': donor})


def donor_delete(request, donor_id):
    donor = get_object_or_404(Donor, id=donor_id)
    donor.delete()
    return redirect('donor_list')


# Recipient Views
def recipient_list(request):
    recipients = Recipient.objects.all()
    paginator = Paginator(recipients, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'donor/recipient_list.html', {'page_obj': page_obj})


def recipient_detail(request, recipient_id):
    recipient = get_object_or_404(Recipient, id=recipient_id)
    return render(request, 'donor/recipient_detail.html', {'recipient': recipient})


def recipient_create(request):
    if request.method == 'POST':
        recipient = Recipient(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            blood_type=request.POST['blood_type'],
            phone_number=request.POST['phone_number'],
            email=request.POST['email']
        )
        recipient.save()
        return redirect('recipient_list')
    return render(request, 'donor/recipient_form.html')


def recipient_update(request, recipient_id):
    recipient = get_object_or_404(Recipient, id=recipient_id)
    if request.method == 'POST':
        recipient.first_name = request.POST.get('first_name', recipient.first_name)
        recipient.last_name = request.POST.get('last_name', recipient.last_name)
        recipient.blood_type = request.POST.get('blood_type', recipient.blood_type)
        recipient.phone_number = request.POST.get('phone_number', recipient.phone_number)
        recipient.email = request.POST.get('email', recipient.email)
        recipient.save()
        return redirect('recipient_list')
    return render(request, 'donor/recipient_form.html', {'recipient': recipient})


def recipient_delete(request, recipient_id):
    recipient = get_object_or_404(Recipient, id=recipient_id)
    recipient.delete()
    return redirect('recipient_list')


# Donation Views
def donation_list(request):
    donations = Donation.objects.all()
    paginator = Paginator(donations, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'donor/donation_list.html', {'page_obj': page_obj})


def donation_create(request):
    if request.method == 'POST':
        Donation.objects.create(
            donor_id=request.POST['donor'],
            donation_date=request.POST['donation_date'],
            donation_location_id=request.POST['donation_location'],
            volume=request.POST['volume']
        )
        return redirect('donation_list')
    return render(request, 'donor/donation_form.html')


# Event Views
def event_list(request):
    events = Event.objects.all()
    paginator = Paginator(events, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'donor/event_list.html', {'page_obj': page_obj})
from django.shortcuts import render, get_object_or_404

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'donor/event_detail.html', {'event': event})
def event_create(request):
    locations = Location.objects.all()  # Send to template
    if request.method == 'POST':
        Event.objects.create(
            name=request.POST.get('name'),
            date=request.POST.get('date'),
            location_id=request.POST.get('location'),  
            description=request.POST.get('description'),
            event_image=request.FILES.get('event_image')
        )
        return redirect('event_list')
    return render(request, 'donor/event_form.html', {'locations': locations, 'event': None})
def event_update(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.name = request.POST.get('name', event.name)
        event.date = request.POST.get('date', event.date)
        event.location_id = request.POST.get('location', event.location_id)
        event.description = request.POST.get('description', event.description)
        if request.FILES.get('event_image'):
            event.event_image = request.FILES.get('event_image')
        event.save()
        return redirect('event_detail', event_id=event.id)
    return render(request, 'donor/event_form.html', {'event': event})
def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'donor/event_delete.html', {'event': event})

# Feedback Views
def feedback_list(request):
    feedbacks = Feedback.objects.all()
    paginator = Paginator(feedbacks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'donor/feedback_list.html', {'page_obj': page_obj})


def feedback_create(request):
    if request.method == 'POST':
        Feedback.objects.create(
            donor_id=request.POST.get('donor'),
            message=request.POST.get('message'),
            rating=request.POST.get('rating')
        )
        return redirect('feedback_list')
    return render(request, 'donor/feedback_form.html')


# Branch Views
def branch_list(request):
    branches = Branch.objects.all()
    paginator = Paginator(branches, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'donor/branch_list.html', {'page_obj': page_obj})


def branch_detail(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    return render(request, 'donor/branch_detail.html', {'branch': branch})


def branch_create(request):
    if request.method == 'POST':
        branch = Branch(
            name=request.POST['name'],
            location=request.POST['location'],
            contact_number=request.POST['contact_number']
        )
        branch.save()
        return redirect('branch_list')
    return render(request, 'donor/branch_form.html')


def branch_update(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    if request.method == 'POST':
        branch.name = request.POST['name']
        branch.location = request.POST['location']
        branch.contact_number = request.POST['contact_number']
        branch.save()
        return redirect('branch_list')
    return render(request, 'donor/branch_form.html', {'branch': branch})


def branch_delete(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    if request.method == 'POST':
        branch.delete()
        return redirect('branch_list')
    return render(request, 'donor/branch_confirm_delete.html', {'branch': branch})


# Location Views
def location_list(request):
    locations = Location.objects.all()
    paginator = Paginator(locations, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'donor/location_list.html', {'page_obj': page_obj})


def location_detail(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    return render(request, 'donor/location_detail.html', {'location': location})


def location_create(request):
    if request.method == 'POST':
        location = Location(
            name=request.POST['name'],
            address=request.POST['address'],
            contact_number=request.POST['contact_number']
        )
        location.save()
        return redirect('location_list')
    return render(request, 'donor/location_form.html')


def location_update(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    if request.method == 'POST':
        location.name = request.POST['name']
        location.address = request.POST['address']
        location.contact_number = request.POST['contact_number']
        location.save()
        return redirect('location_list')
    return render(request, 'donor/location_form.html', {'location': location})


def location_delete(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    if request.method == 'POST':
        location.delete()
        return redirect('location_list')
    return render(request, 'donor/location_confirm_delete.html', {'location': location})