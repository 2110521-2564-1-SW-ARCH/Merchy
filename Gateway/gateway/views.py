from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User
from .forms import RegistationForm


# Create your views here.
def landing_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def all_users(request):
    users = User.objects.all()
    return render(request, 'gateway/users.html', {
            'users': users,
    })


def user_details(request, user_id):
    # selected_user = User.objects.get(id=user_id)
    selected_user = get_object_or_404(User, pk=user_id)
    return render(request, 'gateway/user-details.html', {
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
            users = User.objects.all()
            return render(request, 'gateway/users.html', {
                'users': users,
            })
    return render(request, 'gateway/add-user.html', {
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
            return all_users(request)

    context = {
        'form': registration_form
    }

    return render(request, 'gateway/update-user.html', context)


def del_user(request, user_id):
    User.objects.filter(id=user_id).delete()
    return all_users(request)

