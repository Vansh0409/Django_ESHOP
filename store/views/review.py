from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from store.models.reviews import Review
from django.views import View
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class RReview(View):

    def get(self, request, **kwargs):
        product = request.session.get('product')
        print(product)
        product_id = self.kwargs['myid']
        product = Product.objects.get(id=product_id)
        print(product)
        reviews = Review.get_reviews_by_product(product)

        # print(reviews)
        return render(request, 'review.html', {'reviews': reviews, 'product': product})

    def post(self, request, **kwargs):

        postData = request.POST
        product_id = self.kwargs['myid']
        product = Product.objects.get(id=product_id)
        review = request.POST.get('review')
        value = {'review': review, 'product':product}

        review = Review(review=review, product=product)
        review.save()
        data = {
            'review': review,
            'values': value,
            'product':product
        }


        #return render(request, 'review.html', data)
        return redirect('review', myid=product.id)
