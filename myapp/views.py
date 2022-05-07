
import email
from multiprocessing import context
from urllib.request import Request
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from random import *
from django.core.mail import send_mail 

# Create your views here.
def home(request):
   
    if 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        all_cha=Chairman.objects.all()
        all_member=Member.objects.all()
        all_wat=Watchman.objects.all()
        member_count=Member.objects.all().count()
        notic_count=Notice.objects.all().count()
        com_count=Complain.objects.all().count()
        
        context={
            'uid':uid,
            'cid':cid,
            'all_member':all_member,
            'member_count':member_count,
            'all_cha':all_cha,
            'all_wat':all_wat,
            'notic_count':notic_count,
            'com_count':com_count,
        }
        return render(request,"myapp/index.html",context)
    elif 'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        mid=Member.objects.get(user_id=uid)
        all_cha=Chairman.objects.all()
        all_wat=Watchman.objects.all()
        all_member=Member.objects.all()
        member_count=Member.objects.all().count()
        notic_count=Notice.objects.all().count()
        com_count=Complain.objects.all().count()
         
        context={
            'uid':uid,
            'mid':mid,
            'all_member':all_member,
            'member_count':member_count,
            'all_cha':all_cha,
            'all_wat':all_wat,
            'notic_count':notic_count,
            'com_count':com_count,
        }
        return render(request,"myapp/index.html",context)
    elif 'w_email' in request.session:
        uid=User.objects.get(email=request.session['w_email'])
        wid=Watchman.objects.get(user_id=uid)
        all_cha=Chairman.objects.all()
        all_member=Member.objects.all()
        all_wat=Watchman.objects.all() 
        member_count=Member.objects.all().count()
        notic_count=Notice.objects.all().count()
        com_count=Complain.objects.all().count()
        
        context={
            'uid':uid,
            'wid':wid,
            'all_member':all_member,
            'member_count':member_count,
            'all_cha':all_cha,
            'all_wat':all_wat,
            'notic_count':notic_count,
            'com_count':com_count,
        }
        return render(request,"myapp/index.html",context)
    else:
        all_member=Member.objects.all()
        all_cha=Chairman.objects.all()
        member_count=Member.objects.all().count()
        all_wat=Watchman.objects.all()
        notic_count=Notice.objects.all().count()
        com_count=Complain.objects.all().count()
        
        context={
            'all_member':all_member,
            'member_count':member_count,
            'all_cha':all_cha,
            'all_wat':all_wat,
            'notic_count':notic_count,
            'com_count':com_count,

        }
        return render(request,"myapp/index.html",context)
        

def login(request):
    if "c_email" in request.session:
        return redirect("home")
    else:
        if request.POST:
            email = request.POST['email']
            password=request.POST['password']
            role=request.POST['role']
            uid=User.objects.get(email=email)
            
            if uid.password == password:
            
                if uid.role=='Chairman':
                    cid=Chairman.objects.get(user_id=uid)
                    request.session['c_email']= uid.email
                    context={
                        'uid':uid,
                        'cid':cid,
                    }
                    return render(request,"myapp/index.html",context)
                if uid.role=='Member':
                    mid=Member.objects.get(user_id=uid)
                    request.session['m_email']= uid.email
                    context= {
                        'uid':uid,
                        'mid':mid,
                    }
                    return render(request,"myapp/index.html",context)
                if uid.role=='Watchman':
                    wid=Watchman.objects.get(user_id=uid)
                    request.session['w_email']= uid.email
                    context={
                        'uid':uid,
                        'wid':wid,
                    }
                    return render(request,"myapp/index.html",context)
                else:
                    print("error")
                    return render(request,"myapp/login.html")
                

            else: 
                
                return render(request,"myapp/login.html")
        else:
        
            return render(request,"myapp/login.html")

def registration(request):
    if request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        contact=request.POST['contact']
        dob=request.POST['dob']
        email=request.POST['email']
        gender=request.POST['gender']
        
        uid=User.objects.create(email=email, password="123456", first_name=fname, last_name=lname,role="Watchman" )
        wid=Watchman.objects.create(user_id=uid, first_name=fname, last_name=lname, dob=dob, gender=gender, contact=contact, email= email)
        print("successfull")
        return render(request,"myapp/login.html")
    
    else:
        return render(request,"myapp/registration.html")

def logout(request):
    if 'c_email' in request.session:
        del request.session['c_email']
        return redirect("login")
    if 'm_email' in request.session:
        del request.session['m_email']
        return redirect("login")
    if 'w_email' in request.session:
        del request.session['w_email']
        return redirect("login")
    else:
        return redirect("login")

