from django.shortcuts import render
from .models import ChoreGroup, Chore
from django.shortcuts import redirect

def choregroupList(request):
    print('debug choregroupList')
    print(request)
    choregroups = ChoreGroup.objects.all().filter(author=request.user).order_by('-choregroup_name')
    return render(request, 'chore/index.html', {'choregroups':choregroups })

def choregroupCreate(request):
    print('debug choreGroupCreate')


    if request.method == 'POST':
        print(request.POST['choregroup_name'])
        print(request.POST['description'])
        print(request.POST)
        newchoreGroup = ChoreGroup.objects.create(
            choregroup_name=request.POST['choregroup_name'],
            description=request.POST['description'],
            author=request.user
        )
        print('new choregroupid:', newchoreGroup.id)
        for formName in request.POST:
            print(formName, request.POST[formName])
            if formName.startswith('chore_name'):
                choreNumber=formName.split("_")[2]
                sequenceField= 'chore_sequence_' + choreNumber
                Chore.objects.create(
                    chore_name=request.POST[formName],
                    sequence=request.POST[sequenceField],
                    choregroup=newchoreGroup
                )
        return redirect('choregroup_list')
    else:
        return render(request, 'chore/choregroup_form.html')


def choregroupUpdate(request):
    print('debug choreGroupUpdate')

def choregroupDelete(request,pk):
    ChoreGroup.objects.filter(pk=pk).delete()
    print('debug choreGroupDelete', pk)
    return redirect('choregroup_list')