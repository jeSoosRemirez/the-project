from django.shortcuts import render
from django.http import HttpResponse

from ..models.groups_model import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def groups_list(request):
    groups = Group.objects.all()

    # order groups
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    # paginate groups
    paginator = Paginator(groups, 3)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer then deliver first page
        groups = paginator.page(1)
    except EmptyPage:
        # if page is out of range (9999) then deliver last page of res
        groups = paginator.page(paginator.num_pages)
    return render(request, 'students/groups.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1></h1>Group Add Form')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Groups $s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
