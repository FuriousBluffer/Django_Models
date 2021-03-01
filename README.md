### How model maps a class to a database?
- ORM --> Object Relational Mapper
  - Takes a python object and auto converts to the database language.
  - Gives you the freedom to use any database
  - Class --> Table
  - Field --> Column
  - Class Obj --> Row
    
 - After you have initialised model(s), you need to migrate those to the database schema.

### How to migrate the model to a database language?
 - Run the command in using manage.py utils:
> makemigrations
 - And after running the above command, run this:
> migrate

### What's the difference between migrate and makemigrations?
 - makemigrations --> It creates a script in respect of the changes made to models.py (SQL)
 - migrate --> Runs the script

### .save() is used to add a row in the database.



### Register your models in the admin.py to use them:
 > from django.contrib import admin
 > from trello_app import models
 > # Register your models here.
 > admin.site.register(models.Task)
 > admin.site.register(models.TaskList)