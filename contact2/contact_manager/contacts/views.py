from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import ContactForm

def home(request):
    contacts = request.session.get('contacts', [])
    query = request.GET.get('query', '')

    if query:
        contacts = [c for c in contacts if query.lower() in c['name'].lower() or query.lower() in c['email'].lower()]

    return render(request, 'contacts/home.html', {'contacts': contacts, 'query': query})

def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.cleaned_data
            contacts = request.session.get('contacts', [])
            contacts.append(contact)
            request.session['contacts'] = contacts
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})

def delete_contact(request, email):
    contacts = request.session.get('contacts', [])
    contacts = [c for c in contacts if c['email'] != email]
    request.session['contacts'] = contacts
    return redirect('home')

def send_email(request, email):
    contacts = request.session.get('contacts', [])
    contact = next((c for c in contacts if c['email'] == email), None)

    if contact:
        send_mail(
            subject="New Contact Added",
            message=f"Contact Details:\nName: {contact['name']}\nEmail: {contact['email']}\nPhone: {contact['phone']}\nAddress: {contact['address']}",
            from_email="your-email@example.com",
            recipient_list=[email],
            fail_silently=False,
        )

    return redirect('home')
