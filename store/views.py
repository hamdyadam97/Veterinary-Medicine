from django.shortcuts import render, redirect
from .forms import MyFormSet, CreateStoreForm


# Create your views here.


def create_store(request):
    if request.method == 'POST':
        forms = []
        num_forms = int(request.POST.get('total_forms', 1))
        for i in range(num_forms):
            form = CreateStoreForm(request.POST, prefix=f'form{i}')
            forms.append(form)

        if all(form.is_valid() for form in forms):
            for form in forms:
                form.save()
            return redirect('store_list')
    else:
        forms = [CreateStoreForm(prefix=f'form{i}') for i in range(1)]

    return render(request, 'add_store.html', {'forms': forms})