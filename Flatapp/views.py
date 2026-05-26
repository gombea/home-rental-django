from django.urls import reverse
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
import random
from django.shortcuts import render

# Create your views here.

def index(request):
    apart = Apartment.objects.filter(status=1)
    return render(request, "home.html", locals())

def contact(request):
    return render(request, "contact.html",locals())

def about(request):
    return render(request, "about.html",locals())

def user_register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        address = request.POST['address']
        mobile = request.POST['mobile']
        aadhar = request.POST['aadhar']
        sec_question = request.POST['sec_question']
        answer = request.POST['answer']
        aadhar_img = request.FILES['aadhar_img']
        gender = request.POST['gender']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already Exist.')
            return redirect('user_login')

        # Create user and registration
        user = User.objects.create_user(first_name=first_name, username=email, password=password)
        Registration.objects.create(user=user, address=address, mobile=mobile, aadhar=aadhar,
                                        sec_question=sec_question, answer=answer, aadhar_img=aadhar_img, gender=gender)

        messages.success(request, "Registration successful.")
        return redirect('user_login')
    return render(request, "user_register.html")

def owner_register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        address = request.POST['address']
        mobile = request.POST['mobile']
        elect_img = request.FILES['elect_img']
        sec_question = request.POST['sec_question']
        answer = request.POST['answer']
        aadhar_img = request.FILES['aadhar_img']
        gender = request.POST['gender']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email is already Exist.')
            return redirect('user_login')

        # Create user and registration
        user = User.objects.create_user(first_name=first_name, username=email, password=password)
        Owner.objects.create(user=user, address=address, mobile=mobile, elect_img=elect_img,
                                        sec_question=sec_question, answer=answer, aadhar_img=aadhar_img, gender=gender)

        messages.success(request, "Registration successful.")
        return redirect('user_login')
    return render(request, "owner_register.html")

def user_login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)

        if user:
            try:
                registration_status = Registration.objects.get(user=user).status
            except Registration.DoesNotExist:
                registration_status = None
            try:
                owner_status = Owner.objects.get(user=user).status
            except Owner.DoesNotExist:
                owner_status = None

            if registration_status == 1 or owner_status == 1:
                if user.is_staff:
                    messages.error(request, "Invalid User")
                    return redirect('user_login')
                else:
                    login(request, user)
                    messages.success(request, "User Login Successful")
                    return redirect('/')
            else:
                messages.error(request, "User is not active. Please contact support team to become active.")
                return redirect('user_login')
        else:
            messages.error(request, "Invalid User")
            return redirect('user_login')
    return render(request, "user_login.html")

def logout_user(request):
    logout(request)
    messages.success(request, "logout Successful")
    return redirect('/')

def admin_login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        try:
            if user.is_staff:
                login(request, user)
                messages.success(request, "Login Successful")
                return redirect('/')
            else:
                messages.success(request, "Invalid User")
                return redirect('admin_login')
        except:
            messages.success(request, "Invalid User")
            return redirect('admin_login')
    return render(request, "admin_login.html")

@login_required(login_url='/admin_login/')
def user_table(request):
    data = Registration.objects.all()
    return render(request, "user_table.html", locals())

@login_required(login_url='/admin_login/')
def owner_table(request):
    data = Owner.objects.all()
    return render(request, "owner_table.html", locals())

@login_required(login_url='/user_login/')
def add_Apartment(request):
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        furnish = request.POST['furnish']
        atype = request.POST['atype']
        ebill = request.POST['ebill']
        extra = request.POST['extra']
        gender = request.POST['gender']
        rent = request.POST['rent']
        pic1 = request.FILES['pic1']
        pic2 = request.FILES['pic2']
        pic3 = request.FILES['pic3']
        pic4 = request.FILES['pic4']

        # Create Apartment
        owner = Owner.objects.get(user=request.user)
        Apartment.objects.create(owner=owner, name=name, address=address, city=city,
                                        state=state, furnish=furnish, atype=atype, ebill=ebill, extra=extra,
                                 gender=gender, rent=rent, pic1=pic1, pic2=pic2, pic3=pic3, pic4=pic4)

        messages.success(request, "Apartment added successful.")
        return redirect('apartment_table')
    return render(request, "add_Apartment.html")

@login_required(login_url='/user_login/')
def apartment_table(request):
    user = Owner.objects.get(user=request.user)
    data = Apartment.objects.filter(owner=user)
    return render(request, "apartment_table.html", locals())

@login_required(login_url='/user_login/')
def apartment_admtable(request):

    data = Apartment.objects.all()
    return render(request, "apartment_admtable.html", locals())

@login_required(login_url='/user_login/')
def user_profile(request):
    data = Registration.objects.get(user=request.user)
    return render(request, "user_profile.html", locals())

@login_required(login_url='/user_login/')
def owner_profile(request):
    data = Owner.objects.get(user=request.user)
    return render(request, "owner_profile.html", locals())

@login_required(login_url='/user_login/')
def user_change(request):
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(c)
            u.save()
            messages.success(request, "Password changed successfully")
            return redirect('user_login')
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('user_change_password')

    return render(request, 'user_change.html')

@login_required(login_url='/user_login/')
def send_feedback(request):
    if request.method == "POST":
        description = request.POST['description']
        register = Registration.objects.get(user=request.user)
        Feedback.objects.create(description=description, register=register)
        messages.success(request, "Apartment added successful.")
        return redirect('send_feedback')
    return render(request, "send_feedback.html")

@login_required(login_url='/user_login/')
def owner_apartment_detail(request, aid):
    data = Apartment.objects.get(id=aid)
    userList = Payment.objects.filter(apart=data)
    return render(request, "owner_apartment_detail.html", locals())

