from django import template

register = template.Library()

@register.filter(name='product_by_vendor')
def vendor_is_in_cart(product, vindex):
    keys = vindex.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name='order_quantity')
def vendor_cart_quantity(product, vindex):
    keys = vindex.keys()
    for id in keys:
        if int(id) == product.id:
            return vindex.get(id)
    return 0

@register.filter(name='price_total')
def order_price_total(product, vindex):
    return product.price * vendor_cart_quantity(product, vindex)
