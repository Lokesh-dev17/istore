from django.contrib import admin
from istore.models import Contact,Salesorder,salesdetails,productsdetails

admin.site.register(Contact)
admin.site.register(Salesorder)
admin.site.register(salesdetails)
admin.site.register(productsdetails)