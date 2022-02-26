# RentUments website using Django

## Intro

This project was realised in the span of two weeks. While doing it I've learned a lot of HTML and CSS, inline attributes and styling, margins/paddings/borders, forms and other stuff. It was very interesting to realise a project for the first time even such basic one. 

For every component of a website a different git branch was created, i. e. for footer I used a 'footer' branch, for navbar - 'navbar' and so on. It was my first serious project where I've used a lot of git branches, did a bunch of checkouts, different merges and so on.

## Accessing the website

1. Install [Python](https://www.python.org/downloads/);
2. Install Django: in console type (make sure you have PIP in your PATH variable) `pip install Django`;
3. Copy the contents of the repository to your working directory;
4. Run in console `python %location_of_your_directory%/manage.py runserver`
5. If everything goes correctly you should see the line "Starting development server at http://127.0.0.1:8000/"
6. Open your browser and enter the url given in the previous line.

### Guide

#### Navbar

On the top you can see a logo I made in PhotoShop in 5 minutes, font is [WarCraft](https://ru.ffonts.net/warcraft.font). The navbar buttons are all clickable: 
- Home - to homepage;
- About - to this text;
- Products - to catalogue of items;
    - The buttons in the middle don't work except for 'Go to all products';
        - Here you can click on any product that is in database, the site realises dynamic routing (you can also add items to database but more on that later);
        - After clicking on the item you can get back to the list of all items or delete the chosen product;
        - If you decide to delete the product, you will be asked for confirmation of the action. This deletes the product from the database.
- Contact Us - this page containts the contact form and links (not-working) to possible questions. The form doesn't actually send anything. This page was more of a training ground where I trained CSS and HTML attributes;
- Cart - not realised;
- Login - leads to working login page.

#### All urls

Click on any of the links to go to any working html file that was created.
**Note:** You must create a superuser before accessing admin page (base django admin page).

#### Footer

Only the 'Contacts' page is intact with all the links there working as intended.

At the bottom are my contacts.


### Django side of the project

**'base.html':** The fundamental file which has links to CSS, logo, \<head> information. 
In order to use it as a template, every html page should have **{% extends 'base.html' %}** tag in the beginning. This file has 2 django **{% block %}** tags which have content that, if replaced in the 'child' files, will show the replaced information, otherwise it will show the original contents that are in 'base.html'. You can see these blocks on 'home', 'cart' pages
**Note:** Because the 'All urls' is not in any **{% block %}** tag, it is not replaced in any html file and just loads from 'base.html'.
It has 2 **{% include %}** tags that load 'navbar.html' and 'footer.html'. 
**{% load static %}** in the beginning is used to load the static files (images, CSS).

### Adding stuff to database

You can add files to database using 2 methods:
1. via the admin page after creating superuser (I'll write down the process in the end);
2. via the 'create' page using the form. You don't have to login in order to do it (sadly, I didn't have time to realise this feature).

### Creating a user and accessing admin page

In your console run `python %location_of_your_directory%/manage.py createsuperuser` then enter any username, email (not required), password. Now you can login via the 'Login' page in navbar or 'admin' url in the main body of the site.

## Thank you for trying out my project!
[Telegram](t.me/SXRU1)
