from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User
from .forms import RegistationForm


# Create your views here.
# def landing_page(request):
#     return render(request, 'users/landing-page.html')


def all_users(request):
    users = User.objects.all()
    return render(request, 'users/users.html', {
            'users': users,
    })


def user_details(request, user_id):
    # selected_user = User.objects.get(id=user_id)
    selected_user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/user-details.html', {
        'fname': selected_user.fname,
        'lname': selected_user.lname,
        # 'dob': selected_user.dob,
        'gender': selected_user.get_gender_display(),
        'email': selected_user.email,
        'role': selected_user.get_role_display(),
    })


def add_user(request):
    registration_form = RegistationForm()
    if request.method == 'POST':
        registration_form = RegistationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect("/users")
    return render(request, 'users/add-user.html', {
        'form': registration_form,
    })


def update_user(request, user_id):
    # fetch the object related to passed id
    selected_user = get_object_or_404(User, id=user_id)
    # pass the object as instance in form

    registration_form = RegistationForm(request.POST or None,
                                        instance=selected_user)

    if request.method == 'POST':
        if registration_form.is_valid():
            print('Form Valid')
            registration_form.save()
            return redirect("/users")

    context = {
        'form': registration_form
    }

    return render(request, 'users/update-user.html', context)


def del_user(request, user_id):
    User.objects.filter(id=user_id).delete()
    return redirect("/users")