def add_member(request):
    if request.POST:
        uid=User.objects.get(email=request.session["c_email"])
        cid=Chairman.objects.get(user_id=uid)
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        flat_number=request.POST['flat_number']
        email=request.POST['email']
        dob=request.POST['dob']
        gender=request.POST['gender']
        contact=request.POST['contact']
        job_profession=request.POST['job_profession']
        job_address=request.POST['job_address']
        vehical_type=request.POST['vehical_type']
        vehical_details=request.POST['vehical_details']
        pic=request.FILES['pic']
        

        mid=Member.objects.create(user_id=uid,c_id=cid,first_name=f_name,last_name=l_name,flat_no=flat_number,email=email,dob=dob,gender=gender,contact=contact,job_profession=job_profession,job_address=job_address,vehical_type=vehical_type,vehical_details=vehical_details,pic=pic)
        uid=User.objects.create(first_name=f_name, last_name=l_name, email=email, password="123456",role="Member" )
        if 'c_email' in request.session:
            uid=User.objects.get(email=request.session['c_email'])
            cid=Chairman.objects.get(user_id=uid)
            all=Chairman.objects.all()
            context={
             'all':all,
             'uid':uid,
             'cid':cid
            }
            return render(request,'myapp/add-member.html',context)
        return render(request,'myapp/add-member.html')
    else:
        if 'c_email' in request.session:
            uid=User.objects.get(email=request.session['c_email'])
            cid=Chairman.objects.get(user_id=uid)
            all=Chairman.objects.all()
            context={
             'all':all,
             'uid':uid,
             'cid':cid
            }
            return render(request,"myapp/add-member.html",context)

def my_profile(request):
    if 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        all=Chairman.objects.get(user_id=uid)

        context={
                        'uid':uid,
                        'cid':cid,
                        'all':all
                    }
        return render(request,'myapp/my-profile.html',context)

    if 'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        mid=Member.objects.get(user_id=uid)
        all=Member.objects.get(user_id=uid)
        context= {
                        'uid':uid,
                        'mid':mid,
                        'all':all

                    }
        return render(request,'myapp/my-profile.html',context)
    if 'w_email' in request.session:
        uid=User.objects.get(email=request.session['w_email'])
        wid=Watchman.objects.get(user_id=uid)
        all=Watchman.objects.get(user_id=uid)
        context={
                        'uid':uid,
                        'wid':wid,
                        'all':all
                    }
        return render(request,'myapp/my-profile.html',context)
        
   


    return render(request,'myapp/my-profile.html')

def update_profile(request):
        uid=User.objects.get(email=request.session["c_email"])
        cid=Chairman.objects.get(user_id=uid)
        all=Chairman.objects.all()
        
        
        # pid=Chairman.objects.get(id=request.POST['id'])
        if request.POST:
               
            cid.first_name =request.POST['f_name']
            cid.last_name=request.POST['l_name']
            cid.flat_no=request.POST['flat_number']
            cid.email=request.POST['email']
            cid.dob=request.POST['dob']
            cid.gender=request.POST['gender']
            cid.contact=request.POST['contact']
            cid.job_profession=request.POST['job_profession']
            cid.job_address=request.POST['job_address']
            cid.vehical_type=request.POST['vehical_type']
            cid.vehical_details=request.POST['vehical_details']
            cid.save()
            return redirect("my-profile")
        else:
            return render(request,'myapp/my-profile.html')


def all_member(request):
    if 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        mall=Member.objects.all()

        context={
                        'uid':uid,
                        'cid':cid,
                        'mall':mall,
                    }
        return render(request,'myapp/all-member.html',context)

    elif 'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        mid=Member.objects.get(user_id=uid)
        mall=Member.objects.all()
        context= {
                        'uid':uid,
                        'mid':mid,
                        'mall':mall,

                    }
        return render(request,'myapp/all-member.html',context)
    elif 'w_email' in request.session:
        uid=User.objects.get(email=request.session['w_email'])
        wid=Watchman.objects.get(user_id=uid)
        mall=Member.objects.all()
        context={
                        'uid':uid,
                        'wid':wid,
                        'mall':mall,
                    }

        return render(request,'myapp/all-member.html',context)


