from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, TemplateView

from core.forms import SupplierForm
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

class HomeTemplateView(TemplateView):
   
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title1"] = "Autor | TeacherCode"
        context["title2"] = "Super Mercado Económico Popular"
        #context["suppliers"] = Supplier.objects.count()
        return context
    

    #return render(request,'home.html',data)

class SupplierListView(ListView): 
    model = Supplier 
    template_name = 'supplier/list.html'  # Nombre del template a usar 
    context_object_name = 'suppliers'     # Nombre del contexto a pasar al template 
    paginate_by = 10                    
    # Número de objetos por página 
    ordering = ['name']                   

    def get_queryset(self):
        # Se Puede personalizar el queryset aquí si es necesario
        queryset = super().get_queryset()  # self.model.objects.all()
        query = self.request.GET.get('q','')
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(ruc__icontains=query))
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title1"] = "Autor | TeacherCode"
        context["title2"] = "Listado de Proveedores VBC"
        return context
    
class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "supplier/form.html"
    success_url = reverse_lazy("core:supplier_list")  # Redirigir a la lista de proveedores después de crear uno nuevo
    #login_url = '/supplier_list/'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title1'] = '"Proveedores"'
        context['title2'] = 'Crear Nuevo Proveedor VBC'
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "supplier/form.html"
    success_url = reverse_lazy("core:supplier_list")  # Redirigir a la lista de proveedores después de crear uno nuevo
    #login_url = '/supplier_list/'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title1'] = '"Proveedores"'
        context['title2'] = 'Editar Proveedor'
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = "supplier/delete.html"
    success_url = reverse_lazy("core:supplier_list") 

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.delete()
    #     return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title1'] = "Eliminar"
        context['title2'] = 'Eliminar Proveedor VBC'
        return context