from django.shortcuts import render
from django.http import HttpResponse


# Views for Students

def students_list(request):
    students = (
        {
            'id': 1,
            'first_name': 'Viktor',
            'last_name': 'Kapusta',
            'ticket': 742,
            'image': 'img/kapusta.png'
        },
        {
            'id': 2,
            'first_name': 'Vitaliy',
            'last_name': 'Tsal',
            'ticket': 617,
            'image': 'img/papich.png'
        },
        {
            'id': 3,
            'first_name': 'Oleg',
            'last_name': 'Negdanchik',
            'ticket': 27,
            'image': 'img/bruh.png'
        }
    )
    return render(request, "students/students_list.html", {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


# Views for Groups

def groups_list(request):
    return render(request, 'students/groups.html')


def groups_add(request):
    return HttpResponse('<h1></h1>Group Add Form')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Groups $s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
