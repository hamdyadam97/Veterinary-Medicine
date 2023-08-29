
from django.shortcuts import render
from .forms import my_form_set

def create_product(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Instantiate the formset with the POST data
        forms = my_form_set(request.POST)
        # Check if the formset is valid
        print(len(forms),'len of froms')
        for form in forms:
            print('loooooooooops')
            print(form.has_changed(), 'form.has_changed()')
            # Check if the individual form is valid
            if form.is_valid() and form.has_changed():
                print('foms is valid ')
                form.save()
            else:
                # Handle the case where an individual form is not valid
                # For example, you can add error messages to the form
                # or log the error
                print('Form is not valid:')
        # Redirect or return a success message
        return render(request, 'add_product.html', {'forms': forms})
    else:
        # Display empty formset
        forms = my_form_set()
    return render(request, 'add_product.html', {'forms': forms})