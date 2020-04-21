from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.shortcuts import redirect


from .forms import GenerateRandomUserForm
from .tasks import create_random_user_acounts

class GenerateRandomUserView(FormView):
    template_name = 'index.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_acounts.delay(total)
        messages.success(self.request, 'Se estan creando usuarios, espere un momento')
        return redirect('user_list')




class UserListView(ListView):
    model = User
    context_object_name = 'usuarios'
    paginate_by = 10
    template_name = "lista_usuarios.html"
