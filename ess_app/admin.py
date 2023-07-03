from django.contrib import admin

# Register your models here.
from .models import Scheme,Query,Feedback_Rating,Rented,Tips,Consultant,Owner,Client,Seller

class Scheme_Admin(admin.ModelAdmin):
    list_display=('scheme_topic','scheme_contents','date')
    search_fields=('scheme_topic','date')
    list_filter=['date']

class Feedback_Admin(admin.ModelAdmin):
    list_display=('name','email','phone','feedback_text','ratings','date')
    search_fields=('name','ratings','date',)
    list_filter=['date']

class Tips_Admin(admin.ModelAdmin):
    list_display=('tips_contents','date')
    search_fields=('date')
    list_filter=['date']

class Query_Admin(admin.ModelAdmin):
    list_display=('name','email','phone','user_query','date')
    search_fields=('name','date')
    list_filter=['date']


class Consultant_Admin(admin.ModelAdmin):
    list_display=('user_id','password','name','email','phone','address','experience','date')
    search_fields=('user_id','experience','date')
    list_filter=['experience','date']

class Owner_Admin(admin.ModelAdmin):
    list_display=('owner_id','password','name','email','phone','city','address','type','date')
    search_fields=('owner_id','type','date')
    list_filter=['type','date']

class Client_Admin(admin.ModelAdmin):
    list_display=('client_id','password','name','email','phone','date')
    search_fields=('client_id','date')
    list_filter=['date']

class Rented_Admin(admin.ModelAdmin):
    list_display=('user_id','property_type','rent_price','facilities','city','address','contact','date')
    search_fields=('property_type','rent_price','date')
    list_filter=['property_type','rent_price','date']

class Seller_Admin(admin.ModelAdmin):
    list_display=('user_id','property_type','sell_price','facilities','city','address','contact','date')
    search_fields=('property_type','sell_price','date')
    list_filter=['property_type','sell_price','date']



admin.site.register(Scheme,Scheme_Admin)
admin.site.register(Query,Query_Admin)
admin.site.register(Feedback_Rating)
admin.site.register(Tips)
admin.site.register(Consultant,Consultant_Admin)
admin.site.register(Owner,Owner_Admin)
admin.site.register(Client)
admin.site.register(Rented,Rented_Admin)
admin.site.register(Seller,Seller_Admin)


admin.site.site_header="Estate Essentials Administration"
admin.site.site_title="Admin Dashboard"
admin.site.index_title="Welcome to Real Estate Portal"