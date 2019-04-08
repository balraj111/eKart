from django.http import Http404
from django.views.generic import ListView,DetailView

from django.shortcuts import render, get_object_or_404

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

class ProductSlugView(DetailView):
    queryset = Product.objects.featured()
    template_name = 'products/detail.html'

    def get_object(self,*args,**kwarg):
        request = self.request
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(Product,slug=slug,active=True)

        try:
            instance = Product.objects.get(slug=slug,active=True)
        except Product.DoesNotExist:
            raise Http404("Not Found")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug,active=True)
            instance = qs.first()
        except:
            raise Http404("something went wrong")


        print(instance,slug)
        if instance is  None:
            raise Http404("product not exist")
        return instance


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