def maintenance(request):
    if 'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        mid=Member.objects.get(user_id=uid)
        mall=Member.objects.all()
        context= {
                        'uid':uid,
                        'mid':mid,
                        'mall':mall,

                    }
        return render(request,'myapp/maintenance.html',context)
    elif 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        mall=Member.objects.all()
        context= {
                        'uid':uid,
                        'cid':cid,
                        'mall':mall,

                    }
        return render(request,'myapp/maintenance.html',context)
    elif 'w_email' in request.session:
        uid=User.objects.get(email=request.session['w_email'])
        wid=Watchman.objects.get(user_id=uid)
        return render(request,'myapp/maintenance.html')
        
        
        
        

def all_event(request):
    if request.POST:
        event_title = request.POST['event_title']
        pic=request.FILES['pic']
        dob=request.POST['dob']
        event_dis=request.POST['event_dis']
        eid=Event.objects.create(event_title=event_title, pic=pic, dob=dob, event_dis=event_dis)
        if 'c_email' in request.session:
            uid=User.objects.get(email=request.session["c_email"])
            cid=Chairman.objects.get(user_id=uid)
            eid=Event.objects.all()
            context={
                'uid':uid,
                'cid':cid,
                'eid':eid

            }
            return render(request,'myapp/add-event.html',context)
    uid=User.objects.get(email=request.session["c_email"])
    cid=Chairman.objects.get(user_id=uid)
    eid=Event.objects.all()
    context={
                'uid':uid,
                'cid':cid,
                'eid':eid

            }
    return render(request,'myapp/add-event.html',context)
        
       

        
    return render(request,'myapp/add-event.html')

def view_event(request):
    if 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        all=Event.objects.all()

        context={
                        'uid':uid,
                        'cid':cid,
                        'all':all
                    }
        return render(request,'myapp/event_list.html',context)

    if 'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        mid=Member.objects.get(user_id=uid)
        all=Event.objects.all()
        context= {
                        'uid':uid,
                        'mid':mid,
                        'all':all

                    }
        return render(request,'myapp/event_list.html',context)
    if 'w_email' in request.session:
        uid=User.objects.get(email=request.session['w_email'])
        wid=Watchman.objects.get(user_id=uid)
        all=Event.objects.all()
        context={
                        'uid':uid,
                        'wid':wid,
                        'all':all
                    }

        return render(request,'myapp/event_list.html',context)
    
    return render(request,"myapp/event_list.html")


def add_complain(request):
    if request.POST:
        com_title=request.POST['com_title']
        com_dis=request.POST['com_dis']
        coid=Complain.objects.create(com_title=com_title,com_dis=com_dis)
       
        if 'm_email' in request.session:
            uid=User.objects.get(email=request.session['m_email'])
            mid=Member.objects.get(user_id=uid)
            coid=Complain.objects.all()
            context={
                'uid':uid,
                'mid':mid,
                'coid':coid,

            }
            return render(request,"myapp/add-complain.html",context)
        else:
            return render(request,"myapp/add-complain.html")
    uid=User.objects.get(email=request.session['m_email'])
    mid=Member.objects.get(user_id=uid)
    coid=Complain.objects.all()
    context={
            'uid':uid,
            'mid':mid,
            'coid':coid,

            }
        
    return render(request,"myapp/add-complain.html",context)


def list_complain(request):
    if 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        all=Complain.objects.all()

        context={
                        'uid':uid,
                        'cid':cid,
                        'all':all
                    }
        return render(request,'myapp/complain_list.html',context)

    if 'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        mid=Member.objects.get(user_id=uid)
        all=Complain.objects.all()
        context= {
                        'uid':uid,
                        'mid':mid,
                        'all':all

                    }
        return render(request,'myapp/complain_list.html',context)
    if 'w_email' in request.session:
        uid=User.objects.get(email=request.session['w_email'])
        wid=Watchman.objects.get(user_id=uid)
        all=Complain.objects.all()
        context={
                        'uid':uid,
                        'wid':wid,
                        'all':all
                    }

        return render(request,'myapp/complain_list.html',context)
    return render(request,"myapp/complain_list.html")

def add_notice(request):
    if request.POST:
        notice_title=request.POST['notice_title'] 
        dob=request.POST['dob']
        notice_dis=request.POST['notice_dis']
        nid=Notice.objects.create(notice_title=notice_title,dob=dob,notice_dis=notice_dis)
        
        if "c_email" in request.session:
            uid=User.objects.get(email=request.session['c_email'])
            cid=Chairman.objects.get(user_id=uid)
            nid=Notice.objects.all()

            context={
                        'uid':uid,
                        'cid':cid,
                        'nid':nid
                    }
            return render(request,'myapp/add-notice.html',context)
        else:
            return render(request,'myapp/add-notice.html')
    uid=User.objects.get(email=request.session['c_email'])
    cid=Chairman.objects.get(user_id=uid)
    nid=Notice.objects.all()
    context={
                    'uid':uid,
                    'cid':cid,
                    'nid':nid
                }
    return render(request,'myapp/add-notice.html',context)


