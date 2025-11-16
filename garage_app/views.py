from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from decimal import Decimal
from .models import vehicle, jobitem, invoice
from .forms import VehicleForm, JobItemForm, InvoiceForm

def home(request):
    return render(request, "garage_app/home.html")

# VEHICLES
def vehicle_list(request):
    vehicles = vehicle.objects.all()
    return render(request, "garage_app/vehicle_list.html", {"vehicles": vehicles})

def vehicle_add(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("vehicle_list")
    return render(request, "garage_app/form.html", {"form": form})

def vehicle_detail(request, pk):
    vehicle = get_object_or_404(vehicle, pk=pk)
    jobs = vehicle.jobs.all()
    return render(request, "garage_app/vehicle_detail.html", {"vehicle": vehicle, "jobs": jobs})

# JOB ITEMS (sticky notes)
def job_add(request):
    form = JobItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("vehicle_list")
    return render(request, "garage_app/form.html", {"form": form})

# INVOICES
def invoice_add(request):
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("invoice_list")
    return render(request, "garage_app/form.html", {"form": form})

def invoice_list(request):
    invoices = invoice.objects.all()
    return render(request, "garage_app/invoice_list.html", {"invoices": invoices})

def invoice_detail(request, pk):
    invoice = get_object_or_404(invoice, pk=pk)
    return render(request, "garage_app/invoice_detail.html", {"invoice": invoice})

# DAY END REPORT
def day_end(request):
    today = timezone.localdate()
    invoices = invoice.objects.filter(issued_at__date=today)

    total = sum(i.total_amount() for i in invoices)
    paid = sum(i.total_amount() for i in invoices if i.paid)
    unpaid = total - paid

    return render(request, "garage_app/day_end.html", {
        "invoices": invoices,
        "total": total,
        "paid": paid,
        "unpaid": unpaid,
        "date": today
    })
