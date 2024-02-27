# ecommerce-website
I am creating a fully functional ecommerce website. Walk with me.

# Steps

**1. Setup Project ✅**

• Create new project 'ecommerce_website' ✅
• Create new app (core) ✅
• Install Apps in Settings.py ✅
• Configure Templates ✅
• Configure Static and Media Files in settings and Urls.py ✅
• Create a new view, urls and template then runserver. ✅
• Configure template inheritance and partials ✅
• Build Frontend ✅
_Comments_
_Building the frontend took longer than i expected since it's really not my strongest suite. I followed a YouTube tutorial to create a fancy ecommerce site and i added some Javascript event listeners for a better user experience. N.B. For now the site isn't responsive and so it should only be used on desktop._

**2. Configure Admin Page, Superuser and Jazzmin  ✅** 

• Install Jazzmin (pip install django-jazzmin) ✅
• Add jazzmin in INSTALLED_APPS ✅
• Add Jazzmin Config Code in Settings.py ✅
• Create Superuser ✅
• Login To Admin Section ✅
_Comments_
_I had never used Jazzmin till this day. Looks way better than the default django dashboard._

**3. Custom User Model ✅**

• Create new app userauths ✅
• Install App in settings.py ✅
• Create custom class User (AbstractUser) : in models.py ✅
• Add AUTH USER MODEL = 'userauths.User' in settings.py ✅
• Comment out django.contrib.admin and admin urls in Setting.py ✅
• Run Makemigrations and Migrate and Uncomments Comments ✅
• Create New Superuser ✅
• Register User model In Admin.py ✅
• Login to admin with email and password ✅
_Comments_
_Ran into a bit of a problem that gave me a tough time. Inconsistent migration history and some other runtime errors. Resetting the migrations solved it._

4. User Register System ✅

• Create new form class UserRegisterForm (UserCreationForm) : in forms.py ✅
• Write view to register def RegisterView (request) : user ✅
• Configure template to show form ✅
• Login to website from Frontend ✅
_Comments_
_Learnt a whole lot here. Adding styling to a django form apparently isn't very direct._

5. User Login System

• Write view to login def LoginView (request) : user
• Configure template to grab input field
• Login to website from Frontend
• Password reset system.

6. User Logout System

• Write view def LogoutView (request) : to Logout a user
• Configure URL
• Test the Feature

7. Alerts In Django

• Copy and Paste CDN Boostrap (version 4)
• Write alert conditional statements

8. Django Context Processor for Template

• Create a new file context_processor.py in core app
• Install In Setting.py TEMPLATES Section List as Icore.context processors.default',
• Now Add Code for Context Processor.

9. Product Model Structure

• Create new Model Class and Add Field for product
• Register Model Classes in Admin

10. List View for Products

• Create Logic to Display only Featured Products in Homepage
• Create New view to List All The Active products from the DB
• Configure Urls.py and Template

11. Category List View

• Create New view to List All active categories.
• Configure Urls.py and Template


12. Product Category List View

• Create New view to List All The Active products from the DB depending on the category selected.
• Configure Urls.py and Template

13. Product Detail View

• Create New view to showcase the Details of a selected Product using pid
• Configure Urls.py and Template

14. Product Rating and Review

• Get all reviews in Product Detail and Lists them out in the template
• Calculate the rating_average for a product
