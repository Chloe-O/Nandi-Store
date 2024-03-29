# Nandi Store

For this project I have created an E-commerce store which focuses on selling houseplants, users can visit the site and purchase different houseplants as a registered user or guest. 

[Link to my deployed site on Heroku](https://nandi-store.herokuapp.com/)

![Screenshot of site's Index page](https://nandi-store.s3.eu-west-2.amazonaws.com/media/store_index.JPG)

---

# User Experience (UX)

## User Stories

### First Time Visitor Goals
1. Upon first visiting the site, I want to understand what the site is for
2. Easily navigate through the site
3. Quickly create a user account if I think I will use the site again for future purchases
4. Easily make purchases with or without being a registered user
5. Clearly find products for sale and find more information about these before adding to my basket
6. Search for a particular product or only view products of a particular category
7. Sort products by category, price and ratings

### Registered User Goals
1. Easily log in and out of my account
2. Reset my password if I forget it
3. Save my preferred delivery information on my profile for quicker, more convenient checkout
4. View details of my past orders
5. Receive a verification email when creating my account for extra security
6. Receive confirmation that my order has been successful after checkout
7. Be confident that the payment method used is secure
8. Sort products by category, price and ratings
9. Search for a particular product or only view products of a particular category

### Guest User Goals
1. Easily checkout without need to create an account
2. Make a purchase by inputting my delivery information at the checkout
3. Receive confirmation that my order has been successful after checkout
4. Be confident that the payment method used is secure
5. Sort products by category, price and ratings

### Admin/Owner Goals
1. Feel confident a user can easily navigate the site to make purchases
2. Easily add, edit or delete items to/from the store
4. Allow users who do not wish to create an account to also make purchases through the site
5. Make users aware and remind them that they can qualify for free shipping if they spend £25.00+ - this encourages users to spend more to take advantage of free shipping offer

---

## Design

- Jinja templating used to create a 'base.html' template which helps keep consistency across the site's pages i.e. Header is rendered the same on all pages as the same code is injected on all pages
- The site has a simple design to allow a user to easily understand how to navigate through the site and made purchases

## Colour Scheme

- The colour scheme is white, black, yellow and green
- Where Bootstrap's colour classes have been used e.g. warning yellow for the banner underneath the nav bar or on the bag page to tell a user they only need to spend so much to qualify for free shipping catches the attention of the user but is not used so much to draw away from the rest of the site

## Typography

- Lato from Google Fonts is the font used throughout the site

## Imagery

- I used Pexels and Pixabay to find images related to my site i.e. plant images and jumbotron index image
- I have edited some of the photos using Windows Photo editor

## Wireframes

- [Link to wireframes](https://nandi-store.s3.eu-west-2.amazonaws.com/media/ms4_wireframes.pdf)

# Technologies Used

## Languages, frameworks and services used for this site:

- [JavaScript](https://www.javascript.com/)
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Python](https://www.python.org/)
- [Bootstrap v5](https://getbootstrap.com/)
- [Django](https://www.djangoproject.com/)
- [JQuery](https://jquery.com/)
- [GitHub](https://github.com/)
- [Stripe](https://stripe.com/gb)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)



## Libraries & Programs Used

1. [Google Fonts:](https://fonts.google.com/)
   - Google fonts were used to import font
2. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used for icons that appear on the site
3. [GitHub:](https://github.com/)
   - GitHub was used to store the project and version control
4. [Balsamiq:](https://balsamiq.com/)
   - Balsamiq was used to create the wireframes for the site
5. [Heroku:](https://www.heroku.com/)
   - Heroku was used to deploy the site
6. [Amazon Web Services - AWS](https://aws.amazon.com/)
   - AWS used for hosting static files e.g. images, css
7. [GitPod](https://www.gitpod.io/)
  - IDE
8. [PostgresSQL](https://www.postgresql.org/)
  - Database functionality provided by Heroku
9. [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)


---

# Authentication

- Authentication is provided by Django's Allauth, this provides templates for user actions such as login/register/email verifications etc.
- Built in security features e.g. a user cannot create an account using a password that is similar to their username or password

# Features

__Index__
1. Users can easily navigate to other pages on the site using the navigation bar, user can also go straight to products by clicking 'SHOP NOW'

__Products__
1. Products are clearly displayed using Bootstrap cards, this includes an image of the item, name, rating and price
2. Users can sort items by category, price, rating

__Product details__
1. Shows larger image of item and provides description of item
2. Buttons allow user to add item to bag or go back to all products

__Profile__
1. Users with a registered account can view any previous orders and their default delivery/billing info from the profile page

__Bag__
1. User can view items in their bag or will be told their bag is empty
2. User will be able to view items with quantity, price per unit and sub-total
3. Total cost is displayed with cost of delivery(if applicable)
4. User can navigate to the checkout from here to complete purchase

__Checkout__
1. User is shown total cost to pay and items they are purchasing
2. Users with account who have provided delivery/billing info will have the form populated. Otherwise, the user will have to manually input this
3. User is made aware whether purchase has been successful or not
4. User can proceed without filling out all the required fields

__Admin/Owner__
1. Admin can add new items
2. By navigating to the products page, admin can edit or delete existing products

---

# Testing

## Code Validation

The W3C Markup Validator and W3C CSS Validator Services were used to validate the project as well as pep8online.com. Some errors are present, particularly with Python code, though these cannot be rectified or would break the code.

### HTML

- I validated the HTML using the deployed site's URL
- This did thrown an error regarding information held in the meta tags in my base template, I have ignored these as this is consistent with the material in the Boutique ado tutorial

![HTML](https://nandi-store.s3.eu-west-2.amazonaws.com/media/html_validation.png)

---

### CSS

#### Base CSS
![CSS](https://nandi-store.s3.eu-west-2.amazonaws.com/media/base_css_validation.jpg)

#### Checkout CSS
![CSS](https://nandi-store.s3.eu-west-2.amazonaws.com/media/checkout_css_validation.jpg)
---

## Python

For 'line too long' errors, I opted not to change these as found breaking up the string caused the code to break - as they are, they do not cause any issues with the running of the code. I did not include the screenshots of these validations due to the amount of python files that needed to be check, I have noted any errors experienced below:

- views.py in bag app throws a 'line too long' error - however I cannot change this as the string of text becomes broken if I try to split it over more than 2 lines
- models.py in checkout app gives an 'continuation line under-indented for visual indent', this cannot be changed or will break the string
- models.py in checkout app also gives a 'line too long' error - again, this cannot be changed
- webhook_handler.py in checkout app throws 2 'line too long' errors
- webhooks.py in checkout throws a 'line too long' error
- settings.py in nandi_store app throws 4 'line too long' errors
- urls.py and widgets.py in product app throws a 'line too long' error

---

### JavaScript

I used JSHint.com to validate any Javascript. Unfortunately, JSHint does not recognise Jquery syntax so any Jquery code produced an 'undefined variable' error. 

Other than this, there were no errors in the Javascript.

## Testing User Stories from User Experience (UX) Section and Testing

I have completed testing in line with user and owner goals

### First Time Visitor Goals
1. Upon first visiting the site, I want to understand what the site is for
  - Users can quickly navigate to the store using the navigation bar and find the site sells houseplants
2. Easily navigate through the site
 - The user can navigate through the site using the navigate bar, search bar or buttons throughout the site
3. Quickly create a user account if I think I will use the site again for future purchases
  - Navigation bar features the option to log in or register
4. Easily make purchases with or without being a registered user
  - Users who do not wish to create an account can still navigate through the site and make purchases but do not have access to a profile page. If the a guest user tries to navigate to the profile page, they will be prompted to log in
5. Clearly find products for sale and find more information about these before adding to my basket
 - On the products page, users can click on items for more information about a particular product
6. Search for a particular product or only view products of a particular category
 - Users can user the search bar to search for a particular keyword(s)
 - On the products pages, a user can filter products by category using the dropdown
7. Sort products by category, price and ratings
 - Users can sort products by category, price or rating using the dropdown on the products page

### Registered User Goals
1. Easily log in and out of my account
  - Using the navigation bar, a user can easily log in or out of their account
2. Reset my password if I forget it
  - If a user forgets their password, they can choose the 'forgot my password' link and they will be sent an email with a link to reset their password
3. Save my preferred delivery information on my profile for quicker, more convenient checkout
  - On the profile page, a registered user can input their address and save this. When purchasing, this information will be pre-filled on the checkout page
4. View details of my past orders
  - When navigating to the profile page, any past orders will be displayed. A user can click on each order to get more information about it such as items order, order date/time & billing address
5. Receive a verification email when creating my account for extra security
  - The user will receive a verification email upon registering an account, they will need to follow the link in the email to verify their account
6. Receive confirmation that my order has been successful after checkout
  - The user should receive an email following a successful order confirming this success *this feature currently does not work and user receives no email* 
7. Be confident that the payment method used is secure
   - Stripe is used to handle payments, this is a secure payment service
8. Sort products by category, price and ratings
 - Users can sort products by category, price or rating using the dropdown on the products page
9. Search for a particular product or only view products of a particular category
 - Users can user the search bar to search for a particular keyword(s)
 - On the products pages, a user can filter products by category using the dropdown

### Guest User Goals
1. Easily checkout without need to create an account
  - User does not need an account to make a purchase and can make an order as a guest
2. Make a purchase by inputting my delivery information at the checkout
 - When reaching checkout, the user will have to input relevant contact and delivery information to make the order
3. Receive confirmation that my order has been successful after checkout
  - The user should receive an email following a successful order confirming this success *this feature currently does not work and user receives no email* 
4. Be confident that the payment method used is secure
   - Stripe is used to handle payments, this is a secure payment service
5. Sort products by category, price and ratings
 - Users can sort products by category, price or rating using the dropdown on the products page

### Admin/Owner Goals
1. Feel confident a user can easily navigate the site to make purchases
  - Navigation bar makes it easy to get around the site as is clear and present on each page
2. Easily add, edit or delete items to/from the store
  - Using the manage products link, admin/owner can add new products including their names, description, price, rating and image
  - On the products page, the admin/owner can opt to edit an existing item or delete it all together
4. Allow users who do not wish to create an account to also make purchases through the site
 - Users are not obligated to create an account to make a purchase so admin/owner can be confident if any user wishes to make a purchase, they can
5. Make users aware and remind them that they can qualify for free shipping if they spend £25.00+ - this encourages users to spend more to take advantage of free shipping offer
- The banner runs along the underside of the navigation bar reminding users that order over £25.00 qualify for free shipping
- When viewing their bag, the user is told how much extra they would need to spend to get free shipping if their order does not exceed £25.00(or told shipping is £0.00 if order is equal to or exceeds £25.00)
 - This encourages users to 'top up' their order and spend more if it falls below the threshold

---

# Bugs/Known Issues

### * *Due to time constraints and not being able to obtain an extension, unfortuntely the site does remain unfinished at present and I have not been able to go outside the scope of the course material* *

- I have not been able to add the required additional apps due to not having sufficient time to add these
- Toasts when carrying out actions (i.e. adding items to bag) are not visible on the page
- Order summaries show as '£0.00' despite items having different costs but when paying order sum is correct(also shows correct payment amount on Stripe)
- Footer on Profile and Checkout Success pages do not span the entire width of the viewport
- Spinner colour when payment is processing is not opaque despite using RGB colour with opacity
- Users do not receive a confirmation email when making an order but receive all other email instances i.e. forgot password, verify email etc.
- Image formatting on products page is not consistent

# Resolved Issues

- I encountered a bug early on where clicking the link to the index page did not work could not find template, I discovered this was because I was using 'index' instead 'home' in my href url
- Delivery threshold was no displaying on base.html - I realised this was because 'FREE_DELIVERY_THRESHOLD' was written in caps, once I changed this to lowercase this resolved the issue
- When deploying to Heroku the index image did not display, I provided the url to this image from my AWS bucket which resolved this

---

# Deployment

In order to deploy the site, Github, AWS and Heroku were used.

## Github & Gitpod

1. I created a repository for the project on GitHub, using Gitpod I was able to use the green 'Gitpod' button to open the project in a Gitpod workspace and work on the project from here - commits and pushes were actioned using the source control tab in Gitpod
2. To clone the repository, a user can clone the repo use the 'code' button in the repo. From here the repo can be cloned using HTTPS or GitHub CLI. Alternatively, a user can clone the repo locally by selecting the 'Open with GitHub Desktop' option, this will produce a prompt for GitHub Desktop to open - more information about cloning a repository can be found [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
3. When running locally, all the relevant dependencies will need to be installed using pip, in the IDE's terminal type:
   > pip3 install -r requirements.txt
4. Create a Procfile, this will allow Heroku to understand the type of app we are running, the following should be input to the Procfile:
   > web: gunicorn nandi_store.wsgi:application

---

## Heroku

1. Create a Heroku account or log in if you already have an account
2. Create a new app in Heroku and select your region or closet region, for me this was Europe, I am based in the UK
3. Navigate to 'Resources' and provision a Heroku Postgres database, using the free plan here is fine
4. In GitPod install dj_database_url and psycopg2-binary using the pip3 install command in the terminal
5. Install requirements using
  > pip3 freeze > requirements.txt
6. Import dj_database_url in project level settings.py
7. Comment out the current DATABASE settings(these will be required later) 
8. Obtain DATABASE_URL from Heroku Key Vars, type the following into DATABASE settings 
  > 'default': dj_database_url.parse(*DATABASE URL GOES HERE*)
9. Run migrations by using
  > python3 manage.py migrate
10. If you do not already have a superuser account, you can create one using the following command and following prompts in the terminal
  > python3 manage.py createsuperuser
11. In settings.py uncomment the previously commented out DATABASE settings and update this using an if statement - the app will run on Heroku but can 'fall back' on SQL if needed
12. Install gunicorn using:
  > pip3 install gunicorn
13. Again, freeze requirements using:
  > pip3 freeze > requirements.txt
14. Create Procfile and input the following to allow Heroku to understand how to run the project:
  > web: gunicorn nandi_store.wsgi:application
15. Login to Heroki using the terminal by typing and following terminal prompts
  > heroku login -i
16. We do not want Heroku to collect static files so must disable this for now using(--app nandi-store is only requirement if you have one than one app):
  > heroku config:set DISABLE_COLLECTSTATIC=1 --app nandi-store
17. Back in settings.py we need to change ALLOWED_HOSTS to, to allow Heroku app to run but also to allow us to still access it via GitPod:
  > ALLOWED_HOSTS = ['nandi-store.herokuapp.com', 'localhost']
18. Copy Environment Variables from GitPod into Heroku's Config Vars which can be found in settings

---

### Deploying in Heroku

1. Using GitPod Heroku needs to be initialised, in the terminal input:
  > git remote: heroku git:remote -a nandi-store
2. Push to Heroku Master using:
  > git push heroku master
3. In the Heroku Overview you will be able to see Heroku building the app - the site is now live
4. Once Heroku has finished the build, we can link our Git repo to Heroku for automatic deployment which means any changes to the repo will automatically be pushed to the Heroku branch and live site will reflect and changes - In the Deploy tab, click 'GitPod' in Deployment methods and search for the relevant repo and connect
5. Finally, tick the option to allow automatic deploys
6. The app can be launced using the'Open App' button towards the top of the screen

---

## AWS

AWS is used to host the static files needed for our project.

1. Visit AWS website and log in or register as a new user if you've no account
2. Create a new bucket by:
  * Name your AWS - in this case 'nandi-store'
  * Select region closest to you - based in UK this was (EU(London) EU-west-2)
  * Uncheck access box to allow access for public - anyone will be able to access the bucket
  * Click 'Create Bucket'
  * Navigate to 'Properties' and enable Static Website Hosting
  * Navigate to 'Permissions' CORS and add the below into the input field:
  > [
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
3. Navigate to 'Bucket Policy' and select Policy Generator to create a security policy - select 'S3 Bucket Policy' Add * to Principle which will alow all principals
  * Navigate to 'Action' and copy the ARN, paste this into the Edit Bucket Policy field and add /* to so all resources can be accessed in the bucket
    > "nandi-store/*"
  * Navigate to 'Access Control List' - under Everyone(Public Access) select List then save changes
4. To create a user we will need to begin by creating a group by:
  * Navigate to the service IAM(Identity and Access Management) 
  * Create a new group - in this case 'manage-nandi-store'
  * Click next step again, a second time, we don'y have a policy to attach to the group as of yet
  * Navigate to 'Policies' and click Create Policy
  * Under JSON tab select 'Import Managed Policy' From here we can import a policy - AWS offers policies, so we can use their 'AmazonS3FullPolicy' - import this
  * Back in S3, under our bucket copy your ARN
  * In IAM update Resource item and copy your ARN using the following pattern:
    > "arn:aws:s3:::magnetic-eyes"
      "arn:aws:s3:::magnetic-eyes/*"
  * Review Policy
  * Choose a name and descripton for the policy and click Create Policy
  * Navigate to Groups, select your Group and navigate to Permissons then Attach Policy 
  * Find your newly created policy and attach it to the Group
5. We will need to create a user to add to the Group - Navigate to Users under the IAM service tab and select 'Add User'
  * Allow Programmatic Acces and click Next
  * Add new user to group
  * Click through next until you are given the option to click Create User
  * Download the CSV which will contain the user credentials - ensure this is kept safe as it cannot be downloaded again
6. Next, we will need to connect our AWS bucket to Django, begin by installing boto3 & django-storages using the IDE terminal:
  > pip3 install boto3
  > pip3 install django-storages
  * Freeze requirements using:
  > pip3 freeze > requirements.txt
7. Add 'storages' to installed apps on settings.py
  * Add the following to settings.py which allows communication between our project/Heroku and AWS:
 ![AWS Bucket Config](https://nandi-store.s3.eu-west-2.amazonaws.com/media/aws_bucket_config.jpg)
  * Back in Heroku we need to add the following AWS config vars which will be the credentials found in the csv file from AWS:
  > AWS_ACCESS_KEY_ID - *input key from csv file*
  > AWS_SECRET_ACCESS_KEY -  *input key from csv file*
  > USE_AWS - True
  * Delete the collectstatic config variable as we no longer require this
8. In settings.py add:
  >  AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
9. Create a file called 'customer_storages.py', this will need to contain the following: 
  > from django.conf import settings
  > from storages.backends.s3boto3 import S3Boto3Storage

  > class StaticStorage(S3Boto3Storage):
  > location = settings.STATICFILES_LOCATION

  > class MediaStorage(S3Boto3Storage):
  > location = settings.MEDIAFILES_LOCATION
10. As per the code in the screenshot above, our project now knows where to find our AWS static files
  * The cache control tells the browser to cache static files for a long time which causes minimal disruption for the user
11. Static files(images, JS & CSS) will need to be downloaded from GitPod if not stored locally then uploaded to your AWS bucket

## Stripe

1. Take the Stripe keys from the config variables in GitPod settings, these are as follows:
  > STRIPE_PUBLIC_KEY
  > STRIPE_SECRET_KEY
  > STRIPE_WH_SECRET *This is obtained from the developer section of the Stripe website
2. Add these variables to Heroku config vars
3. Back in the developer section of Stripe website, add a new endpoint, opt to receive all events then add the endpoint
4. Reveal signing secret, replace STRIPE_WH_SECRET config var with this



---

# Credit

- [Django Allauth Docs](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [W3Schools](https://www.w3schools.com/howto/howto_css_hero_image.asp) Hero image
- Boutique Ado tutorial
- [The Little Botanical](https://thelittlebotanical.com) information about different houseplants

# Image Credits

- [Header Image](https://www.pexels.com/@cottonbro) Cottonbro @ Pexels
- [Aloe Vera Image](https://www.pexels.com/@cisiq) Cintia Siqueira @ Pexels
- [Crassula Image](https://www.pexels.com/@harry-cooke) Harry Cooke @ Pexels
- [Heart Cactus Image](https://pixabay.com/users/chloelindaphotographe-9286470/) Chloe Linda @ Pixabay
- [Test plant image](https://www.pexels.com/@huy-phan-316220) Huy Phan @ Pexels
- [Aloe Vera Info](https://en.wikipedia.org/wiki/Aloe_vera) Wikipedia
- [Crassula Info](https://en.wikipedia.org/wiki/Crassula) Wikipedia
- [Heart Cactus Info](https://en.wikipedia.org/wiki/Hoya_kerrii) Wikipedia
- [Noimage Image](https://github.com/ckz8780/boutique_ado_v1/blob/dependabot/pip/django-3.0.7/media/noimage.png) Code Institute boutique_ado_v1 project
