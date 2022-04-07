from modeltranslation.translator import translator, TranslationOptions
from .models import *

class PostTranslationOptions(TranslationOptions):
    fields = ('name','description')

translator.register(Product, PostTranslationOptions)

class CatTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CatTranslationOptions)

class SlideTranslationOptions(TranslationOptions):
    fields = ('sub_title','title')

translator.register(Slider, SlideTranslationOptions)