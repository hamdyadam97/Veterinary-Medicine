from django.shortcuts import render, redirect
from .forms import MyFormSet, CreateStoreForm,formset_factory
from .models import Store
from django.core.paginator import Paginator


# Create your views here.
def create_store(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Instantiate the formset with the POST data
        forms = MyFormSet(request.POST)
        # Check if the formset is valid
        print(len(forms),'len of froms')
        for form in forms:
            print('loooooooooops')
            # Check if the individual form is valid
            if form.is_valid():
                print('foms is valid ')
                form.save()
            else:
                # Handle the case where an individual form is not valid
                # For example, you can add error messages to the form
                # or log the error
                print('Form is not valid:')
        # Redirect or return a success message
        return render(request, 'add_store.html', {'forms': forms})
    else:
        # Display empty formset
        forms = MyFormSet()

    return render(request, 'add_store.html', {'forms': forms})


def list_store(request):
    s_list = Store.objects.all()
    paginator = Paginator(s_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    stores = paginator.get_page(page_number)
    return render(request, "display_products.html", {"stores": stores})
