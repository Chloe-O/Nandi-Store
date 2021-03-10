# Nandi Store

For this project, I have used HTML, CSS, Python(using Flask framework). The small amount of JavaScript has been handled by Bootstrap using a Jquery CDN. 

[Link to my deployed site on Heroku]()

![Screenshot of site's Index page]()

---

# User Experience (UX)

The purpose of my site is 

## User Stories

## First Time Visitor Goals



## Returning Time Visitor Goals & Frequent Time Visitor Goals



## Design

 - Jinja templating used to create a 'base.html' template which helps keep consistency across the site's pages

## Colour Scheme

- The colour scheme is

## Typography

- Lato from Google Fonts is the font used throughout the site

## Imagery

- I used Pexels to find images related to my site i.e. photos of food
- I have edited the photos....

## Wireframes

- [Link to wireframes]()

# Technologies Used

Languages used for this site:

- [JavaScript](https://www.javascript.com/)
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Python](https://www.python.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Jinja](https://jinja.palletsprojects.com/)

## Frameworks, Libraries & Programs Used

1. [Google Fonts:](https://fonts.google.com/)
   - Google fonts were used to import the Roboto font 
2. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used for icons that appear on the site
3. [GitHub:](https://github.com/)
   - GitHub was used to store the project and version control
4. [Balsamiq:](https://balsamiq.com/)
   - Balsamiq was used to create the wireframes for the site
5. [Heroku:](https://www.heroku.com/)
   - Heroku was used to deploy the site

---

# Features

- A user can 

# Data Structure

- 

---

# Testing

## Code Validation

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no errors in the project and the Python code is PEP8 compliant.

### HTML

- I validated the HTML using the deployed site's URL

![HTML]()

---

### CSS

![CSS]()

---

### JavaScript

![Python]()
---

### JavaScript

![CSS]()


## Testing User Stories from User Experience (UX) Section and Testing

I have completed testing alongside visitor goals

## First Time Visitor Goals

- I want to understand the purpose of the site within a short time of visiting the site by the images and description on the landing page
  - The site is quite minimal and clearly laid out, it is easy for a user to user the purpose of and navigate through the site
   1. When navigating through the site, using the navigation bar or collapsable menu(on smaller display), there are no broken links or misdirects
- I want to easily create an account to make full use of the site
  - A user can click on the 'login/register' page in the navigation bar to log in or register to the site
   1. A user can log in or register an account using a minimum length of 5 characters for their username and password
- I want to add, edit and delete my own recipes
  - A logged in user, can navigate to their own profile page or the recipes page and easily update or delete their recipes
   1. Once a user is logged in or creates an account, they will automatically be redirected to their own profile page
   2. If a user has submitted recipes, these will appear on the user's profile page as well as the all recipes where buttons allow user to select edit or delete
- I want to view recipes submitted by other users
  - Users can navigate to the recipes page to view all submitted recipes including their own
   1. The all recipes page displays all submitted recipes in a Bootstrap accordian
   2. Users not logged in can manually access the recipes page, can view recipes but cannot make any changes
- I want to search the recipe database using keywords, recipe names and by course i.e. Breakfast, Lunch, Dinner
  - Users can use the search function on the recipes page to find recipes - the search function will look at the recipe's name, its category and ingedients and return relevant results if any
    1. User can search for a term and commence the search using the magnifying glass icon or clear the search and 'reset' the page using the refresh icon

## Returning Time Visitor Goals & Frequent Time Visitor Goals

- I want to return to the site and log in
  - Users can easily navigate to the log in page and log in to view recipes
    1. Log in page is easy to find from the index page, user is redirected to profile page upon successful log in
- I want a place to keep a record of my own recipes
  - Once a user creates an account, they can create recipes - these will be submitted to the database where all users can view them but also a user can view them on their own profile page
    1. User can submit/edit recipes, these display on recipe page and profile page
- I want to be able to view my recipes on my own profile page, separate to other user's recipes
  - The user's profile will continue to show recipes only they have submitted
    1. Once submitted, user's recipes will be commited to the database and remain there and display on all recipes and profile pages
- I want to easily add, edit and delete my own recipes
  - From the recipes or profile, a user can easily edit or delete a recipe by opening up the relevant accordian item and clicking edit or delete
    1. Recipes can be deleted using the buttons under the recipes's title in the accordian section
- I want to search the recipe database using keywords, recipe names and by course i.e. Breakfast, Lunch, Dinner
  - Again, users can use the search function on the recipes page to find recipes - the search function will look at the recipe's name, its category and ingedients and return relevant results if any
    1. User can search for a term and commence the search using the magnifying glass icon or clear the search and 'reset' the page using the refresh icon
  - I want to log out when I am finished using the site and clear session data
    1. When logged in, the navigation bar shows a log out option(only viewable by logged in users), clicking this logs the user out and redirects them to the log in page


## Further Testing

- I have used Chrome Developer Tools to understand how the live Heroku app looks on different devices, I've also tested the app on my own Samsung S20+ device
- I have viewed the app in different browsers such as Google Chrome, Samsung Internet, Microsoft Edge and Mozilla Firefox - I noticed the site loads slightly slower on Firefox compared to other browers
- I have tested the site by creating accounts, submitting, editing and deleting recipes to ensure there were no error when carrying out these actions
- I have tested the links on the site to ensure no broken links, social media links in the foot redirect in new tabs so do not lead any from the site

---

# Bugs/Known Issues




# Resolved Issues

 - I encountered a bug early on where clicking the link to the index page did not work and threw a 'xxxxx' error, I discovered this was because I was using 'index' instead 'home' in my href url

---

# Deployment

In order to deploy the site, Github, MongoDB and Heroku were used.

## Github & Gitpod 
1. I created a repository for the project on GitHub, using Gitpod I was able to use the green 'Gitpod' button to open the project in a Gitpod workspace and work on the project from here - commits and pushes were actioned using the source control tab in Gitpod
2. To clone the repository, a user can clone the repo use the 'code' button in the repo. From here the repo can be cloned using HTTPS or GitHub CLI. Alternatively, a user can clone the repo locally by selecting the 'Open with GitHub Desktop' option, this will produce a prompt for GitHub Desktop to open - more information about cloning a repository can be found [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
3. When running locally, all the relevant dependencies will need to be installed using pip, in the IDE's terminal type:
> pip3 install -r requirements.txt
4. Create a Procfile, this will allow Heroku to understand the type of app we are running, the following should be input to the Procfile:
> web: python run.py

---

# Credit

- [Django Allauth Docs](https://django-allauth.readthedocs.io/en/latest/installation.html)



# Image Credit

- [Header Image](https://www.pexels.com/@cottonbro) Cottonbro @ Pexels
- [Noimage Image](https://github.com/ckz8780/boutique_ado_v1/blob/dependabot/pip/django-3.0.7/media/noimage.png) Code Institute boutique_ado_v1 project
