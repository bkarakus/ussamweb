# encoding: utf-8
from mezzanine.conf import register_setting

register_setting(
    name="SITE_ADDRESS_LINE_1",
    label=u"Adres (Satır 1)",
    description=u"Adres (Satır 1)",
    editable=True,
    default=''
)

register_setting(
    name="SITE_ADDRESS_LINE_2",
    label=u"Adres (Satır 2)",
    description=u"Adres (Satır 2)",
    editable=True,
    default=''
)

register_setting(
    name="SITE_ADDRESS_CITY",
    label=u"Adres (Satır 3)",
    description=u"Şehir Adı ve/veya Ülke adı",
    editable=True,
    default=''
)

register_setting(
    name="SITE_ADDRESS_POSTAL_CODE",
    label=u"Posta Kodu",
    description=u"Posta Kodu",
    editable=True,
    default=''
)

register_setting(
    name="SITE_PHONE",
    label=u"Telefon",
    description=u"Telefon numarası",
    editable=True,
    default='+90 --- -- --'
)

register_setting(
    name="SITE_FAX",
    label=u"FAX",
    description=u"Fax numarası",
    editable=True,
    default='+90 --- -- --'
)

register_setting(
    name="SITE_EMAIL",
    label=u"Email",
    description=u"",
    editable=True,
    default=''
)

register_setting(
    name="SITE_GOOGLE_MAP",
    label=u"Google Map",
    description=u"",
    editable=True,
    default=""
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description=("Sequence of setting names available within templates."),
    editable=False,
    default=("SITE_ADDRESS_LINE_1", "SITE_ADDRESS_LINE_2", 
             "SITE_ADDRESS_POSTAL_CODE", "SITE_ADDRESS_CITY", 
             "SITE_PHONE", "SITE_FAX", "SITE_EMAIL",
             "SITE_GOOGLE_MAP",),
    append=True,
)