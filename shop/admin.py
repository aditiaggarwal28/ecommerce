from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Transaction
from .models import Contact
from .models import Checkout
from .models import Orderupdate
from .models import Payment

admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(Contact)
admin.site.register(Checkout)
admin.site.register(Orderupdate)
admin.site.register(Payment)

