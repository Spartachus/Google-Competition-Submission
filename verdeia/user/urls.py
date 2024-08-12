
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home_view, name='home'),]

urlpatterns = [ 
    path('', views.home_view, name='home'),
    path('login/', views.login, name="login"),
    path('unavailable/', views.unavailable, name="unavailable"),    
    path('signup/', views.signup, name="signup"),
    path('getstarted/', views.gettingstarted, name="gettingstarted"),
    #misc urls
    path('privacypolicy/', views.privacy, name="privacy"),
    path('terms/', views.termsconditions, name="termsconditions"),
    path('contact/', views.contact, name="contact"),
    path('000/', views.unavailable, name="unavailable"),
    path('faq/', views.faq, name="faq"),
    path('pricing/', views.pricing, name="pricing"),
    #user urls
    path('home/', views.loggedin, name="userlogged"),
    path('projects/', views.projects, name="projects"),
    path('events/', views.events, name="events"),
    #path('goals/', views.goals, name="goals"),
    path('askgaia/', views.askgaia, name="askgaia"),
    path('profile/', views.profile, name="profile"),
    path('profile/update/', views.updateprofile, name="update_profile"),
    path('start/', views.start, name="start"),
    path('update', views.update_track, name="update_track"),
    #user projects
    path('projects/plant', views.planting, name="plant"),
    path('projects/fog', views.fog, name="fog"),
    path('projects/solar', views.solar, name="solar"),
    path('projects/capture', views.capcha, name="capture"),
    #user volunteer
    path('volunteer/plastic', views.plastic, name="plastic"),
    path('volunteer/sea', views.sea, name="sea"),
    path('volunteer/tree', views.tree, name="tree"),
    path('volunteer/organise', views.organise, name="organise"),
    #Blogs
    path('blog/', views.blog, name="blog"),
    path('blog/understanding-your-carbon-footprint', views.blog_1, name="blog_1"),
    path('blog/10-simple-ways', views.blog_2, name="blog_2"),
    path('blog/importance-of-carbon-ofsetting', views.blog_3, name="blog_3"),
    path('blog/top-renewable-energy-sources', views.blog_4, name="blog_4"),
    path('blog/guide-to-carbon-certificate', views.blog_6, name="blog_6"),
    path('blog/corporate-social-responsibility', views.blog_5, name="blog_5"),
    #test user
    path('test/', views.test, name="test"),

]

if settings.DEBUG:
    # do not do this in prod
    from django.conf.urls.static import static
    # Try Django
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)