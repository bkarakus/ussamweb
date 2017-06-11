from django.forms.models import ModelForm

class AlwaysChangedModelForm(ModelForm):
    def has_changed(self):
        """ Should returns True if data differs from initial. 
        By always returning true even unchanged inlines will get validated and saved."""
        if self.instance and self.instance.pk:
            return True
        else:
            return super(AlwaysChangedModelForm, self).has_changed()