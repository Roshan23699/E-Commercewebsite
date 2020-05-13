from django.contrib import admin

# Register your models here.
from .models import Product
from .models import SlideShow
from .models import FoodGrain
from .models import SaltSugarandJaggery
from .models import OilsGheeandMasala
from .models import DalandPulses
from .models import Fruit
from .models import Vegetable

admin.site.register(Product)
admin.site.register(FoodGrain)
admin.site.register(SlideShow)
admin.site.register(DalandPulses)
admin.site.register(OilsGheeandMasala)
admin.site.register(SaltSugarandJaggery)
admin.site.register(Fruit)
admin.site.register(Vegetable)
