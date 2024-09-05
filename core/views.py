from django.shortcuts import render, redirect
from users.models import Member
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required
# from django.contrib.auth.models import User
# from .forms import SignUpForm
# # from .models import Profile, Member
# from django.contrib.auth import logout

# from django.contrib.auth.forms import UserCreationForm
# from django.core.mail import send_mail

# Create your views here.


def base(request):
    return render(request, 'core/base.html')




# Create sample members
# Member.objects.create(name="John Doe", details="A friendly member.", image_url="http://example.com/john.jpg")
# Member.objects.create(name="Jane Smith", details="Loves hiking and outdoor activities.", image_url="http://example.com/jane.jpg")
# Add more members as needed

def home(request):
    members = Member.objects.all()
    print(f"Number of users: {members.count()}")  # Debug statement
    return render(request, 'core/home.html', {'members': members})


def contact(request):
    if request.method == 'POST':
        # Process the form data here
        # name = request.POST['name']
        # email = request.POST['email']
        # subject = request.POST['subject']
        # message = request.POST['message']
        pass  # Replace with your form handling logic

    return render(request, 'core/contact.html')




def about(request):
    return render(request, 'core/about.html')

def terms(request):
    return render(request, 'core/terms.html')

def privacy(request):
    return render(request, 'core/privacy.html')



# def chat(request):
#     return render(request, 'core/chat.html')

# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.core.mail import send_mail
# # from .models import Member

# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False  # Deactivate account until admin approval
#             user.save()
#             Member.objects.create(user=user)
#             # Notify admin via email
#             send_mail(
#                 'New User Signup',
#                 f'A new user has signed up: {user.username}',
#                 'your_email@example.com',
#                 ['admin@example.com'],
#                 fail_silently=False,
#             )
#             return redirect('signup_pending')
#     else:
#         form = UserCreationForm()
#     return render(request, 'core/registration/signup.html', {'form': form})

# def signup_pending(request):
#     return render(request, 'core/registration/signup_pending.html')

 

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return redirect('base')
#             else:
#                 return render(request, 'core/registration/account_inactive.html')
#         else:
#             return render(request, 'core/registration/login.html', {'error': 'Invalid username or password'})
#     else:
#         return render(request, 'core/registration/login.html')

# @staff_member_required
# def approve_users(request):
#     pending_users = User.objects.filter(is_active=False)
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         user = User.objects.get(id=user_id)
#         user.is_active = True
#         user.save()
#         return redirect('approve_users')
#     return render(request, 'core/registration/approve_users.html', {'pending_users': pending_users})

# @login_required
# def profile_view(request):
#     return render(request, 'profile.html', {'user': request.user})

# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('base')

# @staff_member_required
# def approve_users(request):
#     if request.method == 'POST':
#         member_id = request.POST.get('member_id')
#         member = Member.objects.get(pk=member_id)
#         member.approved = True
#         member.save()
#         # Optionally send email to user notifying approval
#         # Redirect or show success message

#     pending_members = Member.objects.filter(approved=False)
#     return render(request, 'core/registration/approve_users.html', {'pending_members': pending_members})
