# About:

This aplication is a social media project where the user post photos in a specific place and give recommendations, classify, sugestions, and categorize in a diversity way to other people that never went to the same place, but want a preview about the local.

You can see a preview in the page: http://caarlosaugusto.pythonanywhere.com/

# Running:
To run this application in your local enviroment, you need to install the follow packages:

$ pip install django

#to use password_validation
$ pip install bcrypt

$ pip install django[argon2]

#to use images
$ pip install pillow

#sometimes you can get some error with this command, so you need to use this:
$ pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
