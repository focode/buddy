from django.views import generic
from django.shortcuts import render
from braces.views import LoginRequiredMixin
from . import forms
from models import usersProfiles


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class UserProfiles(LoginRequiredMixin, generic.TemplateView):

    def get(self, request, *args, **kwargs):
        template_name = "profiles/edit_profile.html"
        http_method_names = ['get', 'post']
        user = self.request.user
        models = usersProfiles
        form = forms.UserProfileForm(request.POST)
        if form.is_valid():
          # The form is valid and can be saved to the database
          # by calling the 'save()' method of the ModelForm instance.
          form.save()

          # Render the success page.
          return render(request, "tshirt_register/success.html")

          # This means that the request is a GET request. So we need to
          # create an instance of the TShirtRegistrationForm class and render it in
          # the template
        else:
            form = forms.UserProfileForm(request.POST)
            return render(request, "tshirt_register/tshirt_register.html", { 'form' : form })


