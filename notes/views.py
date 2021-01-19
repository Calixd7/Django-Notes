from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm, NoteSearchForm
from django.contrib.messages import success, error


def notes_list(request):
    notes = Note.objects.all()
    return render(request, "notes/notes_list.html", {"notes": notes})


def note_details(request, pk):
    note = get_object_or_404(Note, pk=pk)

    return render(request, "notes/note_details.html", {"note": note})


def notes_create(request):
    if request.method == "GET":
        form = NoteForm()

    else:
        form = NoteForm(data=request.POST)

        if form.is_valid():

            form.save()

            success(request, "Your note was created!")
            return redirect(to='notes_list')

    return render(request, "notes/notes_create.html", {"form": form})


def notes_update(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'GET':
        form = NoteForm(instance=note)

    else:
        form = NoteForm(data=request.POST, instance=note)

        if form.is_valid():
            form.save()
            success(request, 'Note has been updated!')
            return redirect(to='notes_list')

    return render(request, 'notes/notes_update.html', {'form': form})


def notes_delete(request, pk):
    if request.method == 'GET':
        return render(request, 'notes/notes_delete.html')

    else:
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        success(request, 'Note has been deleted!')
        return redirect(to='notes_list')


def notes_search(request):
    if request.method == 'GET':
        form = NoteSearchForm()
        return render(request, 'notes/notes_search.html', {'form': form})

    else:
        title_text = request.POST['title']
        title_search_crit = request.POST['title_search_by']

        body_text = request.POST['body']
        body_search_crit = request.POST['body_search_by']

        results = Note.objects.all()

        if title_search_crit == 'contains':
            results = results.filter(title__contains=title_text)

        else:
            results = results.filter(title=title_text)

        if body_search_crit == 'contains':
            results = results.filter(body__contains=body_text)

        else:
            results = results.filter(body=body_text)

        return render(request, 'notes/notes_search_results.html', {'results': results})