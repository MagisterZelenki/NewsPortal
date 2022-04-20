from django import template
from datetime import datetime

register = template.Library()

@register.filter()
def censor(value):
   bad_words = {'war', 'ukraine'}
   for i in bad_words:
      if i.find(value):
         value = value.replace(i[1::], "*" * len(i))
   return f'{value.lower()}'