def notice_board(request):
    if 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        nall=Notice.objects.all()

        context={
                        'uid':uid,
                        'cid':cid,
                        'nall':nall
                    }
        return render(request,'myapp/notice-board.html',context)

    if 'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        mid=Member.objects.get(user_id=uid)
        nall=Notice.objects.all()
        context= {
                        'uid':uid,
                        'mid':mid,
                        'nall':nall

                    }
        return render(request,'myapp/notice-board.html',context)
    if 'w_email' in request.session:
        uid=User.objects.get(email=request.session['w_email'])
        wid=Watchman.objects.get(user_id=uid)
        nall=Notice.objects.all()
        context={
                        'uid':uid,
                        'wid':wid,
                        'nall':nall
                    }

        return render(request,'myapp/notice-board.html',context)
    return render(request,"myapp/notice-board.html")


def add_visitors(request):
    if request.POST:
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        flat_number=request.POST['flat_number']
        email=request.POST['email']
        contact=request.POST['contact']
        vid=Visitors.objects.create(first_name=f_name,last_name=l_name,flat_no=flat_number,email=email,contact=contact)
        
        if 'w_email' in request.session:
            uid=User.objects.get(email=request.session['w_email'])
            wid=Watchman.objects.get(user_id=uid)
            vid=Visitors.objects.all()
            context={
                'uid':uid,
                'wid':wid,
                'vid':vid
            }
            return render(request,"myapp/add-visitors.html",context)
        else:
            return render(request,"myapp/add-visitors.html",context)
    
    uid=User.objects.get(email=request.session['w_email'])
    wid=Watchman.objects.get(user_id=uid)
    vid=Visitors.objects.all()
    context={
                'uid':uid,
                'wid':wid,
                'vid':vid
            }       
            
            
    return render(request,"myapp/add-visitors.html",context)

def all_visitors(request):
    if 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        vall=Visitors.objects.all()

        context={
                        'uid':uid,
                        'cid':cid,
                        'vall':vall
                    }
        return render(request,'myapp/all-visitors.html',context)

    if 'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        mid=Member.objects.get(user_id=uid)
        vall=Visitors.objects.all()
        context= {
                        'uid':uid,
                        'mid':mid,
                        'vall':vall

                    }
        return render(request,'myapp/all-visitors.html',context)
    if 'w_email' in request.session:
        uid=User.objects.get(email=request.session['w_email'])
        wid=Watchman.objects.get(user_id=uid)
        vall=Visitors.objects.all()
        context={
                        'uid':uid,
                        'wid':wid,
                        'vall':vall
                    }

        return render(request,'myapp/all-visitors.html',context)

    return render(request,"myapp/all-visitors.html")

def add_photos(request):
    if request.POST:
        pic=request.FILES['pic']
        dob=request.POST['dob']
        p_name=request.POST['p_name']
        pid=photos.objects.create(pic=pic,dob=dob,photo_name=p_name)
        if 'c_email' in request.session:
            uid=User.objects.get(email=request.session['c_email'])
            cid=Chairman.objects.get(user_id=uid)
            pid=photos.objects.all()
            context={
                'uid':uid,
                'cid':cid,
                'pid':pid
            }
            return render(request,"myapp/add-photos.html",context)
        
    uid=User.objects.get(email=request.session['c_email'])
    cid=Chairman.objects.get(user_id=uid)
    mid=Member.objects.all()
    pid=photos.objects.all()
    context={
                'uid':uid,
                'cid':cid,
                'mid':mid,
                'pid':pid
            }
            
    return render(request,"myapp/add-photos.html",context)

def photo_gallery(request):
    if 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        pall=photos.objects.all()

        context={
                        'uid':uid,
                        'cid':cid,
                        'pall':pall
                    }
        return render(request,'myapp/photo_gallery.html',context)

    if 'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        mid=Member.objects.get(user_id=uid)
        pall=photos.objects.all()
        context= {
                        'uid':uid,
                        'mid':mid,
                        'pall':pall

                    }
        return render(request,'myapp/photo_gallery.html',context)
    if 'w_email' in request.session:
        uid=User.objects.get(email=request.session['w_email'])
        wid=Watchman.objects.get(user_id=uid)
        pall=photos.objects.all()
        context={
                        'uid':uid,
                        'wid':wid,
                        'pall':pall
                    }

        return render(request,'myapp/photo_gallery.html',context)

    
    return render(request,"myapp/photo_gallery.html")

