from django.shortcuts import render

# Create your views here.

from namelist.models import Member, Syozoku

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_members = Member.objects.all().count()
#    num_instances = MemberInstance.objects.all().count()


    # The 'all()' is implied by default.    
    num_syozokus = Syozoku.objects.count()

    context = {
        'num_members': num_members,
#        'num_instances': num_instances,
        'num_syozokus': num_syozokus,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'namelist/index.html', context=context)

from django.views import generic

class MemberListView(generic.ListView):
    model = Member

class MemberDetailView(generic.DetailView):
    model = Member

class SyozokuListView(generic.ListView):
    model = Syozoku

class SyozokuDetailView(generic.DetailView):
    model = Syozoku
