from django.shortcuts import render, redirect
from .forms import InvoiceForm, InvoiceSearchForm
from .models import Invoice

# Create your views here.
def home_page(request):
    """This is a view function that takes in request for the home page and renders the contents"""
    title = "Welcome Gee: You are now on the home page"
    context = {
        "title" : title
    }
    return render(request, "home.html", context)

def add_invoice(request):
    """This is a view function that adds a new invoice and displays the contents"""
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect ('/add_invoice')
    context = {
        "form" : form,
        "Title" : "NEW INVOICE"
    }
    return render(request, "new_invoice.html", context)

def list_invoice_items(request):
    """function that lists the invoice items by querying the database"""
    title = "List of Invoices"
    queryset = Invoice.objects.all()
    form = InvoiceSearchForm(request.POST or None)

    context = {
        "title" : title,
        "queryset" : queryset,
        "form" : form,
    }
    if request.method == 'POST':
        queryset = Invoice.objects.filter(invoice_number__icontains=form['invoice_number'].value()), name__icontains=form['name'].value()
        return render(request, "list_invoice_items.html", context)