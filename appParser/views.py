import os
import csv
from datetime import date, datetime, timedelta
from .forms import ConfigForm, ConfigLogForm
from django.contrib.auth.models import User
from .models import Config, Frequency, ConfigLog, Status
from django.http import FileResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test


def contract_view(request):
    contracts = Config.objects.all()
    return render(request, 'appParser/dashboard.html', {'contracts': contracts})

def status_view(request):

    if request.method == 'POST':
        start_date_str = request.POST.get('StartDate')
        end_date_str = request.POST.get('EndDate')
        configs = ConfigLog.objects.filter(dateExecuted__gte=start_date_str, dateExecuted__lt=end_date_str)
    else:
        configs = ConfigLog.objects.filter(dateExecuted__date=date.today())

    return render(request, 'appParser/logStatus.html', {'configs': configs, 'reportDate': date.today()})

def import_config_data(request):
    with open('C:\\Users\\DELL\\OneDrive\\Documents\\WebProject\\SDSol\\projectParser\\contractData.csv'
            , newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Config.objects.create(
                # id = ['id'],
                fileType = row['ContractName'],
                fullName = row['Full Name'],
                sourceFileLocation = ['add/add/folder'],
                sourceFileNamingConvention = row['File Naming Convention'],
                frequency = Frequency.objects.get(id=row['frequencyid']),
                outputSchemaName = row['Schema Name'],
                outputObjectName = row['Object Name'],
                parser = row['PreProcessor'],
                isActive = True,
                createdBy = User.objects.get(id=row['createdBy']),
            )

    print("Data imported successfully!")
    return redirect('dashboard')

def import_status_data(request):
    with open('C:\\Users\\DELL\\OneDrive\\Documents\\WebProject\\SDSol\\projectParser\\statusLogData.csv'
            , newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            ConfigLog.objects.create(
                sourceLogID = row['LogID'],
                fileType = Config.objects.filter(fileType=row['ContractID']).first(),
                sourceFile = row['SourceFile'],
                status = Status.objects.get(name=row['Status']),
            )

    print("Data imported successfully!")
    return redirect('dashboard')

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def show_config(request, config_id):
    contract = get_object_or_404(Config, pk=config_id)

    if request.method == 'POST':
        form = ConfigForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ConfigForm(instance=contract)

    return render(request, 'appParser/edit_contract.html', {'form': form, 'contract': contract})

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def show_stats(request, log_id):
    configlog = get_object_or_404(ConfigLog, pk=log_id)
    status = configlog.status.name

    if request.method == 'POST':
        form = ConfigLogForm(request.POST, instance=configlog)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ConfigLogForm(instance=configlog)

    return render(request, 'appParser/view_log.html', {'form': form, 'configlog': configlog, 'status': status})

def download_file_view(request):
    if request.method == "POST":
        status = "Success"  # logic to determine status again (server-side validation)
        if status == "Success":
            file_path = 'C:\\Users\\DELL\\OneDrive\\Documents\\WebProject\\SDSol\\projectParser\\dataModel.xlsx'
            if os.path.exists(file_path):
                return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='file.xlsx')
            else:
                return HttpResponseNotFound("File not found.")
        else:
            return HttpResponseNotFound("Download not allowed.")
