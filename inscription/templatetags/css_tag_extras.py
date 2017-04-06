from django import template
register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
   if "Date" not in field.label:
      return field.as_widget(attrs={"class": css})
   else:
      return  field.as_widget(attrs={"class": css + " datepicker"})