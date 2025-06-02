from django.shortcuts import render, redirect
from .forms import InvoiceForm, InvoiceSearchForm, InvoiceUpdateForm
from .models import Invoice
from django.contrib import messages

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
    total_invoices = Invoice.objects.count()
    queryset = Invoice.objects.order_by('-invoice_date-')[:6]
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Invoice saved successfully')
        return redirect ('/list_invoice')
    context = {
        "form" : form,
        "Title" : "NEW INVOICE",
        "total_invoices" : total_invoices,
        "queryset" : queryset,
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
    
def update_invoice(request, pk):
    """function that update and edit any of the invoice"""
    queryset = Invoice.objects.get(id=pk)
    form = InvoiceUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = InvoiceUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_invoice')
        
    context = {
        'form' : form
    }
    return render(request, 'new_invoice.html', context)

def delete_invoice(request, pk):
    """function that deletes request"""
    queryset = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/list_invoice')
    return render (request, 'delete_invoice.html')