from django.http import Http404
from django.views.generic import ListView,DetailView

from django.shortcuts import render

from .models import Product

class ProductFeaturedView(ListView):
    #queryset = Product.objects.featured()
    template_name = 'products/list.html'

    def get_queryset(self,*args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    #queryset = Product.objects.featured()
    template_name = 'products/detail.html'

    def get_queryset(self,*args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductListView(ListView):
    #queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_queryset(self,*args, **kwargs):
        request = self.request
        return Product.objects.all()


class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self,*args, **kwargs):
        context=super(ProductDetailView,self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self,*args,**kwarg):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)

        print(instance,pk)
        if instance is  None:
            raise Http404("product not exist")
        return instance





# Create your views here.
