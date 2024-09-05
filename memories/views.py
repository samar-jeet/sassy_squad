from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from .models import Memory
from .forms import MemoryForm
from django.contrib.auth.decorators import login_required

@login_required
def memory(request):
    return render(request, 'memories/memory.html')

class MemoryCreateView(CreateView):
    model = Memory
    form_class = MemoryForm
    template_name = 'memories/memory_form.html'
    success_url = reverse_lazy('memory-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MemoryListView(ListView):
    model = Memory
    template_name = 'memories/memory_list.html'
    context_object_name = 'memories'

    def get_queryset(self):
        return Memory.objects.all()

class MemoryUpdateView(UpdateView):
    model = Memory
    form_class = MemoryForm
    template_name = 'memories/memory_update_form.html'
    success_url = reverse_lazy('memory-list')


from django.views.generic import DeleteView
class MemoryDeleteView(DeleteView):
    model = Memory
    template_name = 'memories/memory_confirm_delete.html'
    success_url = reverse_lazy('memory-list')
