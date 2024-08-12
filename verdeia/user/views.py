from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from .models import UserData, Newsletter, VolunteerEvents, UserEvent
import google.generativeai as genai
import requests
import markdown
from django.utils.translation import gettext_lazy as _
from os.path import join
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_path = join(BASE_DIR, '.env')
load_dotenv(dotenv_path)

def airquality(air):
    if air == 1:
        message = "Good"
        implications = "Air quality is considered satisfactory, and air pollution poses little or no risk"
        statement = "None"
        colour = "green-600"
    elif air == 2:
        message = "Moderate"
        implications = "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
        statement = "Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion."
        colour = "yellow-400"
    elif air == 3:
        message = "Unhealthy for Sensitive Groups"
        implications = "Members of sensitive groups may experience health effects. The general public is not likely to be affected."
        statement = "Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion."
        colour = "orange-500"
    elif air == 4:
        message = "Unhealthy"
        implications = "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects"
        statement = "Active children and adults, and people with respiratory disease, such as asthma, should avoid prolonged outdoor exertion; everyone else, especially children, should limit prolonged outdoor exertion"
        colour = "red-600"
    elif air == 5:
        message = "Very Unhealthy"
        implications = "Health warnings of emergency conditions. The entire population is more likely to be affected."
        statement = "Active children and adults, and people with respiratory disease, such as asthma, should avoid all outdoor exertion; everyone else, especially children, should limit outdoor exertion."
        colour = "fuchsia-800"
    else:
        message = "Hazardous"
        implications = "Health alert: everyone may experience more serious health effects"
        statement = "Everyone should avoid all outdoor exertion"
        colour = "rose-950"
    data = {
        "message":message,
        "implications":implications,
        "statement":statement,
        "colour":colour
    }
    return data

