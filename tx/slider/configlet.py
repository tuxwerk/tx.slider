from zope.interface import Interface
from zope.interface import implements
from zope.component import adapts

from zope import schema
#from zope.formlib import form

from tx.slider import message_factory as _
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.app.controlpanel.form import ControlPanelForm

from zope.component.hooks import getSite
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFDefault.formlib.schema import SchemaAdapterBase

from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from plone.z3cform import layout
from z3c.form import form

from zope.component import getUtility
from plone.registry.interfaces import IRegistry

def slider_navigation_type_choices(context):
    return SimpleVocabulary([
        SimpleTerm(title=_(u"Arrows"),  value='arrows'),
        SimpleTerm(title=_(u"Bullets"), value='bullets'),
        SimpleTerm(title=_(u"Both"),    value='both'),
        SimpleTerm(title=_(u"None"),    value='none'),
    ])

def slider_effect_choices(context):
    return SimpleVocabulary([
        SimpleTerm(title=_(u"Horizontal"), value='scrollHorz'),
        SimpleTerm(title=_(u"Vertical"),   value='scrollVert'),
        SimpleTerm(title=_(u"Tile slide"), value='tileSlide'),
        SimpleTerm(title=_(u"Tile blind"), value='tileBlind')
    ])

def slider_configuration_choices(context):
    configs = getUtility(IRegistry)['tx.slider.configlet.ISliderControlPanel.configuration']
    items = []
    for config in configs:
        t = config.split(":")
        items = items + [(t[1],t[0]),]
    terms = [ SimpleTerm(value=pair[0], token=pair[0], title=pair[1]) for pair in items ]
    return SimpleVocabulary(terms)

def slide_configuration_choices(context):
    configs = getUtility(IRegistry)['tx.slider.configlet.ISliderControlPanel.slide_configuration']
    items = []
    for config in configs:
        t = config.split(":")
        items = items + [(t[1],t[0]),]
    terms = [ SimpleTerm(value=pair[0], token=pair[0], title=pair[1]) for pair in items ]
    return SimpleVocabulary(terms)

class ISliderControlPanel(Interface):
    """
    The actual slider settings
    """

    configuration = schema.List(
        title=_(u'Configuration'),
        description=_(u"Enter one configuration per line. Format: 'Name:css-class-name'. First entry is default."),
        value_type=schema.TextLine(),
        required=True
    )

    slide_configuration = schema.List(
        title=_(u'Slide configuration'),
        description=_(u"Additional configuration for individual slides. Format: 'Name:css-class-name'."),
        value_type=schema.TextLine(),
        required=False
    )

    effect = schema.Choice(
        source="slider_effect_choices",
        title=_(u"Effect"),
        description=_(u"Please choose the default effect type."),
        default="scrollHorz",
        required=True
    )

    speed = schema.Int(
        title=_(u"Speed"),
        description=_(u"Speed at which the slides will transition (in milliseconds)."),
        default=800,
        required=True
    )

    pause = schema.Int(
        title=_(u"Pause"),
        description=_(u"Duration of the pause between transitions (in milliseconds)."),
        default=4000,
        required=True
    )

    navigation_type = schema.Choice(
        source      = "slider_navigation_type_choices",
        title       = _(u"Type of navigation"),
        description = _(u"Please choose the default navigation type."),
        default     = "arrows",
        required    = True        
    )

    image_scale_width = schema.Int(
        title=_(u"Image scale width"),
        description=_(u"All uploaded images will be scaled down to this value."),
        default=1200,
        required=True
    )
    
class ControlPanelForm(RegistryEditForm):

    form.extends(RegistryEditForm)
    schema = ISliderControlPanel
    label = _(u"Slider default settings")
    description = _(u'Default settings to use for all sliders.')
    
class ControlPanel(ControlPanelFormWrapper):

    form = ControlPanelForm
