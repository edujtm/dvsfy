from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout

# Create your views here.

class AppView(TemplateView):
    """
    Represents the main app section.

    This is needed because the OAuth protocol incurs a redirect for login,
    which means that a landing page is necessary before the user is authenticated.

    The Authorization Code Flow from OAuth specs is not well suited for single page
    web apps, but it's the only one (of the Spotify API) which allows to keep the 
    access token for an undetermined amount of time.
    """
    template_name = 'app.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/')
        return super(AppView, self).get(request)


def landing_page_view(request):
    if request.user.is_authenticated:
        return redirect('/app/')
    return render(request, "index.html")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')