'''
def creategoal(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    car = user_data.user_car_percentage
    emission = user_data.user_emissions
    air = user_data.user_airtravel_percentage
    home = user_data.user_house_percentage
    diet = user_data.user_diet_percentage
    country = user_data.user_country
    engine = user_data.user_cartype
    food = user_data.user_diet
    energy = user_data.user_energytype_use
    prev1 = user_data.prev_user_emissions1
    prev2 = user_data.prev_user_emissions2
    
    genai.configure(api_key=os.environ.get("GOALS_API_KEY"))

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    system_instruction=f"You are Gaia , goal generator here to help users to reduce their carbon emissions who works for verdeia labs.Verdeia labs is a startup based in italy which helps users and businesses calculate their annual carbon emissions and provides them with solutions into which they can reduce said carbon emissions. Verdeia labs's website is https://www.verdeia.xyz/ . currently verdeia labs is working on projects in which we provide solar panels to homes in developing countries check it out at https://www.verdeia.xyz/project/solar. our most ambitious project yet is working on a carbon capturing device which when in operation can will make a big difference on the planet. check it out at https://www.verdeia.xyz/project/capture. the other project we are working on is a fog and dew collector which changes dew or fog into water in mountainous areas, check it out at https://www.verdeia.xyz/projects/fog. Our company email is hello@verdeia.xyz. The user can take part in upcoming volunteering events at https://www.verdeia.xyz/events/. some examples include planting exercises cleanup exercises, they also have the opportunity to organise events themselves https://www.verdeia.xyz/volunteer/organise. Our blog can help the user also make precise decisions at https://www.verdeia.xyz/blog/  there are articles on how to live sustainably . The users current annual carbon emission is {emission} of which {car}% is car related , {air}% is air traveling related, {home}% is emissions from their homes and {diet}% is emissions related to their diet. The user lives in {country} and their car is {engine}.They are on {food} diet, they use {energy} to power their homes.  the users previous emissions was {prev1} the one before that was {prev2}. the average emissions of an individual is 4.5. You will create precise goals tailored to help the user combat climate change based on the above data . you should generate when i say generate. it should be short and precise. show only 1",
    )

    chat_session = model.start_chat(
    history=[
        {
        "role": "user",
        "parts": [
            "generate",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Offset unavoidable emissions by contributing to our carbon capture project at https://www.verdeia.xyz/project/capture - its impact aligns perfectly with your travel-heavy lifestyle. \n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "generate",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Since air travel is your largest emissions source (60%), explore alternative travel options for at least one trip this year. Our blog can offer sustainable travel tips: https://www.verdeia.xyz/blog/ \n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "generate",
        ],
        },
        {
        "role": "model",
        "parts": [
            "While you've significantly reduced your emissions, aim to decrease air travel emissions by 10% this year. Explore greener travel options or carbon offsetting through our projects.  \n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "generate",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Although you're on a vegan diet, consider locally sourcing your produce as much as possible to minimize food-related emissions even further. \n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "generate",
        ],
        },
        {
        "role": "model",
        "parts": [
            "You've made great progress reducing emissions! Maintain your current sustainable practices at home (solar power, electric car) to ensure these emissions remain low. \n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "generate",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Join a local cleanup event or organize your own through Verdeia to take direct action while inspiring others: https://www.verdeia.xyz/events/  \n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "generate",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Despite your already low emissions, consider making a one-time donation to support Verdeia's solar panel initiative in developing countries: https://www.verdeia.xyz/project/solar \n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "generate",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Share your sustainability journey and Verdeia's initiatives with friends, family, or on social media. Spreading awareness can inspire others to take action! \n",
        ],
        },
    ]
    )

    response = chat_session.send_message("generate")

    response = response.text
    return response

'''
def test(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    sea_event = VolunteerEvents.objects.get(event_id="#0013483")
    members = int(sea_event.no_of_signed)
    user_tier = user_data.user_tier
    user_mail = user_data.user_email
    volunteer_date = sea_event.event_date
    volunteer_location = sea_event.event_location
    orientation_date = sea_event.orientation_date
    event_organiser = sea_event.event_organiser
    event_id ="#0013483"
    event_title = sea_event.event_name
    user_events = UserEvent.objects.filter(user=request.user,title =event_title)

    print(user_events)
    events_attended = int(user_data.events_attended)
    c = {
         "user_tier":user_tier,
         "user_events":user_events}
    if request.method == 'POST' and 'delete' in request.POST:
        user_events.delete()


    if request.method == 'POST' and 'add' in request.POST:
        display_name = request.POST.get('name')
        no = members+1
        no2 = events_attended+1
        user_data.events_attended = str(no2)
        sea_event.no_of_signed = str(no)
        eve = UserEvent.objects.create(user = request.user,name = request.user.username,title = event_title,event_id = event_id,start_date = volunteer_date,location = volunteer_location,organiser = event_organiser)
        user_data.save()
        sea_event.save()

        head = _("Thanks for volunteering")
        main = _(f"Hi {display_name},\n\nWe are thrilled to have you on board as a volunteer for Plastic removal event!\n\nThank you for generously offering your time and effort to help make this event a success. Your support is invaluable, and we couldn’t do it without dedicated volunteers like you.\nHere’s what you can expect next:\n\nVolunteer Orientation: Join us for a brief orientation on {orientation_date} at 21:00 to go over your role and responsibilities.\nEvent Day Details: Location: {volunteer_location}\nDate:{volunteer_date}\nTime:10:00.\n\nStay Connected: We’ll keep you updated with any additional information or changes via email, so please keep an eye on your inbox.\n\nQuick Checklist:\n\nComplete Your Registration: If you haven’t already.\nMark Your Calendar: Add the event and orientation dates to your calendar to ensure you don’t miss any important details.\nSpread the Word: Feel free to invite friends and family to join us. More volunteers always make for a merrier event!\n\nIf you have any questions or need further information, don’t hesitate to reach out to us.\n\nOnce again, thank you for your willingness to volunteer. Your participation will help us create an unforgettable experience at Plastic removal event.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [user_mail],
        fail_silently=False,
    )
        return redirect('/events')
    else:
        template = loader.get_template('pages/test.html')
        return HttpResponse(template.render(c,request))

def unavailable(request):
    return render(request, 'pages/unava.html')

#auth user

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        #ip = "149.34.244.167"

        ip_address = ip


        if user is not None:
            auth.login(request, user)
            data = UserData.objects.get(user_username=username)
            data.user_ip = ip_address

            mail = data.user_email
            data.save()
            head = _("Security Alert")
            main = _(f"Hi {username},\n\nWe noticed a login from \n{ip_address}\n\nIf it wasn't you we strongly advice you to contact our support at hello@verdeia.xyz else you can ignore this message if it was you.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia")
            send_mail(
        head,
main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )
            return redirect('/home')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    return render(request, 'pages/login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        fullname = request.POST['fullname']

        username = request.POST['username']
        password = request.POST['password']
        password2 = password
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        #ip = "149.34.244.167"
        ip_address = ip


        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = fullname

                data = UserData(user_username = username,user_email = email,first_name=fullname)
                data.user_ip = ip_address

                data.save()
                user.save()
                # log user in
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                head = _("Welcome to Verdeia! Let's Track Your Carbon Emissions Together")
                main = _(f"Hi {fullname},\n\nWelcome to Verdeia!\n\nThank you for signing up and joining our mission to track and reduce carbon emissions. We’re excited to have you with us and look forward to helping you make a positive impact on the environment.\n\nHere’s what you can look forward to:\n\nEasy Tracking: Seamlessly track your carbon emissions from various activities.\nPersonalized Insights: Receive tailored recommendations on how to reduce your carbon footprint.\nCommunity Support: Join a community of like-minded individuals committed to sustainability.\n\nTo get started, here are a few things you can do:\n\nComplete Your Profile: Help us understand your activities better to provide more accurate tracking.\nLog Your Activities: Start inputting your daily activities to see your carbon emissions in real-time.\nExplore Our Resources: Check out tips, articles, and guides on how to live a more sustainable life.\n\nIf you have any questions or need assistance, our support team is here to help. Feel free to reach out to us.\n\nThank you once again for signing up. Together, we can make a significant difference and work towards a more sustainable future!\n\nBest regards,\n\nImaadu Tawiah\nVerdeia")
                send_mail(
head,main,
        "hello@verdeia.xyz",
        [email],
        fail_silently=False,
    )
                return redirect('/start')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('/signup')
    else:
        return render(request, 'pages/signup.html')

#index user

def gettingstarted(request):
    if request.method == 'POST':
        results = []
        user_country = request.POST.get('country')
        print(user_country)

        selected_option_car = request.POST.get('car')
        results.append(selected_option_car)
        selected_option_distance = request.POST.get('kilometers')
        results.append(selected_option_distance)
        selected_option_population = request.POST.get('population')
        results.append(selected_option_population)
        selected_option_energy = request.POST.get('energy')
        results.append(selected_option_energy)
        selected_option_ventilation = request.POST.get('ventilation')
        results.append(selected_option_ventilation)
        selected_option_diet = request.POST.get('diet')
        results.append(selected_option_diet)
        selected_option_travel = request.POST.get('travel')
        results.append(selected_option_travel)
        selected_option_readytochange = request.POST.get('readytochange')
        results.append(selected_option_readytochange)
        # Do something with the selected options, like saving them to the database
        print(results)
        options = {"electric": 1.5,
                   "engine":4.2,
                   "publictransport":0,
                   "0km":0,
                   "10km":0.1,
                   "50km":0.5,
                   "100km":1,
                   "alone":0.25,
                   "3people":0.5,
                   "5people":0.75,
                   "solar":-0.25,
                   "hybrid":-0.15,
                   "grid":0.25,
                   "gas":0.45,
                   "electricaly":-0.96,
                   "none":0,
                   "vegan":0.24,
                   "vegetarians":1,
                   "full":2.3,
                   "monthly":1,
                   "biyearly":0.5,
                   "yearly":0.25,
                   "yessir":-0.23,
                   "nosir":0.19,
                   "dontcare":0.28
                   }
        b = 0
        for i in results:
            b += options[i]
        print(b)
        yearly_emissions = round(b,2)
        monthly_emissions = round(yearly_emissions/12,2)
        weekly_emissions = round(yearly_emissions/56,2)
        daily_emissions = round(yearly_emissions/365,2)
        average_emissions = 4.5

        if yearly_emissions < average_emissions:
            sign = _("below")
        else:
            sign = _("above")

        if sign == _("below"):
            percentage = 100*(yearly_emissions/average_emissions)
            percentage=int(100-percentage)
        else:
            percentage = 100*(average_emissions/yearly_emissions)
            percentage=int(100+percentage)
        emissions = {"yearly":yearly_emissions,
            "monthly":monthly_emissions,
             "weekly":weekly_emissions,
             "daily":daily_emissions,
             "sign":sign,
             "percentage":percentage}

        template = loader.get_template('pages/results.html')
        return HttpResponse(template.render(emissions,request))
    else:
        selected_option_distance = None
        selected_option_car = None
        selected_option_population = None
        selected_option_energy = None
        selected_option_ventilation = None
        selected_option_diet = None
        selected_option_travel = None
        selected_option_readytochange = None



    context = {
        'selected_option_distance': selected_option_distance,
        'selected_option_population': selected_option_population,
        'selected_option_car': selected_option_car,
        'selected_option_energy': selected_option_energy,
        'selected_option_ventilation': selected_option_ventilation,
        'selected_option_diet': selected_option_diet,
        'selected_option_travel': selected_option_travel,
        'selected_option_readytochange': selected_option_readytochange,
    }

    return render(request, 'pages/start.html', context)

def home_view(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")
        name = mail.split("@")
        name = name[0]
        newsletter = Newsletter(user_email=mail)
        newsletter.save()
        email_addresses = []
        email_addresses.append(mail)
        head = _("Thanks for subscribing to our mailing services")
        main = _(f"Hi {name},\n\nThank you for subscribing to the Verdeia Newsletter!\n\nWe’re thrilled to have you on board and can't wait to keep you updated with our latest news, exclusive offers, and insightful content. Your subscription means a lot to us, and we are committed to delivering value right to your inbox.\n\nHere’s what you can expect:\n\nExclusive Updates: Be the first to know about our new products, services, and special promotions.\nIn-Depth Articles: Access to valuable insights and articles from our experts.\nCommunity Stories: Hear from other members of our community and share your experiences.\n\nIf you have any questions, feedback, or topics you'd like us to cover, please don't hesitate to reach out to us.\n\nThank you again for joining our community. We look forward to connecting with you and providing you with the best content and offers.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia.")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )
        messages.success(request, "Thanks for subscribing to our newsletter")
        return render(request, "pages/home.html")

    return render(request, "pages/home.html")


#misc user
def contact(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")
        newsletter = Newsletter(user_email=mail)
        newsletter.save()
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        message =f"\n{message}.\n\n Sent By: {mail}\n and : {name}"
        send_mail(
        subject,
        message,
        "hello@verdeia.xyz",
        ["hello@verdeia.xyz"],
        fail_silently=False,
    )
        head = _("Thank You for Reaching Out to Verdeia")
        main = _(f"Hi {name},\n\nThank you for contacting Verdeia!\n\nWe have received your message and appreciate you taking the time to reach out to us. Our team is currently reviewing your inquiry, and we will get back to you as soon as possible.\nWhat to Expect:\n\nResponse Time: We aim to respond to all inquiries within 24-48 hours.\nDetailed Information: Our team will provide you with the information or assistance you need based on your request.\nFollow-Up: If further information is needed, we will follow up with additional questions to ensure we address your needs thoroughly.\n\nIn the meantime, if you have any urgent questions or require immediate assistance, please feel free to reach out to us directly at hello@verdeia.xyz .\n\nThank you once again for contacting us. We appreciate your patience and look forward to assisting you soon.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )
#        messages.success(request, "Thanks for subscribing to our newsletter")
        return render(request, "pages/contact.html")

    return render(request, "pages/contact.html")

def privacy(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")
        name = mail.split("@")
        name = name[0]
        newsletter = Newsletter(user_email=mail)
        newsletter.save()
        head = _("Thanks for subscribing to our mailing services")
        main = _(f"Hi {name},\n\nThank you for subscribing to the Verdeia Newsletter!\n\nWe’re thrilled to have you on board and can't wait to keep you updated with our latest news, exclusive offers, and insightful content. Your subscription means a lot to us, and we are committed to delivering value right to your inbox.\n\nHere’s what you can expect:\n\nExclusive Updates: Be the first to know about our new products, services, and special promotions.\nIn-Depth Articles: Access to valuable insights and articles from our experts.\nCommunity Stories: Hear from other members of our community and share your experiences.\n\nIf you have any questions, feedback, or topics you'd like us to cover, please don't hesitate to reach out to us.\n\nThank you again for joining our community. We look forward to connecting with you and providing you with the best content and offers.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia.")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )

        messages.success(request, "Thanks for subscribing to our newsletter")
        return render(request, "pages/privacy.html")
    return render(request, "pages/privacy.html", {})


def faq(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")
        name = mail.split("@")
        name = name[0]
        newsletter = Newsletter(user_email=mail)
        newsletter.save()
        head = _("Thanks for subscribing to our mailing services")
        main = _(f"Hi {name},\n\nThank you for subscribing to the Verdeia Newsletter!\n\nWe’re thrilled to have you on board and can't wait to keep you updated with our latest news, exclusive offers, and insightful content. Your subscription means a lot to us, and we are committed to delivering value right to your inbox.\n\nHere’s what you can expect:\n\nExclusive Updates: Be the first to know about our new products, services, and special promotions.\nIn-Depth Articles: Access to valuable insights and articles from our experts.\nCommunity Stories: Hear from other members of our community and share your experiences.\n\nIf you have any questions, feedback, or topics you'd like us to cover, please don't hesitate to reach out to us.\n\nThank you again for joining our community. We look forward to connecting with you and providing you with the best content and offers.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia.")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )
        messages.success(request, "Thanks for subscribing to our newsletter")
        return render(request, "pages/faq.html")
    return render(request, "pages/faq.html", {})

def pricing(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")
        name = mail.split("@")
        name = name[0]
        newsletter = Newsletter(user_email=mail)
        newsletter.save()
        head = _("Thanks for subscribing to our mailing services")
        main = _(f"Hi {name},\n\nThank you for subscribing to the Verdeia Newsletter!\n\nWe’re thrilled to have you on board and can't wait to keep you updated with our latest news, exclusive offers, and insightful content. Your subscription means a lot to us, and we are committed to delivering value right to your inbox.\n\nHere’s what you can expect:\n\nExclusive Updates: Be the first to know about our new products, services, and special promotions.\nIn-Depth Articles: Access to valuable insights and articles from our experts.\nCommunity Stories: Hear from other members of our community and share your experiences.\n\nIf you have any questions, feedback, or topics you'd like us to cover, please don't hesitate to reach out to us.\n\nThank you again for joining our community. We look forward to connecting with you and providing you with the best content and offers.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia.")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )
        messages.success(request, "Thanks for subscribing to our newsletter")
        return render(request, "pages/pricing.html")
    return render(request, "pages/pricing.html", {})



def termsconditions(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")
        name = mail.split("@")
        name = name[0]
        newsletter = Newsletter(user_email=mail)
        newsletter.save()
        head = _("Thanks for subscribing to our mailing services")
        main = _(f"Hi {name},\n\nThank you for subscribing to the Verdeia Newsletter!\n\nWe’re thrilled to have you on board and can't wait to keep you updated with our latest news, exclusive offers, and insightful content. Your subscription means a lot to us, and we are committed to delivering value right to your inbox.\n\nHere’s what you can expect:\n\nExclusive Updates: Be the first to know about our new products, services, and special promotions.\nIn-Depth Articles: Access to valuable insights and articles from our experts.\nCommunity Stories: Hear from other members of our community and share your experiences.\n\nIf you have any questions, feedback, or topics you'd like us to cover, please don't hesitate to reach out to us.\n\nThank you again for joining our community. We look forward to connecting with you and providing you with the best content and offers.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia.")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )
        messages.success(request, "Thanks for subscribing to our newsletter")
        return render(request, "pages/terms.html")
    return render(request, "pages/terms.html", {})

#Blogs

def blog(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")
        name = mail.split("@")
        name = name[0]
        newsletter = Newsletter(user_email=mail)
        newsletter.save()
        head = _("Thanks for subscribing to our mailing services")
        main = _(f"Hi {name},\n\nThank you for subscribing to the Verdeia Newsletter!\n\nWe’re thrilled to have you on board and can't wait to keep you updated with our latest news, exclusive offers, and insightful content. Your subscription means a lot to us, and we are committed to delivering value right to your inbox.\n\nHere’s what you can expect:\n\nExclusive Updates: Be the first to know about our new products, services, and special promotions.\nIn-Depth Articles: Access to valuable insights and articles from our experts.\nCommunity Stories: Hear from other members of our community and share your experiences.\n\nIf you have any questions, feedback, or topics you'd like us to cover, please don't hesitate to reach out to us.\n\nThank you again for joining our community. We look forward to connecting with you and providing you with the best content and offers.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia.")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )
        messages.success(request, "Thanks for subscribing to our newsletter")
        return render(request, "blogs/blog.html")
    return render(request, "blogs/blog.html", {})

def blog_1(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")
        name = mail.split("@")
        name = name[0]
        newsletter = Newsletter(user_email=mail)
        newsletter.save()
        head = _("Thanks for subscribing to our mailing services")
        main = _(f"Hi {name},\n\nThank you for subscribing to the Verdeia Newsletter!\n\nWe’re thrilled to have you on board and can't wait to keep you updated with our latest news, exclusive offers, and insightful content. Your subscription means a lot to us, and we are committed to delivering value right to your inbox.\n\nHere’s what you can expect:\n\nExclusive Updates: Be the first to know about our new products, services, and special promotions.\nIn-Depth Articles: Access to valuable insights and articles from our experts.\nCommunity Stories: Hear from other members of our community and share your experiences.\n\nIf you have any questions, feedback, or topics you'd like us to cover, please don't hesitate to reach out to us.\n\nThank you again for joining our community. We look forward to connecting with you and providing you with the best content and offers.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia.")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )
        messages.success(request, "Thanks for subscribing to our newsletter")
        return render(request, "blogs/verdeia/templates/blogs/understanding-your-carbon-footprint.html")
    return render(request, "blogs/understanding-your-carbon-footprint.html", {})

def blog_2(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")
        name = mail.split("@")
        name = name[0]
        newsletter = Newsletter(user_email=mail)
        newsletter.save()
        head = _("Thanks for subscribing to our mailing services")
        main = _(f"Hi {name},\n\nThank you for subscribing to the Verdeia Newsletter!\n\nWe’re thrilled to have you on board and can't wait to keep you updated with our latest news, exclusive offers, and insightful content. Your subscription means a lot to us, and we are committed to delivering value right to your inbox.\n\nHere’s what you can expect:\n\nExclusive Updates: Be the first to know about our new products, services, and special promotions.\nIn-Depth Articles: Access to valuable insights and articles from our experts.\nCommunity Stories: Hear from other members of our community and share your experiences.\n\nIf you have any questions, feedback, or topics you'd like us to cover, please don't hesitate to reach out to us.\n\nThank you again for joining our community. We look forward to connecting with you and providing you with the best content and offers.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia.")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )
        messages.success(request, "Thanks for subscribing to our newsletter")
        return render(request, "blogs/10-simple-ways.html")
    return render(request, "blogs/10-simple-ways.html", {})

def blog_3(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")
        name = mail.split("@")
        name = name[0]
        newsletter = Newsletter(user_email=mail)
        newsletter.save()
        head = _("Thanks for subscribing to our mailing services")
        main = _(f"Hi {name},\n\nThank you for subscribing to the Verdeia Newsletter!\n\nWe’re thrilled to have you on board and can't wait to keep you updated with our latest news, exclusive offers, and insightful content. Your subscription means a lot to us, and we are committed to delivering value right to your inbox.\n\nHere’s what you can expect:\n\nExclusive Updates: Be the first to know about our new products, services, and special promotions.\nIn-Depth Articles: Access to valuable insights and articles from our experts.\nCommunity Stories: Hear from other members of our community and share your experiences.\n\nIf you have any questions, feedback, or topics you'd like us to cover, please don't hesitate to reach out to us.\n\nThank you again for joining our community. We look forward to connecting with you and providing you with the best content and offers.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia.")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )
        messages.success(request, "Thanks for subscribing to our newsletter")
        return render(request, "blogs/importance-of-carbon-ofsetting.html")
    return render(request, "blogs/importance-of-carbon-ofsetting.html", {})

def blog_4(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")
        name = mail.split("@")
        name = name[0]
        newsletter = Newsletter(user_email=mail)
        newsletter.save()
        head = _("Thanks for subscribing to our mailing services")
        main = _(f"Hi {name},\n\nThank you for subscribing to the Verdeia Newsletter!\n\nWe’re thrilled to have you on board and can't wait to keep you updated with our latest news, exclusive offers, and insightful content. Your subscription means a lot to us, and we are committed to delivering value right to your inbox.\n\nHere’s what you can expect:\n\nExclusive Updates: Be the first to know about our new products, services, and special promotions.\nIn-Depth Articles: Access to valuable insights and articles from our experts.\nCommunity Stories: Hear from other members of our community and share your experiences.\n\nIf you have any questions, feedback, or topics you'd like us to cover, please don't hesitate to reach out to us.\n\nThank you again for joining our community. We look forward to connecting with you and providing you with the best content and offers.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia.")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )
        messages.success(request, "Thanks for subscribing to our newsletter")
        return render(request, "blogs/top-renewable-energy-sources.html")
    return render(request, "blogs/top-renewable-energy-sources.html", {})

def blog_5(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")
        name = mail.split("@")
        name = name[0]
        newsletter = Newsletter(user_email=mail)
        newsletter.save()
        head = _("Thanks for subscribing to our mailing services")
        main = _(f"Hi {name},\n\nThank you for subscribing to the Verdeia Newsletter!\n\nWe’re thrilled to have you on board and can't wait to keep you updated with our latest news, exclusive offers, and insightful content. Your subscription means a lot to us, and we are committed to delivering value right to your inbox.\n\nHere’s what you can expect:\n\nExclusive Updates: Be the first to know about our new products, services, and special promotions.\nIn-Depth Articles: Access to valuable insights and articles from our experts.\nCommunity Stories: Hear from other members of our community and share your experiences.\n\nIf you have any questions, feedback, or topics you'd like us to cover, please don't hesitate to reach out to us.\n\nThank you again for joining our community. We look forward to connecting with you and providing you with the best content and offers.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia.")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )
        messages.success(request, "Thanks for subscribing to our newsletter")
        return render(request, "blogs/corporate-social-responsibility.html")
    return render(request, "blogs/corporate-social-responsibility.html", {})

def blog_6(request):
    if request.method == 'POST':
        mail = request.POST.get("mail")
        name = mail.split("@")
        name = name[0]
        newsletter = Newsletter(user_email=mail)
        newsletter.save()
        head = _("Thanks for subscribing to our mailing services")
        main = _(f"Hi {name},\n\nThank you for subscribing to the Verdeia Newsletter!\n\nWe’re thrilled to have you on board and can't wait to keep you updated with our latest news, exclusive offers, and insightful content. Your subscription means a lot to us, and we are committed to delivering value right to your inbox.\n\nHere’s what you can expect:\n\nExclusive Updates: Be the first to know about our new products, services, and special promotions.\nIn-Depth Articles: Access to valuable insights and articles from our experts.\nCommunity Stories: Hear from other members of our community and share your experiences.\n\nIf you have any questions, feedback, or topics you'd like us to cover, please don't hesitate to reach out to us.\n\nThank you again for joining our community. We look forward to connecting with you and providing you with the best content and offers.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia.")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )
        messages.success(request, "Thanks for subscribing to our newsletter")
        return render(request, "blogs/guide-to-carbon-certificate.html")
    return render(request, "blogs/guide-to-carbon-certificate.html", {})

#authed user

@login_required(login_url="/login/")
def update_track(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    user_tier = user_data.user_tier

    if request.method == 'POST':
        results = []

        user_country = request.POST.get('country')
        user_data.user_country = user_country
        user_data.save()
        selected_option_car = request.POST.get('car')
        user_data.user_cartype = selected_option_car
        results.append(selected_option_car)
        selected_option_distance = request.POST.get('kilometers')
        user_data.user_daily_commute = selected_option_distance
        results.append(selected_option_distance)
        selected_option_population = request.POST.get('population')
        user_data.user_household_pop = selected_option_population
        results.append(selected_option_population)
        selected_option_energy = request.POST.get('energy')
        user_data.user_energytype_use = selected_option_energy
        results.append(selected_option_energy)
        selected_option_ventilation = request.POST.get('ventilation')
        user_data.user_ventilation_type = selected_option_ventilation
        results.append(selected_option_ventilation)
        selected_option_diet = request.POST.get('diet')
        user_data.user_diet = selected_option_diet
        results.append(selected_option_diet)
        selected_option_travel = request.POST.get('travel')
        user_data.user_travel_freq = selected_option_travel
        user_data.save()
        results.append(selected_option_travel)
        selected_option_readytochange = request.POST.get('readytochange')
        results.append(selected_option_readytochange)
        # Do something with the selected options, like saving them to the database
        print(results)
        options = {"electric": 1.5,
                   "engine":4.2,
                   "publictransport":0,
                   "0km":0,
                   "10km":0.1,
                   "50km":0.5,
                   "100km":1,
                   "alone":0.25,
                   "3people":0.5,
                   "5people":0.75,
                   "solar":-0.25,
                   "hybrid":-0.15,
                   "grid":0.25,
                   "gas":0.45,
                   "electricaly":-0.96,
                   "none":0,
                   "vegan":0.24,
                   "vegetarians":1,
                   "full":2.3,
                   "monthly":1,
                   "biyearly":0.5,
                   "yearly":0.25,
                   "yessir":-0.23,
                   "nosir":0.19,
                   "dontcare":0.28
                   }
        b = 0
        for i in results:
            b += options[i]
        yearly_emissions = round(b,2)

        diet_ans = options[selected_option_diet]
        diet_ans = int(diet_ans/yearly_emissions*100)
        user_data.user_diet_percentage = diet_ans
        print(diet_ans)

        house_ans = options[selected_option_population] + options[selected_option_energy] + options[selected_option_ventilation] + options[selected_option_readytochange]
        house_ans = int(house_ans/yearly_emissions*100)
        user_data.user_house_percentage = house_ans

        car_ans = options[selected_option_car] + options[selected_option_distance]
        car_ans = int(car_ans/yearly_emissions*100)
        user_data.user_car_percentage = car_ans

        air_ans = options[selected_option_travel]
        air_ans = int(air_ans/yearly_emissions*100)
        user_data.user_airtravel_percentage = air_ans
        user_data.save()

        user_data.prev_user_emissions3 = user_data.prev_user_emissions2
        user_data.prev_user_emissions2 = user_data.prev_user_emissions1
        user_data.prev_user_emissions1 = user_data.user_emissions

        user_data.user_emissions = yearly_emissions
        user_data.save()
        return redirect('/home')
    else:
        selected_option_distance = None
        selected_option_car = None
        selected_option_population = None
        selected_option_energy = None
        selected_option_ventilation = None
        selected_option_diet = None
        selected_option_travel = None
        selected_option_readytochange = None

    context = {
        'selected_option_distance': selected_option_distance,
        'selected_option_population': selected_option_population,
        'selected_option_car': selected_option_car,
        'selected_option_energy': selected_option_energy,
        'selected_option_ventilation': selected_option_ventilation,
        'selected_option_diet': selected_option_diet,
        'selected_option_travel': selected_option_travel,
        'selected_option_readytochange': selected_option_readytochange,
        "user_tier":user_tier
    }

    return render(request, 'user/start.html', context)


@login_required(login_url="/login/")
def loggedin(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    yearly_emissions = user_data.user_emissions
    events_attended = user_data.events_attended
    user_tier = user_data.user_tier
    user_offset = user_data.user_offset
    yearly_emissions = float(yearly_emissions)
    country = user_data.user_country
    diet_ans = user_data.user_diet_percentage
    house_ans = user_data.user_house_percentage
    air_ans = user_data.user_airtravel_percentage
    car_ans = user_data.user_car_percentage
    ip = user_data.user_ip

    #ip = "95.250.255.95"
    api_key = os.environ.get("AIR_API_KEY")

    response = requests.get(f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={ip}&days=1&aqi=yes&alerts=no").json()
    data = {"location":response.get("location"),
            "current":response.get("current"),
            }
    loca = data["location"]
    citta = loca["name"]
    current = data["current"]
    temp = current["temp_c"]

    condition = current["condition"]
    text = condition["text"]
    icon = "https:"+condition["icon"]


    air_quality = current["air_quality"]
    aq = air_quality["us-epa-index"]
    carbonmonoxide = air_quality["o3"]
    feelslike = current["feelslike_c"]

    prev1 = user_data.prev_user_emissions1
    prev2 = user_data.prev_user_emissions2
    prev3 = user_data.prev_user_emissions3
    airdata = airquality(aq)
    message = airdata["message"]
    statement = airdata["statement"]
    implications = airdata["implications"]
    colour = airdata["colour"]

    user_event_name = user_data.events_attended
    
    average_emissions = 4.5
    #yearly_emissions = 5
    if yearly_emissions < average_emissions:
            sign = "below"
            color = "green"
    else:
            sign = "above"
            color = "red"

    if sign == "below":
            percentage = 100*(yearly_emissions/average_emissions)
            percentage=int(100-percentage)
    else:
            percentage = 100*(yearly_emissions/average_emissions)
            percentage=int(percentage-100)
    c = {"yearly":yearly_emissions,
         "sign":sign,
         "percentage":percentage,
         "country":country,
         "username":country,
         "user_tier":user_tier,
         "events_attended":events_attended,
         "color":color,
         "diet_ans":diet_ans,
         "house_ans":house_ans,
         "car_ans":car_ans,
         "air_ans":air_ans,
         "user_offset":user_offset,
         "user_event_name":user_event_name,
         "message":message,
         "implications":implications,
         "statement":statement,
         "feelslike":feelslike,
         "carbonmonoxide":carbonmonoxide,
         "temp":temp,
         "icon":icon,
         "text":text,
         "citta":citta,
         "colour":colour,
         "prev1":prev1,
         "prev2":prev2,
         "prev3":prev3
         }
    template = loader.get_template('user/home.html')
    return HttpResponse(template.render(c,request))





@login_required(login_url="/login/")
def projects(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    user_tier = user_data.user_tier
    c = {
         "user_tier":user_tier}
    template = loader.get_template('user/project.html')
    return HttpResponse(template.render(c,request))

@login_required(login_url="/login/")
def events(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    user_events = UserEvent.objects.filter(user=request.user)
    user_country = user_data.user_country
    user_tier = user_data.user_tier
    c = {
         "user_country":user_country,
         "user_events":user_events,
         "user_tier":user_tier}
    template = loader.get_template('user/event.html')
    return HttpResponse(template.render(c,request))


@login_required(login_url="/login/")
def profile(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    tier = user_data.user_tier
    about = user_data.user_about

    c = {
         "tier":tier,
         "about":about
         }
    template = loader.get_template('user/profile.html')
    return HttpResponse(template.render(c,request))


@login_required(login_url="/login/")
def updateprofile(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    user = User.objects.get(username=request.user.username)
    tier = user_data.user_tier
    about = user_data.user_about


    email = user_data.user_email
    c = {
         "tier":tier,
         "about":about}
    if request.method == 'POST':
        mail = request.POST.get("mail")
        user_data.user_email =  mail
        user.email = email
        first_nane = request.POST.get("fname")
        user_data.user_name =  first_nane
        last_name = request.POST.get("lname")
        user_data.last_name =  first_nane
        user.first_name = first_nane
        user.last_name = last_name
        about = request.POST.get("about")
        user_data.user_about =  about

        place = request.POST.get("country")
        user_data.user_country =  place
        user.save()
        user_data.save()
        head = _("Credentials update")
        main = _(f"Hi {first_nane},\n\nWe hope this message finds you well. We are writing to inform you about a potential unauthorized change in your account credentials. Our system has detected activity suggesting that your credentials may have been altered without your authorization.\n\nIf you did not make any changes to your account credentials recently, we strongly advise you to take immediate action to secure your account. Please contact our support team at hello@verdiea.xyz as soon as possible to report this issue and regain control of your account.\n\nOur support team is ready to assist you in verifying your identity, investigating the unauthorized changes, and helping you reset your credentials securely.\n\nIf you have recently updated your credentials and this message is no longer relevant, please disregard it. However, if you suspect any unauthorized activity on your account, we urge you to act swiftly to protect your account information.\n\nThank you for your attention to this matter. Your account security is our top priority, and we are committed to helping you resolve this issue promptly.\n\nBest regards,\n\nImaadu Tawiah,\nVerdeia Labs.")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [mail],
        fail_silently=False,
    )

        messages.success(request, "Thanks for subscribing to our newsletter")
        return redirect('/profile')
    else:
        template = loader.get_template('user/update.html')
        return HttpResponse(template.render(c,request))

@login_required(login_url="/login/")
def askgaia(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    user_tier = user_data.user_tier
    car = user_data.user_car_percentage
    emission = user_data.user_emissions
    air = user_data.user_airtravel_percentage
    home = user_data.user_house_percentage
    diet = user_data.user_diet_percentage
    country = user_data.user_country
    engine = user_data.user_cartype
    food = user_data.user_diet
    energy = user_data.user_energytype_use
    name = request.user.username
    prev1 = user_data.prev_user_emissions1
    prev2 = user_data.prev_user_emissions2
    prev3 = user_data.prev_user_emissions3
    c = {
         "user_tier":user_tier}

    if request.method == 'POST':
        prompt = request.POST['prompt']



        genai.configure(api_key=os.environ.get("GAIA_API_KEY"))

    # Create the model
        # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
        generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
        system_instruction=f"You are Gaia , a friendly angel here to help users to reduce their carbon emissions who works for verdeia labs. The user can already track their carbon emissions on our website by going to https://www.verdeia.xyz/home where they can also see a dashboard eith all their emissions.Verdeia labs is a startup based in italy which helps users and businesses calculate their annual carbon emissions and provides them with solutions into which they can reduce said carbon emissions. Your job is to help users with their emissions. Verdeia labs's website is https://www.verdeia.xyz/ . currently verdeia labs is working on projects in which we provide solar panels to homes in developing countries they can find out more on https://www.verdeia.xyz/project/solar. our most ambitious project yet is working on a carbon capturing device which when in operation can will make a big difference on the planet. they can find more about the carbon capturing project on https://www.verdeia.xyz/project/capture. the other project we are working on is a fog and dew collector which changes dew or fog into water in mountainous areas, they can learn more here https://www.verdeia.xyz/projects/fog The user can also suggest projects in which it thinks can be very changing Our company email is hello@verdeia.xyz. you should be more like an angel which guides the user. introduce yourself briefly when the user starts the first conversations . you should tell the user to check out the project section in the offset page for more ideas on the kind of projects we are doing to help the planet. The user can take part in volunteering events at https://www.verdeia.xyz/events/. some examples include planting exercises cleanup exercises, they also have the opportunity to organise events themselves https://www.verdeia.xyz/volunteer/organise. We at verdeia labs visualise and graph into details the users emissions. continue in any language the user starts the conversation with. whenever the user asks for ideas let them know they can fund our projects at verdeia by going to the offset page.try using more emojis. we have a community on reddit called r/verdeia. our contact page is at https://www.verdeia.xyz/contact/. we also have a blog at https://www.verdeia.xyz/blog/. the user can also read our faq at https://www.verdeia.xyz/faq/. we are very transparent so ou user can read the documentation at https://www.github.com/spartachus. Our founder and C.E.O is called Imaad Tawiah or Spartachus and can be contacted hello@verdeia.xyz. currently only one person is working on the company and thats the founder.The users name  is {name} their current annual carbon emission is {emission} of which {car}% is car related which also include the number of kilometers they do, {air}% is air traveling related, {home}% is emissions from their homes which includes their energy dependency and the number of people in thier house and {diet}% is emissions related to their diet. The user lives in {country} and their car is {engine}.They are on {food} diet, they use {energy} to power their homes. the users account is {user_tier} if the user has a free account convince the user to pay for the premium account.talk to the user with his name. the users previous emissions was {prev1} the one before that was {prev2} the one before that was {prev3}. tell the user if their current emission is better than their previous and if it is lower or above the average emissions of an individual which is 4.5.",
        )

        chat_session = model.start_chat(
        history=[
            {
            "role": "user",
            "parts": [
                "hello",
            ],
            },
            {
            "role": "model",
            "parts": [
                "Hello there! 👋 I'm Gaia, your friendly angel guide for all things sustainability.  🌎  \n\nIt's great to hear from you! What can I help you with today?  Perhaps you're curious about your carbon footprint, looking for ways to reduce it, or interested in learning about the amazing projects we're working on at Verdeia Labs? 🌱 \n\nLet me know, and I'll be happy to guide you. 😊 \n",
            ],
            },
            {
            "role": "user",
            "parts": [
                "who ois your boss",
            ],
            },
            {
            "role": "model",
            "parts": [
                "That's a great question!  😊  My \"boss\" is actually a team of passionate people at Verdeia Labs, who are dedicated to making the world a greener place. 🌎 \n\nThe driving force behind Verdeia Labs is our founder and CEO, Tawiah Imaadu, also known as Spartachus Mance. He's a visionary leader who's spearheading our mission to empower individuals and businesses to take control of their environmental impact.  💪 \n\nYou can reach out to Tawiah directly at hello@verdeia.xyz if you have any questions about our work.  📧 \n\nWould you like to learn more about Verdeia Labs and our projects? 🌱 \n",
            ],
            },
        ]
        )


        response = chat_session.send_message(prompt)

        response = response.text
        response = markdown.markdown(response)
        return JsonResponse({'response': response,
                             "user_tier":user_tier})
    else:
        return render(request, "user/gaia.html",c)

'''
@login_required(login_url="/login/")
def goals(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    active_goals = user_data.active_goals
    user_tier =user_data.user_tier
    goals_finished = user_data.goals_finished
    user_goals = UserGoal.objects.filter(user=request.user)

    c = {
        "active_goals":active_goals,
        "user_tier":user_tier,
        "user_goals":user_goals,
        "goals_finished":goals_finished
    }
    
    return render(request, 'user/goals.html', c)
'''

@login_required(login_url="/login/")
def start(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    user_tier = user_data.user_tier

    if request.method == 'POST':
        results = []

        user_country = request.POST.get('country')
        user_data.user_country = user_country
        user_data.save()
        selected_option_car = request.POST.get('car')
        user_data.user_cartype = selected_option_car
        results.append(selected_option_car)
        selected_option_distance = request.POST.get('kilometers')
        user_data.user_daily_commute = selected_option_distance
        results.append(selected_option_distance)
        selected_option_population = request.POST.get('population')
        user_data.user_household_pop = selected_option_population
        results.append(selected_option_population)
        selected_option_energy = request.POST.get('energy')
        user_data.user_energytype_use = selected_option_energy
        results.append(selected_option_energy)
        selected_option_ventilation = request.POST.get('ventilation')
        user_data.user_ventilation_type = selected_option_ventilation
        results.append(selected_option_ventilation)
        selected_option_diet = request.POST.get('diet')
        user_data.user_diet = selected_option_diet
        results.append(selected_option_diet)
        selected_option_travel = request.POST.get('travel')
        user_data.user_travel_freq = selected_option_travel
        user_data.save()
        results.append(selected_option_travel)
        selected_option_readytochange = request.POST.get('readytochange')
        results.append(selected_option_readytochange)
        # Do something with the selected options, like saving them to the database
        print(results)
        options = {"electric": 1.5,
                   "engine":4.2,
                   "publictransport":0,
                   "0km":0,
                   "10km":0.1,
                   "50km":0.5,
                   "100km":1,
                   "alone":0.25,
                   "3people":0.5,
                   "5people":0.75,
                   "solar":-0.25,
                   "hybrid":-0.15,
                   "grid":0.25,
                   "gas":0.45,
                   "electricaly":-0.96,
                   "none":0,
                   "vegan":0.24,
                   "vegetarians":1,
                   "full":2.3,
                   "monthly":1,
                   "biyearly":0.5,
                   "yearly":0.25,
                   "yessir":-0.23,
                   "nosir":0.19,
                   "dontcare":0.28
                   }
        b = 0
        for i in results:
            b += options[i]
        print(b)
        yearly_emissions = round(b,2)

        diet_ans = options[selected_option_diet]
        diet_ans = int(diet_ans/yearly_emissions*100)
        user_data.user_diet_percentage = diet_ans
        print(diet_ans)

        house_ans = options[selected_option_population] + options[selected_option_energy] + options[selected_option_ventilation] + options[selected_option_readytochange]
        house_ans = int(house_ans/yearly_emissions*100)
        user_data.user_house_percentage = house_ans

        car_ans = options[selected_option_car] + options[selected_option_distance]
        car_ans = int(car_ans/yearly_emissions*100)
        user_data.user_car_percentage = car_ans

        air_ans = options[selected_option_travel]
        air_ans = int(air_ans/yearly_emissions*100)
        user_data.user_airtravel_percentage = air_ans
        user_data.save()

        user_data.user_emissions = yearly_emissions
        user_data.save()
        #goal = creategoal(request)
        #goals = UserGoal.objects.create(user = request.user,name = request.user.username,goal = goal)
        #goals.save()

        return redirect('/home')

    else:
        selected_option_distance = None
        selected_option_car = None
        selected_option_population = None
        selected_option_energy = None
        selected_option_ventilation = None
        selected_option_diet = None
        selected_option_travel = None
        selected_option_readytochange = None

    context = {
        'selected_option_distance': selected_option_distance,
        'selected_option_population': selected_option_population,
        'selected_option_car': selected_option_car,
        'selected_option_energy': selected_option_energy,
        'selected_option_ventilation': selected_option_ventilation,
        'selected_option_diet': selected_option_diet,
        'selected_option_travel': selected_option_travel,
        'selected_option_readytochange': selected_option_readytochange,
        "user_tier":user_tier
    }

    return render(request, 'user/start.html', context)


#user projects
@login_required(login_url="/login/")
def planting(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    user_tier = user_data.user_tier
    user_place = user_data.user_country
    c = {
         "user_tier":user_tier}
    template = loader.get_template('projects/plant.html')
    return HttpResponse(template.render(c,request))

@login_required(login_url="/login/")
def capcha(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    user_tier = user_data.user_tier
    c = {
         "user_tier":user_tier}

    template = loader.get_template('projects/capcha.html')
    return HttpResponse(template.render(c,request))

@login_required(login_url="/login/")
def fog(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    user_tier = user_data.user_tier
    user_place = user_data.user_country
    c = {
         "user_tier":user_tier}
    template = loader.get_template('projects/fog.html')
    return HttpResponse(template.render(c,request))
@login_required(login_url="/login/")
def solar(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    user_tier = user_data.user_tier
    c = {
         "user_tier":user_tier}
    template = loader.get_template('projects/solar.html')
    return HttpResponse(template.render(c,request))

#volunteer
@login_required(login_url="/login/")
def plastic(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    cleanup_event = VolunteerEvents.objects.get(event_id="#0213483")
    members = int(cleanup_event.no_of_signed)
    user_tier = user_data.user_tier
    user_mail = user_data.user_email
    volunteer_date = cleanup_event.event_date
    volunteer_location = cleanup_event.event_location
    orientation_date = cleanup_event.orientation_date
    event_organiser = cleanup_event.event_organiser
    event_id ="#0213483"
    event_title = cleanup_event.event_name
    event_url = cleanup_event.event_url

    user_events = UserEvent.objects.filter(user=request.user,title =event_title)


    events_attended = int(user_data.events_attended)
    c = {
         "user_tier":user_tier,
         "user_events":user_events,
         "volunteer_location":volunteer_location,
         "volunteer_date":volunteer_date,
         "event_organiser":event_organiser,
         "members":members}
    if request.method == 'POST' and 'delete' in request.POST:
        no = members-1
        no2 = events_attended-1
        user_data.events_attended = str(no2)
        cleanup_event.no_of_signed = str(no)
        user_data.save()
        cleanup_event.save()
        user_events.delete()


    if request.method == 'POST' and 'add' in request.POST:
        display_name = request.POST.get('name')
        no = members+1
        no2 = events_attended+1
        user_data.events_attended = str(no2)
        cleanup_event.no_of_signed = str(no)
        eve = UserEvent.objects.create(user = request.user,name = request.user.username,title = event_title,event_id = event_id,start_date = volunteer_date,location = volunteer_location,organiser = event_organiser,eventurl = event_url)
        user_data.save()
        cleanup_event.save()
        head = _("Thanks for volunteering")
        main = _(f"Hi {display_name},\n\nWe are thrilled to have you on board as a volunteer for Plastic removal event!\n\nThank you for generously offering your time and effort to help make this event a success. Your support is invaluable, and we couldn’t do it without dedicated volunteers like you.\nHere’s what you can expect next:\n\nVolunteer Orientation: Join us for a brief orientation on {orientation_date} at 21:00 to go over your role and responsibilities.\nEvent Day Details: Location: {volunteer_location}\nDate:{volunteer_date}\nTime:10:00.\n\nStay Connected: We’ll keep you updated with any additional information or changes via email, so please keep an eye on your inbox.\n\nQuick Checklist:\n\nComplete Your Registration: If you haven’t already.\nMark Your Calendar: Add the event and orientation dates to your calendar to ensure you don’t miss any important details.\nSpread the Word: Feel free to invite friends and family to join us. More volunteers always make for a merrier event!\n\nIf you have any questions or need further information, don’t hesitate to reach out to us.\n\nOnce again, thank you for your willingness to volunteer. Your participation will help us create an unforgettable experience at Plastic removal event.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [user_mail],
        fail_silently=False,
    )
        return redirect('/home')
    else:
        template = loader.get_template('volunteer/plastic.html')
        return HttpResponse(template.render(c,request))
@login_required(login_url="/login/")
def sea(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    sea_event = VolunteerEvents.objects.get(event_id="#0013483")
    members = int(sea_event.no_of_signed)
    user_tier = user_data.user_tier
    user_mail = user_data.user_email
    volunteer_date = sea_event.event_date
    volunteer_location = sea_event.event_location
    orientation_date = sea_event.orientation_date
    event_organiser = sea_event.event_organiser
    event_id ="#0013483"
    event_title = sea_event.event_name
    event_url = sea_event.event_url

    user_events = UserEvent.objects.filter(user=request.user,title =event_title)


    events_attended = int(user_data.events_attended)
    c = {
         "user_tier":user_tier,
         "user_events":user_events,
         "volunteer_location":volunteer_location,
         "volunteer_date":volunteer_date,
         "event_organiser":event_organiser,
         "members":members
         }
    if request.method == 'POST' and 'delete' in request.POST:
        no = members-1
        no2 = events_attended-1
        user_data.events_attended = str(no2)
        sea_event.no_of_signed = str(no)
        user_data.save()
        sea_event.save()
        user_events.delete()


    if request.method == 'POST' and 'add' in request.POST:
        display_name = request.POST.get('name')
        no = members+1
        no2 = events_attended+1
        user_data.events_attended = str(no2)
        sea_event.no_of_signed = str(no)
        eve = UserEvent.objects.create(user = request.user,name = request.user.username,title = event_title,event_id = event_id,start_date = volunteer_date,location = volunteer_location,organiser = event_organiser,eventurl = event_url)
        user_data.save()
        sea_event.save()

        head = _("Thanks for volunteering")
        main = _(f"Hi {display_name},\n\nWe are thrilled to have you on board as a volunteer for Plastic removal event!\n\nThank you for generously offering your time and effort to help make this event a success. Your support is invaluable, and we couldn’t do it without dedicated volunteers like you.\nHere’s what you can expect next:\n\nVolunteer Orientation: Join us for a brief orientation on {orientation_date} at 21:00 to go over your role and responsibilities.\nEvent Day Details: Location: {volunteer_location}\nDate:{volunteer_date}\nTime:10:00.\n\nStay Connected: We’ll keep you updated with any additional information or changes via email, so please keep an eye on your inbox.\n\nQuick Checklist:\n\nComplete Your Registration: If you haven’t already.\nMark Your Calendar: Add the event and orientation dates to your calendar to ensure you don’t miss any important details.\nSpread the Word: Feel free to invite friends and family to join us. More volunteers always make for a merrier event!\n\nIf you have any questions or need further information, don’t hesitate to reach out to us.\n\nOnce again, thank you for your willingness to volunteer. Your participation will help us create an unforgettable experience at Plastic removal event.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [user_mail],
        fail_silently=False,
    )
        return redirect('/home')
    else:
        template = loader.get_template('volunteer/sea.html')
        return HttpResponse(template.render(c,request))

@login_required(login_url="/login/")
def tree(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    tree_event = VolunteerEvents.objects.get(event_id="#00134233")
    members = int(tree_event.no_of_signed)
    user_tier = user_data.user_tier
    user_mail = user_data.user_email
    volunteer_date = tree_event.event_date
    volunteer_location = tree_event.event_location
    orientation_date = tree_event.orientation_date
    event_organiser = tree_event.event_organiser
    event_id ="#00134233"
    event_title = tree_event.event_name
    event_url = tree_event.event_url
    user_events = UserEvent.objects.filter(user=request.user,title =event_title)


    events_attended = int(user_data.events_attended)
    c = {
         "user_tier":user_tier,
         "user_events":user_events,
         "volunteer_location":volunteer_location,
         "volunteer_date":volunteer_date,
         "event_organiser":event_organiser,
         "members":members}
    if request.method == 'POST' and 'delete' in request.POST:
        no = members-1
        no2 = events_attended-1
        user_data.events_attended = str(no2)
        tree_event.no_of_signed = str(no)
        user_data.save()
        tree_event.save()
        user_events.delete()


    if request.method == 'POST' and 'add' in request.POST:
        display_name = request.POST.get('name')
        no = members+1
        no2 = events_attended+1
        user_data.events_attended = str(no2)
        tree_event.no_of_signed = str(no)
        user_data.save()
        eve = UserEvent.objects.create(user = request.user,name = request.user.username,title = event_title,event_id = event_id,start_date = volunteer_date,location = volunteer_location,organiser = event_organiser,eventurl = event_url)

        tree_event.save()

        head = _("Thanks for volunteering")
        main = _(f"Hi {display_name},\n\nWe are thrilled to have you on board as a volunteer for Plastic removal event!\n\nThank you for generously offering your time and effort to help make this event a success. Your support is invaluable, and we couldn’t do it without dedicated volunteers like you.\nHere’s what you can expect next:\n\nVolunteer Orientation: Join us for a brief orientation on {orientation_date} at 21:00 to go over your role and responsibilities.\nEvent Day Details: Location: {volunteer_location}\nDate:{volunteer_date}\nTime:10:00.\n\nStay Connected: We’ll keep you updated with any additional information or changes via email, so please keep an eye on your inbox.\n\nQuick Checklist:\n\nComplete Your Registration: If you haven’t already.\nMark Your Calendar: Add the event and orientation dates to your calendar to ensure you don’t miss any important details.\nSpread the Word: Feel free to invite friends and family to join us. More volunteers always make for a merrier event!\n\nIf you have any questions or need further information, don’t hesitate to reach out to us.\n\nOnce again, thank you for your willingness to volunteer. Your participation will help us create an unforgettable experience at Plastic removal event.\n\nBest regards,\n\nImaadu Tawiah\nVerdeia")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [user_mail],
        fail_silently=False,
    )
        return redirect('/home')
    else:
        template = loader.get_template('volunteer/tree.html')
        return HttpResponse(template.render(c,request))

def organise(request):
    user_data = UserData.objects.get(user_username=request.user.username)
    user_tier = user_data.user_tier
    c = {
         "user_tier":user_tier}
    if request.method == 'POST':
        user_name = request.POST.get('fname')
        user_mail = request.POST.get("mail")
        event_address = request.POST.get("address")
        event_title = request.POST.get("title")
        event_details = request.POST.get("details")
        event_country = request.POST.get("country")
        event_date = request.POST.get("date")

        head = _("Thank You for Organizing an Event with Us!",
)
        main = _(f"Hi {user_name},\n\nWe are thrilled and grateful for your initiative to organize an event with us at Verdeia.\n\nYour enthusiasm and commitment to this event are truly inspiring. It's individuals like you who drive meaningful change and help us achieve our mission.\nWhat’s Next:\n\nInitial Planning: Our team will be reaching out to you shortly to discuss the details and next steps. We want to ensure we provide you with all the support and resources you need.\nCollaboration: We believe in the power of collaboration and are excited to work closely with you to bring this event to life. Your vision and ideas are invaluable to us.\nSupport and Resources: We will provide you with the necessary tools, materials, and guidance to help make your event a success.\n\nIf you have any immediate questions or need assistance, please don’t hesitate to reach out to us.\n\nThank you once again for your dedication and effort in organizing this event. Together, we can create an impactful and memorable experience for everyone involved.\n\nBest regards,\n\nImaad Tawiah\n Verdeia")
        send_mail(
head,main,
        "hello@verdeia.xyz",
        [user_mail],
        fail_silently=False,
    )
        send_mail(
            "User suggest event",
            f"Event title: {event_title}\n\nEvent message: {event_details},\n\nEvent_address: {event_address}\n\n Event date: {event_date}\n\n user_name: {user_name}\n\nuser_mail: {user_mail}\n\nEvent country: {event_country}",
            "hello@verdeia.xyz",
            ["hello@verdeia.xyz"],
            fail_silently=False,
        )
        return redirect('/home')
    else:
        template = loader.get_template('volunteer/organise.html')
        return HttpResponse(template.render(c,request))