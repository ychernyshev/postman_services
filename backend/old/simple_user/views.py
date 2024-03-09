from django.db.models import Q
from django.shortcuts import render

# from dashboard.models import MailItemModel
# from .forms import UserSearchForm


# Create your views here.
def user_search(request):
    # if request.method == 'GET':
    #     form = UserSearchForm(request.GET)
    #     context = {}
    #
    #     if form.is_valid():
    #         query = form.cleaned_data['query']
    #         wanted_letter = MailItemModel.objects.filter(
    #             Q(track_number__icontains=query) |
    #             Q(date_of_receipt__icontains=query)
    #         )
    #
    #         context.update({
    #             'title': 'Title',
    #             'query': query,
    #             'wanted_letter': wanted_letter,
    #         })
    #
    #     return render(request, 'simple_user/user_search.html', context=context)
    return render(request, 'simple_user/user_search.html')
