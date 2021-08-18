from django.shortcuts import render
from django.http import HttpResponse


def groups_list(request):
    groups = (
        {
            'id': 1,
            'naming': 'A',
            'head': 'Kapusta',
        },
        {
            'id': 2,
            'naming': 'B',
            'head': 'Tsal',
        },
        {
            'id': 3,
            'naming': 'C',
            'head': 'Bruh',
        }
    )
    return render(request, 'students/groups.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1></h1>Group Add Form')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Groups $s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
