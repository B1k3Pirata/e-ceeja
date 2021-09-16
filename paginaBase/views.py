from django.views.generic import TemplateView

# Create your views here.
app_name = 'paginas'

class IndexView(TemplateView):
    template_name = "paginas/base.html"
