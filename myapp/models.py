from django.db import models
from datetime import timezone
import math

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email= models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    otp=models.IntegerField(default=459)
    pic=models.FileField(upload_to="media/images/", default="media/society.jpg")
    # is_active=models.BooleanField(default=True)
    # is_verfied=models.BooleanField(default=False)
    role=models.CharField(max_length=10)
    # created_at=models.DateTimeField(auto_now_add=True,blank=False)
    # updated_at=models.DateTimeField(auto_now=True,blank=False)
    

    def __str__(self):
        return self.email

class Chairman(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    flat_no=models.CharField(max_length=10,null=True)
    email=models.CharField(max_length=100,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.CharField(max_length=15,null=True)
    gender=models.CharField(max_length=100,null=True)
    # address=models.CharField(max_length=100,null=True)
    contact=models.CharField(max_length=10,null=True)
    job_profession=models.CharField(max_length=20,null=True)
    job_address=models.CharField(max_length=20,null=True)
    vehical_type=models.CharField(max_length=20,null=True)
    vehical_details=models.CharField(max_length=20,null=True)
    pic=models.FileField(upload_to="media/images/", default="media/images/society.jpg")
    
    def __str__(self):
        return self.first_name


class Member(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    c_id=models.ForeignKey(Chairman,on_delete=models.CASCADE)
    flat_no=models.CharField(max_length=10,null=True)
    email=models.CharField(max_length=100,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.CharField(max_length=15,null=True)
    gender=models.CharField(max_length=100,null=True)
    # address=models.CharField(max_length=100,null=True)
    contact=models.CharField(max_length=10,null=True)
    job_profession=models.CharField(max_length=20,null=True)
    job_address=models.CharField(max_length=20,null=True)
    vehical_type=models.CharField(max_length=20,null=True)
    vehical_details=models.CharField(max_length=20,null=True)
    pic=models.FileField(upload_to="media/images/", default="media/society.jpg")

    def __str__(self):
        return self.first_name


class Watchman(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.CharField(max_length=100,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dob=models.CharField(max_length=15,null=True)
    gender=models.CharField(max_length=100,null=True)
    contact=models.CharField(max_length=10,null=True)
    pic=models.FileField(upload_to="media/images/", default="media/socity.jpg")
    def __str__(self):
            return self.first_name

class Event(models.Model):
    event_title=models.CharField(max_length=30)
    dob=models.DateField(auto_now_add=True)
    event_dis=models.CharField(max_length=30)
    pic=models.FileField(upload_to="media/images/", default="media/socity.jpg")

    def __str__(self):
            return self.event_title
        
class Complain(models.Model):
    com_title=models.CharField(max_length=20)
    com_dis=models.CharField(max_length=50)
    
    def __str__(self):
        return self.com_title
    
class Notice(models.Model):
    notice_title=models.CharField(max_length=20)
    dob=models.DateField(auto_now_add=True)
    notice_dis=models.CharField(max_length=50)
    
    def __str__(self):
        return self.notice_title
    
class Visitors(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    flat_no=models.CharField(max_length=10,null=True)
    email=models.CharField(max_length=100,unique=True)
    contact=models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return self.last_name
    
class photos(models.Model):
    pic=models.FileField(upload_to="media/images/", default="media/socity.jpg")
    dob=models.DateField(auto_now_add=True)
    photo_name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.photo_name
    
class Suggestion(models.Model):
    suggestion_title=models.CharField(max_length=20)
    suggestion_dis=models.CharField(max_length=50)
    created_date=models.DateTimeField(auto_now_add= True, blank=False)
    
    def __str__(self):
        return self.suggestion_title
    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.created_date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"

    
class Video(models.Model):
    video=models.FileField(upload_to="media/video/", default="media/")
    dob=models.DateField(auto_now_add=True)
    video_name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.video_name
    
    
    
    
    
