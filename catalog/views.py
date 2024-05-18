from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product

from django.shortcuts import render, get_object_or_404, redirect


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'cost_of_purchase', 'created_at', 'updated_at', 'image')
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        new_product = form.save(commit=False)
        new_product.slug = slugify(new_product.name)
        new_product.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'cost_of_purchase', 'created_at', 'updated_at', 'image')
    success_url = reverse_lazy('catalog:home')
    
    def get_success_url(self):
        return reverse('catalog:home_product', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class ActivityView(View):
    def get(self, request, pk):
        product_item = get_object_or_404(Product, pk=pk)
        if product_item.is_published:
            product_item.is_published = False
        else:
            product_item.is_published = True

        product_item.save()

        return redirect(reverse('catalog:home_product'))

class ContactsView(View):
    def get(self, request):
        return render(request, 'contacts.html')

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

        return render(request, 'contacts.html')
# def activity(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     if product_item.is_published:
#         product_item.is_published = False
#     else:
#         product_item.is_published = True
#
#     product_item.save()
#
#     return redirect(reverse('catalog:home_product'))
#
#
# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name} ({phone}): {message}')
#
#     return render(request, 'contacts.html')