
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserData(models.Model):
	user_username = models.CharField(max_length=50, editable=True)
	first_name =  models.CharField(max_length=50,default='John', editable=True)
	last_name =  models.CharField(max_length=50,default='Doe', editable=True)
	user_about =  models.CharField(max_length=100,default="I'm crazy for the climate.", editable=True)
	user_email =  models.CharField(max_length=50,default='jane.doe@email.com', editable=True)
	user_country = models.CharField(max_length=50,default='Verdeia Republic', editable=True)
	user_ip = models.CharField(max_length=50,default='127.0.0.1', editable=True)

	user_emissions = models.CharField(max_length=50,default='0', editable=True)
	prev_user_emissions1 = models.CharField(max_length=50,default='0', editable=True)
	prev_user_emissions2 = models.CharField(max_length=50,default='0', editable=True)
	prev_user_emissions3 = models.CharField(max_length=50,default='0', editable=True)


	user_offset = models.CharField(max_length=50,default='0', editable=True)
	water_emissions = models.CharField(max_length=50,default='0')

	user_tier =  models.CharField(max_length=50,default='Free account', editable=True)
	user_emissions = models.CharField(max_length=50,default='0', editable=True)

	user_cartype =  models.CharField(max_length=50,default='electric', editable=True)
	user_daily_commute =  models.CharField(max_length=50,default='50km', editable=True)
	user_household_pop =  models.CharField(max_length=50,default='3', editable=True)
	user_energytype_use =  models.CharField(max_length=50,default='grid', editable=True)
	user_ventilation_type =  models.CharField(max_length=50,default='gas', editable=True)
	user_diet =  models.CharField(max_length=50,default='vegan', editable=True)
	user_travel_freq =  models.CharField(max_length=50,default='0', editable=True)

	user_airtravel_percentage = models.CharField(max_length=50,default='0', editable=True)
	user_car_percentage = models.CharField(max_length=50,default='0', editable=True)
	user_house_percentage = models.CharField(max_length=50,default='0', editable=True)
	user_diet_percentage = models.CharField(max_length=50,default='0', editable=True)



	events_attended =  models.CharField(max_length=50,default='0', editable=True)
	projects_funded =  models.CharField(max_length=50,default='0', editable=True)
	active_goals =  models.CharField(max_length=50,default='0', editable=True)
	goals_finished =  models.CharField(max_length=50,default='0', editable=True)


	def __str__(self):
		return self.user_username

	
class Newsletter(models.Model):
	user_email =  models.CharField(max_length=50)

	def __str__(self):
		return self.user_email

class VolunteerEvents(models.Model):
	event_name =  models.CharField(max_length=50, default = 'Verdiea volunteer')
	event_organiser =  models.CharField(max_length=50, default = 'Paradio')
	event_id =  models.CharField(max_length=50, default = '#0013483')
	event_date =  models.CharField(max_length=50, default = '20/04/2303')
	orientation_date =  models.CharField(max_length=50, default = '20/04/2003')
	event_location =  models.CharField(max_length=50, default = 'San francisco')
	event_url =  models.CharField(max_length=50, default = "{% url 'event' %}")

	event_description =  models.CharField(max_length=50, default = 'hello world, welcome to my workplace')
	no_of_signed = models.CharField(max_length=50, default = '0')
	def __str__(self):
		return self.event_name
'''
class Event_1(models.Model):
	signed_user =  models.CharField(max_length=50, default = 'Verdiea volunteer')
	def __str__(self):
		return self.signed_user
'''

class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    event_id = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    organiser = models.CharField(max_length=50)
    eventurl = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.name	

'''
class UserGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)

    def __str__(self):
        return self.name	
        
'''