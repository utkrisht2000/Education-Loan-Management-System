from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from .models import Application, Notice, Detail
from django.views.generic import UpdateView

def college(request):
    notice = Notice.objects.all()
    return render(request, "college.html", {'notice':notice})

def notice(request, myid):
    notices = Notice.objects.filter(id=myid).first()
    details = Detail.objects.filter(title=notices)
    return render(request, "notice.html", {'details':details})

def application_form(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    hide = Application.objects.filter(user=request.user)
    if request.method=="POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            application.user = request.user
            application.save()
            return render(request, "application_form.html")
    else:
        form=ApplicationForm()
    return render(request, "application_form.html", { 'form':form,'hide':hide})

def edit_application(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    try:
        application = request.user.application
    except Application.DoesNotExist:
        application = Application(user=request.user)
    if request.method=="POST":
        form = ApplicationForm(data=request.POST, files=request.FILES, instance=application)
        if form.is_valid():
            form.save()
            alert = True
            return render(request, "edit_application.html", {'alert':alert})
    else:
        form=ApplicationForm(instance=application)
    return render(request, "edit_application.html", {'form':form})

def status(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    application = Application.objects.get(user=request.user) 
    return render(request, "status.html", {'application':application})

def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":   
            username = request.POST['username']
            email = request.POST['email']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            
            if password1 != password2:
                messages.error(request, "Passwords do not match.")
                return redirect('/register')
            
            user = User.objects.create_user(username, email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return render(request, 'login.html')   
    return render(request, "register.html")

def loggedin(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return redirect("/")
            else:
                messages.error(request, "Invalid Credentials")
            return render(request, 'college.html')   
    return render(request, "login.html")

def loggedout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')


def handle_admin(request):
    if not request.user.is_superuser:
        return redirect("/login")
    users = User.objects.all().count
    approve = Application.objects.filter(GOV_Status='Approved').count
    reject = Application.objects.filter(GOV_Status='Rejected').count
    pending = Application.objects.filter(GOV_Status='Pending').count
    return render(request, "handle_admin.html", {'approve':approve, 'reject':reject, 'pending':pending, 'users':users})

def users(request):
    if not request.user.is_superuser:
        return redirect("/login")
    allUsers = Application.objects.all()
    return render(request, "users.html", {'allUsers':allUsers})

def student_application(request, myid):
    if not request.user.is_superuser:
        return redirect("/login")
    application = Application.objects.filter(id=myid)
    return render(request, "student_application.html", {'application':application[0]})

class UpdatePostView(UpdateView):
    model = Application
    template_name = 'application_status.html'
    fields = ( 'bank', 'message', 'GOV_Status', 'GOV_Bank', 'GOV_Capital_Amount', 'GOV_Interest',
        	'SBI_Status', 'SBI_Capital_Amount', 'SBI_Interest', 
    		'PNB_Status', 'PNB_Capital_Amount', 'PNB_Interest',
    		 'Axis_Status', 'Axis_Capital_Amount', 'Axis_Interest',
    		  'HDFC_Status', 'HDFC_Capital_Amount', 'HDFC_Interest',
    		  'BOB_Status', 'BOB_Capital_Amount', 'BOB_Interest',
    		  'Canara_Status', 'Canara_Capital_Amount', 'Canara_Interest',
    		  'ICICI_Status', 'ICICI_Capital_Amount', 'ICICI_Interest',
    		  'Kotak_Status', 'Kotak_Capital_Amount', 'Kotak_Interest',
    		  'DCB_Status', 'DCB_Capital_Amount', 'DCB_Interest',
    		  'IDBI_Status', 'IDBI_Capital_Amount', 'IDBI_Interest',
    		  'Andhra_Status', 'Andhra_Capital_Amount', 'Andhra_Interest',
    		  'Federal_Status', 'Federal_Capital_Amount', 'Federal_Interest',
    		  'IndusInd_Status', 'IndusInd_Capital_Amount', 'IndusInd_Interest',
    		  'Karnataka_Status', 'Karnataka_Capital_Amount', 'Karnataka_Interest',
    		  'City_Status', 'City_Capital_Amount', 'City_Interest',
    		  'UCO_Status', 'UCO_Capital_Amount', 'UCO_Interest',
    		  'KVB_Status', 'KVB_Capital_Amount', 'KVB_Interest',
    		  'RBL_Status', 'RBL_Capital_Amount', 'RBL_Interest',
    		  'YES_Status', 'YES_Capital_Amount', 'YES_Interest',
    		  'Union_Status', 'Union_Capital_Amount', 'Union_Interest',
    		  'Auxillo_Status', 'Auxillo_Capital_Amount', 'Auxillo_Interest',
    		  'Avanse_Status', 'Avanse_Capital_Amount', 'Avanse_Interest',
    		  'Gyan_Status', 'Gyan_Capital_Amount', 'Gyan_Interest',
    		  'Student_Status', 'Student_Capital_Amount', 'Student_Interest',)

def approved_applications(request):
    if not request.user.is_superuser:
        return redirect("/login")
    approved = Application.objects.filter(GOV_Status="Approved")
    return render(request, "approved_applications.html", {'approved':approved})

def pending_applications(request):
    if not request.user.is_superuser:
        return redirect("/login")
    pending = Application.objects.filter(GOV_Status="Pending")
    return render(request, "pending_applications.html", {'pending':pending})

def rejected_applications(request):
    if not request.user.is_superuser:
        return redirect("/login")
    rejected = Application.objects.filter(GOV_Status="Rejected")
    return render(request, "rejected_applications.html", {'rejected':rejected})
    
