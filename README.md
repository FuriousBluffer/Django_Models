### How model maps a class to a database?
- ORM --> Object Relational Mapper
  - Takes a python object and auto converts to the database language.
  - Gives you the freedom to use any database
  - Class --> Table
  - Field --> Column
  - Class Obj --> Row
    
### How to migrate the model to a database language?
 - Run the command in using manage.py utils:
> makemigrations
 - And after running the above command, run this:
> migrate

### What's the difference between migrate and makemigrations?
 - makemigrations --> It creates a script in respect of the changes made to models.py (SQL)
 - migrate --> Runs the script

### .save() is used to add a row in the database.