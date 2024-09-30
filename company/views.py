from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect

from CatalystMediaTask.tasks import load_my_file
from company.models import Company
from .forms import QueryBuilderForm, UploadFileForm, UserForm
from django.db import connection
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def user_list(request):
    """list of users and user creation."""
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'New user added successfully.')
            return redirect('user_list')
    else:
        form = UserForm()
    
    users = User.objects.all()
    return render(request, 'account/users.html', {'users': users, 'form': form})

@login_required
def delete_user(request, user_id):
    """Delete a user by their ID."""
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('user_list')

def account_logout(request):
    """Log out the user and redirect to the login page."""
    logout(request)
    return redirect('/accounts/login')


@login_required
def upload_data_view(request):
    client_id = str(uuid.uuid4())
    if request.method == 'POST' :  
        new_catalyst = request.FILES['file']
        client_id = request.POST.get("client_id")
        if not new_catalyst.name.endswith('.csv') or not new_catalyst:
            messages.info(request, 'Please upload a CSV file.')
            return render(request, 'upload_data.html', {'form': form})
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            load_my_file.delay(uploaded_file.id, client_id)

            messages.success(request, 'File uploaded and processed successfully.')
            return render(request, 'upload_data.html',{'client_id':client_id })
    else:
        form = UploadFileForm()

    return render(request, 'upload_data.html', {'form': form, 'client_id':client_id })


class QueryBuilderAPIView(APIView):
    """API view to handle query building"""

    def get(self, request):
        form = QueryBuilderForm(request.GET)
        if form.is_valid():
            queryset = self._filter_queryset(form)
            count = queryset.count()
            return Response({'count': count})
        
        return Response({'error': 'Invalid query'}, status=400)

    def _filter_queryset(self, form):
        """Filter the queryset based on the valid form data."""
        queryset = Company.objects.all()
        
        filters = {
            'name__icontains': form.cleaned_data.get('keyword'),
            'industry__icontains': form.cleaned_data.get('industry'),
            'year_founded': form.cleaned_data.get('year_founded'),
            'locality__icontains': form.cleaned_data.get('city'),
            'locality__icontains': form.cleaned_data.get('state'),
            'country__icontains': form.cleaned_data.get('country'),
            'employees_from__gte': form.cleaned_data.get('employees_from'),
            'employees_to__lte': form.cleaned_data.get('employees_to'),
        }
        
        for filter_key, filter_value in filters.items():
            if filter_value:
                queryset = queryset.filter(**{filter_key: filter_value})
        
        return queryset

@login_required
def query_builder_view(request):
    """Render the query builder page."""
    return render(request, 'query_builder.html')