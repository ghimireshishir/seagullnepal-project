from django.shortcuts import render, get_object_or_404
from .models import Package, Booking
from .forms import BookingForm

def home(request):
    packages = Package.objects.all()
    return render(request, 'agency/home.html', {'packages': packages})

def package_detail(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    return render(request, 'agency/package_detail.html', {'package': package})

def book_package(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.package = package
            booking.save()
            return render(request, 'agency/booking_success.html', {'package': package})
    else:
        form = BookingForm()
    return render(request, 'agency/book_package.html', {'package': package, 'form': form})
