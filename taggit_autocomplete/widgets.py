from django import forms
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

from taggit.utils import edit_string_for_tags
from taggit_autocomplete import settings


class TagAutocomplete(forms.TextInput):
    input_type = 'text'

    def render(self, name, value, attrs=None):
        if value is not None and not isinstance(value, basestring):
            value = edit_string_for_tags(
                    [o.tag for o in value.select_related("tag")])
        attrs['class'] = (attrs.get('class', '') + ' django-taggit-ac').strip()
        attrs['data-src'] = reverse('taggit_autocomplete-list')
        return super(TagAutocomplete, self).render(name, value, attrs)

    class Media:
        css = {
            'all': settings.CSS,
        }
        js = settings.JS
        
