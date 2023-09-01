from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import signupform,EdirUserProfileForm,EdirAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth.models import Group


# new user creation 
def sign_up(request):
    if(request.method == 'POST'):
        # create an obj
        fm=signupform(request.POST)
        
        # validating the user 
        if fm.is_valid():
            # sending message to sign_up.html   
            messages.success(request,"Account created succesfully!!!!!!!")
            user=fm.save()
            mygroup=Group.objects.get(name='User')
            user.groups.add(mygroup)
    # get request 
    else: 
        fm=signupform()
    return render(request,'sign_up.html',{'form':fm})

# uset verification 
def sign_in(request):
    if not request.user.is_authenticated:
        if(request.method == 'POST'):
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                # below request is very necessary in argument 
                # pass uname and upass without quotes
                user=authenticate(request,username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"sign_in succesfully!!!!!!!")

                    # fm.save()
                    return HttpResponseRedirect('/auth/profile/')
                    # fm.save()

                print("Hello outside")
                # fm.save()
                # messages.success(request,"sign_in succesfully!!!!!!!")
        else: 
            fm=AuthenticationForm()
        return render(request,'sign_in.html',{'form':fm})
    else:
        return HttpResponseRedirect('/auth/profile/')
def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/auth/sign_in/') 
def change_pass(request):
    if request.user.is_authenticated:
        if(request.method == 'POST'):
            fm=PasswordChangeForm(user=request.user,data=request.POST)    
            if fm.is_valid():
                fm.save()
                # as password is reset the session id is updated .....so to get session id restored in same profile ...we use 
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password is updated successfully!!!!!')
                return HttpResponseRedirect('/auth/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)    
        return render(request,'change_pass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/auth/sign_in/')
def profile(request):
    # access this page only when user is only logged in(checking by session) 
    if request.user.is_authenticated:
        if request.method=='POST':
            # form = ProfileUpdateForm(instance=request.user , data=request.POST )
            if request.user.is_superuser==True:
                fm=EdirAdminProfileForm(request.POST,instance=request.user)
                users=User.objects.all()
            else:
                users=None
                fm=EdirUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,'Profile Updated Successfully')
                fm.save()
        # when user loged in ....then we can access username and its attributes by session id 
        # return render(request,'profile.html',{'name':request.user,'form':fm} )
        else:
            if request.user.is_superuser==True:
                fm=EdirAdminProfileForm(instance=request.user)
                users=User.objects.all()
            else:
                users=None
                fm=EdirUserProfileForm(instance=request.user)
        return render(request,'profile.html',{'name':request.user.username,'form':fm,'users':users} )
    else:
        return HttpResponseRedirect('/auth/sign_in/')
def userdetail(request,id):
    if request.user.is_authenticated:
        pid=User.objects.get(pk=id)
        fm=EdirAdminProfileForm(instance=pid)
        return render(request,'userdetail.html',{'form':fm})
    else:
        return HttpResponseRedirect('/auth/sign_in/')
    
    # if not (request.user.is_authenticated or request.user.is_staff ):
    #     raise Http404("You are Not Authorized to view this Page")
    #    if request.user.is_superuser!= True :
    #        raise Http404("You Are Not authorized to View This Page")
    #    elif request.user.is_superuser != False:
    #         print('hello admin')
    #            pass
    #    if request.user.is_superuser==False:
    #        raise Http404("You Are Not authorized to View This Page")

