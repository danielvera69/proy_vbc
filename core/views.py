from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Supplier 
from django.shortcuts import redirect, render
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


def home(request):
    data = {
        "title1":"Autor | TeacherCode",
        "title2":"Super Mercado Economico"
    }
   
    return render(request,'home.html',data)

class SupplierListView(ListView): 
    model = Supplier 
    template_name = 'supplier/list.html'  # Nombre del template a usar 
    context_object_name = 'suppliers'     # Nombre del contexto a pasar al template 
    paginate_by = 10                    
    # Número de objetos por página 
    ordering = ['name']                   

    def get_queryset(self):
        # Se Puede personalizar el queryset aquí si es necesario
        queryset = super().get_queryset()  # Solo proveedores activos
        query = self.request.GET.get('q','')
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(ruc__icontains=query))
        return queryset

class SupplierCreateView(CreateView):
    pass

class SupplierUpdateView(UpdateView):
    pass

class SupplierDeleteView(DeleteView):
    pass