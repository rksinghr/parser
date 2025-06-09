# from .models import Lead
# from .forms import LeadForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# @login_required
# def dashboard(request):
#     leads = Lead.objects.all().order_by('-created_at')
#     return render(request, 'app_crm/dashboard.html', {'leads': leads})

# @login_required
# def lead_create(request):
#     form = LeadForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('dashboard')
#     return render(request, 'app_crm/lead_form.html', {'form': form})

# @login_required
# def lead_detail(request, pk):
#     lead = get_object_or_404(Lead, pk=pk)
#     return render(request, 'app_crm/lead_detail.html', {'lead': lead})

# @login_required
# def lead_update(request, pk):
#     lead = get_object_or_404(Lead, pk=pk)
#     form = LeadForm(request.POST or None, instance=lead)
#     if form.is_valid():
#         form.save()
#         return redirect('dashboard')
#     return render(request, 'app_crm/lead_form.html', {'form': form})

# @login_required
# def lead_delete(request, pk):
#     lead = get_object_or_404(Lead, pk=pk)
#     lead.delete()
#     return redirect('dashboard')

