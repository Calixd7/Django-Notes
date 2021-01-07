# Notes app

This project is your first Django project! It is intentionally simple. By the end of it, you will have created an application that can store, search, and filter notes.

You will work on this over the span of a week with daily instructions.

## Day 1

Today, you are learning how to create a new Django project and working with views and templates. You need to:

* Create a new Django project.
* Create an app inside that project called `notes`.
* Create a view called `notes_list` to show you the list of all your notes in `notes/views.py` and link this view to the root URL. Create a template for this view.
* Create a view called `notes_detail` to show you all the information about a single note in `notes/views.py` and link this view to `/notes/<pk>`. Create a template for this view.
* Extract the common pieces of your templates and use template inheritance to make a `base.html` template that both your notes view and notes detail templates inherit from.

### Your notes

Your notes are stored in a dictionary that you should put in `notes/data.py`. Here is some sample data.

```py

NOTES = {
  "1": {
    "title": "Optional background definition",
    "body": """Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh."""
  },
  "2": {
    "title": "Reverse-engineered multimedia utilisation",
    "body": """Curabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem. 
    
    Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat. Praesent blandit. Nam nulla."""
  },
  "3": {
    "title": "Optional object-oriented open architecture",
    "body": "Maecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti. Nullam porttitor lacus at turpis."
  },
  "4": {
    "title": "Down-sized system-worthy extranet",
    "body": """Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede. 
    
    - Morbi porttitor lorem id ligula. 
    - Suspendisse ornare consequat lectus. 
    - In est risus, auctor sed, tristique in, tempus sit amet, sem. 
    - Fusce consequat. Nulla nisl. Nunc nisl.
    """
  },
  "5": {
    "title": "Customizable zero tolerance array",
    "body": """In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem. Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy. 
    
    **Integer** non velit. Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque. Duis bibendum."""
  },
  "6": {
    "title": "Networked stable customer loyalty",
    "body": "Suspendisse potenti. Cras in purus eu magna vulputate luctus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
  }
}
```

### Stretch goals

Add the ability to render your notes as Markdown.

## Day 2

Today, you are learning the basics of models and the admin. You need to:

* Create a `Note` model with a required title and body. This should also contain a `created_at` and `updated_at` field that are auto-populated when the note is created and updated.
* Make migrations for your `Note` model and run those migrations.
* Make an admin interface for your `Note` model.
* Add some notes to your database through the admin interface.
* Migrate your views and templates to use your `Note` model instead of `NOTES` from `notes/data.py`.

## Day 3

Today, you are learning about forms and handling POST requests. You need to:

* Create a `NoteForm` that uses `forms.ModelForm` to handle note data.
* Add the ability to create a note through your site (instead of through the admin). This will require another view and URL.
* Add the ability to edit a note through your site. This will require another view and URL.

## Day 4

Today you are wrapping up your Django tutorial week. You need to:

* Add the ability to delete a note.
* Add the ability to search notes and get back a list of notes that match your search text (case-insensitive).
* Add the ability to sort your notes by title or by updated at (descending or ascending).

## Stretch yourself!

If you finish all of the above, what could you do to improve your application? 

* You could add more CSS to make it stylish.
* You could add some JavaScript to enhance your experience. 
* You could add the ability to create multiple notes at once.
* You could add the ability to render your notes as Markdown.
* You could add comments for notes.
