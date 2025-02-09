from django.views.generic import TemplateView

# pages class views

class HomePageView(TemplateView):
    template_name = "home.html"