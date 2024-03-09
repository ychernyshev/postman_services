from .forms import SearchForm
# from simple_user.forms import UserSearchForm


def add_default_data(request):
    search_form = SearchForm()
    # user_search_form = UserSearchForm()
    return {
        'search_form': search_form,
        # 'user_search_form': user_search_form,
    }