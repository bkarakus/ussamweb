try:
    from urllib import unquote
except ImportError:  # assume python3
    from urllib.parse import unquote

from string import punctuation

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from mezzanine.core.models import Orderable, SiteRelated
from mezzanine.core.models import CONTENT_STATUS_PUBLISHED, CONTENT_STATUS_CHOICES
from mezzanine.core.managers import DisplayableManager
from mezzanine.core.fields import FileField
from mezzanine.utils.models import AdminThumbMixin

class Slide(Orderable, SiteRelated, AdminThumbMixin):
    """
    Allows for pretty banner images across the top of pages that will cycle
    through each other with a fade effect.
    """
    image = FileField(_('Image'), max_length=200, upload_to='slides', format='Image')
    description = models.CharField(_('Description'), blank=True, max_length=200)
    caption = models.CharField(_('Caption'), blank=True, max_length=200)
    
    status = models.IntegerField(_("Status"),
        choices=CONTENT_STATUS_CHOICES, default=CONTENT_STATUS_PUBLISHED,
        help_text=_("With Draft chosen, will only be shown for admin users "
            "on the site."),
        editable=False)
    publish_date = models.DateTimeField(_("Published from"),
        help_text=_("With Published chosen, won't be shown until this time"),
        blank=True, null=True, db_index=True, editable=False)
    expiry_date = models.DateTimeField(_("Expires on"),
        help_text=_("With Published chosen, won't be shown after this time"),
        blank=True, null=True, editable=False)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    admin_thumb_field = "image"
    
    objects = DisplayableManager()
    
    class Meta:
        verbose_name = _('Slide')
        verbose_name_plural = _('Slides')
        ordering = ("-publish_date","_order")

    def __unicode__(self):
        return self.description

    def save(self, *args, **kwargs):
        """
        If no description is given when created, create one from the
        file name.
        """
        if not self.id and not self.description:
            name = unquote(self.image.url).split('/')[-1].rsplit('.', 1)[0]
            name = name.replace("'", '')
            name = ''.join([c if c not in punctuation else ' ' for c in name])
            # str.title() doesn't deal with unicode very well.
            # http://bugs.python.org/issue6412
            name = ''.join([s.upper() if i == 0 or name[i - 1] == ' ' else s
                            for i, s in enumerate(name)])
            self.description = name
        
        self.status = self.content_object.status
        self.publish_date = self.content_object.publish_date
        self.expiry_date = self.content_object.expiry_date
        super(Slide, self).save(*args, **kwargs)