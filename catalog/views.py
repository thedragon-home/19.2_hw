from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, BaseVersionInlineFormSet, VersionForm
from django.forms import inlineformset_factory

from catalog.models import Product, Version

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
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    # def form_valid(self, form):
    #     new_product = form.save(commit=False)
    #     new_product.slug = slugify(new_product.name)
    #     new_product.save()
    #
    #     return super().form_valid(form)
    


# Для отображения активной версии расширьте метод
# get_context_data()
#  контроллера списка продуктов, получите данные о версиях продукта и выберите текущую (активную) версию для продукта.
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm,
                                               formset=BaseVersionInlineFormSet, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if formset.is_valid() and form.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))



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