def add_video(request):
    if request.POST:
        video=request.FILES['video']
        dob=request.POST['dob']
        video_name=request.POST['video_name']
        vsid=Video.objects.create(video=video, dob=dob, video_name=video_name)
        
        if 'c_email' in request.session:
            uid=User.objects.get(email=request.session['c_email'])
            cid=Chairman.objects.get(user_id=uid)
            vsid=Video.objects.all()
            context={
                'uid':uid,
                'cid':cid,
                'vsid':vsid
            }
            return render(request,"myapp/add-video.html",context)
    uid=User.objects.get(email=request.session['c_email'])
    cid=Chairman.objects.get(user_id=uid)
    vsid=Video.objects.all()
    context={
                'uid':uid,
                'cid':cid,
                'vsid':vsid
            }
    return render(request,"myapp/add-video.html",context)

def video_gallery(request):
    
    if 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        vall=Video.objects.all()

        context={
                        'uid':uid,
                        'cid':cid,
                        'vall':vall
                    }
        return render(request,'myapp/video_gallery.html',context)

    if 'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        mid=Member.objects.get(user_id=uid)
        vall=Video.objects.all()
        context= {
                        'uid':uid,
                        'mid':mid,
                        'vall':vall

                    }
        return render(request,'myapp/video_gallery.html',context)
    return render(request,'myapp/video_gallery.html')

       
        

def add_suggestion(request):
    if request.POST:
        suggestion_title=request.POST['suggestion_title']
        suggestion_dis=request.POST['suggestion_dis']
        sid=Suggestion.objects.create(suggestion_title=suggestion_title,suggestion_dis=suggestion_dis)
        
        if 'm_email' in request.session:
            uid=User.objects.get(email=request.session['m_email'])
            mid=Member.objects.get(user_id=uid)
            sid=Suggestion.objects.all()
            context={
                'uid':uid,
                'mid':mid,
                'sid':sid
            }
            return render(request,"myapp/add-suggestions.html",context) 
    uid=User.objects.get(email=request.session['m_email'])
    mid=Member.objects.get(user_id=uid)
    sid=Suggestion.objects.all()
    context={
                'uid':uid,
                'mid':mid,
                'sid':sid
            }
        
        
    return render(request,"myapp/add-suggestions.html",context)

def view_suggestion(request):
    if 'c_email' in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=Chairman.objects.get(user_id=uid)
        sall=Suggestion.objects.all()

        context={
                        'uid':uid,
                        'cid':cid,
                        'sall':sall
                    }
        return render(request,'myapp/view_suggestion.html',context)

    if 'm_email' in request.session:
        uid=User.objects.get(email=request.session['m_email'])
        mid=Member.objects.get(user_id=uid)
        sall=Suggestion.objects.all()
        context= {
                        'uid':uid,
                        'mid':mid,
                        'sall':sall

                    }
        return render(request,'myapp/view_suggestion.html',context)
    if 'w_email' in request.session:
        uid=User.objects.get(email=request.session['w_email'])
        wid=Watchman.objects.get(user_id=uid)
        sall=Suggestion.objects.all()
        context={
                        'uid':uid,
                        'wid':wid,
                        'sall':sall
                    }

        return render(request,'myapp/view_suggestion.html',context)
    return render(request,'myapp/view_suggestion.html')

def forgot_password(request):
    if request.POST:
        email=request.POST['email']
        otp= randint(1111,9999)
        uid = User.objects.get(email=email)
        uid.otp=otp
        uid.save()
        send_mail("Forgot Password", "Your OTP is "+str(otp),"shethjainam17@gmail.com",[email])
        return render(request,'myapp/otp-verify.html',{'email' : email})
    else:
        return render(request,'myapp/forgot-password.html')
        
        


def otp_verify(request):
    if request.POST:
        email=request.POST['email']
        otp=request.POST['otp']
        new_password=request.POST['new_password']
        con_password=request.POST['con_password']
        uid= User.objects.get(email=email)
        
        if str(uid.otp)==otp and new_password==con_password:
            uid.password=new_password
            uid.save()
            return render(request,'myapp/login.html')
    return render(request,'myapp/forgot-password.html')


    
    
    
    
     
    
    
    
    
    
    
    
    
    
    
        
    
    
    



    


    