@login_required(login_url='/user_login/')
def user_apartment_detail(request, aid):
    data = Apartment.objects.get(id=aid)
    existing_payment = Payment.objects.filter(apart=data, register__user=request.user).exists()
    if request.method == "POST":
        cardno = request.POST['cardno']
        nameoncard = request.POST['nameoncard']
        amount = request.POST['amount']

        register = Registration.objects.get(user=request.user)
        if existing_payment:
            messages.warning(request, "You have already made a payment for this apartment.")
            return redirect(reverse('user_apartment_detail', kwargs={'aid': aid}))

        Payment.objects.create(apart=data, cardno=cardno, nameoncard=nameoncard, amount=amount, register=register)
        messages.success(request, "Payment successfully.")
        return redirect('/')

    return render(request, "user_apartment_detail.html", locals())

def change_apartment_status(request, pid):
    data = Apartment.objects.get(id=pid)
    status = int(request.GET.get('action', 1))
    if status in dict(STATUS):
        data.status = status
        data.save()
        messages.success(request, "Apartment Status Changed")
    else:
        messages.error(request, "Invalid Apartment Status")
    return redirect('owner_apartment_detail', aid=pid)

@login_required(login_url='/user_login/')
def user_booking_apartment(request):
    register = Registration.objects.get(user=request.user)
    data = Payment.objects.filter(register=register)
    d = {'data': data}
    return render(request, "user_booking_apartment.html", d)

@login_required(login_url='/user_login/')
def user_booking_list(request):
    owner = Owner.objects.get(user=request.user)
    data = Payment.objects.filter(apart__owner=owner)
    d = {'data': data}
    return render(request, "user_booking_list.html", d)

@login_required(login_url='/user_login/')
def user_payment(request):
    owner = Owner.objects.get(user=request.user)
    data = Payment.objects.filter(apart__owner=owner)
    d = {'data': data}
    return render(request, "user_payment.html", d)

def change_payment_status(request, pid):
    try:
        payment = Payment.objects.get(id=pid)
        if payment.status == "Booked":
            payment.status = "Canceled"
            messages.success(request, "Your Booking Apartment is Canceled")
        elif payment.status == "Canceled":
            payment.status = "Booked"
            messages.success(request, "Your Booking Apartment is Confirmed")
        payment.save()
    except Payment.DoesNotExist:
        messages.error(request, "Invalid Payment Status")
    return redirect('/')

def owner_detail(request, pid):
    data = Owner.objects.get(id=pid)
    return render(request, 'owner_detail.html', locals())

def user_detail(request, pid):
    data = Registration.objects.get(id=pid)
    return render(request, 'user_detail.html', locals())

def change_owner_status(request, pid):
    data = Owner.objects.get(id=pid)
    status = int(request.GET.get('action', 2))
    if status in dict(STATUS):
        data.status = status
        data.save()
        messages.success(request, "Owner Status Changed")
    else:
        messages.error(request, "Invalid Owner Status")
    return redirect('owner_detail', pid=pid)

def change_user_status(request, pid):
    data = Registration.objects.get(id=pid)
    status = int(request.GET.get('action', 1))
    if status in dict(STATUS):
        data.status = status
        data.save()
        messages.success(request, "User Status Changed")
    else:
        messages.error(request, "Invalid User Status")
    return redirect('user_detail', pid=pid)

def apartment_delete(request, pid):
    data = Apartment.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect('apartment_table')

def feedback(request):
    data = Feedback.objects.all()
    d = {'data': data}
    return render(request, 'view_feedback.html', d)

def delete_feed(request, pid):
    data = Feedback.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect('feedback')

@login_required(login_url='/admin_login/')
def admin_change_password(request):
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(c)
            u.save()
            messages.success(request, "Password changed successfully")
            return redirect('/')
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('admin_change_password')

    return render(request, 'admin_change_password.html')

def apartment_search(request):
    if request.method == 'POST':
        atype = request.POST.get('atype', 'All')
        gender = request.POST.get('gender', 'All')
        furnish = request.POST.get('furnish', 'All')

        # Perform your search based on the form inputs
        # Customize this part based on your model and search criteria
        queryset = Apartment.objects.all()

        if atype != 'All':
            queryset = queryset.filter(atype=atype)
        if gender != 'All':
            queryset = queryset.filter(gender=gender)
        if furnish != 'All':
            queryset = queryset.filter(furnish=furnish)

        # Pass the search results to the template
        context = {'apartments': queryset}
        return render(request, 'apartment_search.html', context)

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        sec_question = request.POST.get('sec_question')
        answer = request.POST.get('answer')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if email:
            try:
                user = User.objects.get(username=email)

                # Check if the user is a registered user
                registration = Registration.objects.filter(user=user).first()
                if registration and registration.sec_question == sec_question and registration.answer == answer:
                    if new_password == confirm_password:
                        user.set_password(new_password)
                        user.save()
                        messages.success(request, 'Password reset successfully. You can now log in with the new password.')
                        return redirect('user_login')
                    else:
                        messages.error(request, 'New password and confirm password do not match.')
                else:
                    # Check if the user is an owner
                    owner = Owner.objects.filter(user=user).first()
                    if owner and owner.sec_question == sec_question and owner.answer == answer:
                        if new_password == confirm_password:
                            user.set_password(new_password)
                            user.save()
                            messages.success(request, 'Password reset successfully. You can now log in with the new password.')
                            return redirect('user_login')
                        else:
                            messages.error(request, 'New password and confirm password do not match.')
                    else:
                        messages.error(request, 'Invalid security question or answer for the provided email address.')
            except User.DoesNotExist:
                messages.error(request, 'No user found with the provided email address.')

    return render(request, 'forgot_password.html')