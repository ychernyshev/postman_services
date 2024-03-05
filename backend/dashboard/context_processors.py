from .forms import SearchForm
from simple_user.forms import UserSearchForm


def add_default_data(request):
    search_form = SearchForm()
    user_search = UserSearchForm()
    return {
        'search_form': search_form,
        'user_search': user_search,
    }