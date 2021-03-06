from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.instance import memoize

from tx.slider.settings import PageSliderSettings
from tx.slider.interfaces import ISliderPage
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from Products.CMFCore.interfaces import ISiteRoot

class BaseSliderViewlet(ViewletBase):

    index = ViewPageTemplateFile('templates/viewlet.pt')
    
    @memoize
    def sliderobject(self):
        for item in self.context.aq_chain:
            if ISliderPage.providedBy(item):
                return item
            if ISiteRoot.providedBy(item):
                return None
    
    @memoize
    def get_settings(self):
        return PageSliderSettings(self.sliderobject())

    @memoize
    def registry(self, key):
        return getUtility(IRegistry)['tx.slider.configlet.ISliderControlPanel.' + key]

    @memoize
    def configuration(self):
        configs = self.registry('configuration')
        for config in configs:
            t = config.split("|")
            if t[1] == self.settings.configuration:
                return t
        return configs[0].split("|")
    
    @memoize
    def show(self):
        sliderobject = self.sliderobject()
        if sliderobject:
            if sliderobject != self.context:
                if self.settings.only_here:
                    return False
            if len(self.settings.slides) == 0:
                return False
            else:
                return self.settings.show
        else:
            return False

    @memoize
    def sliderposition(self):
        return self.settings.sliderposition

    @memoize
    def class_name(self):
        c = self.configuration()
        if c:
            return c[1]

    @memoize
    def effect(self):
        return self.settings.effect or self.registry('effect')
                
    @memoize
    def randomize(self):
        return str(self.settings.randomize).lower()

    @memoize
    def speed(self):
        return self.settings.speed or self.registry('speed')

    @memoize
    def pause(self):
        return self.settings.pause or self.registry('pause')

    @memoize
    def continuous(self):
        return self.settings.continuous

    @property
    def slides(self):
        return self.settings.slides

    @memoize
    def absolute_url(self):
        return self.sliderobject().absolute_url()

    @memoize
    def navigation_type(self):
    	return self.settings.navigation_type or self.registry('navigation_type')

    settings = property(get_settings)

class SliderPortalTop(BaseSliderViewlet):

    def is_enabled(self):
        return self.show() and self.sliderposition() == "portal_top"

    def render(self):
        if self.is_enabled():
            return super(SliderPortalTop, self).render()
        else:
            return ""

class SliderAboveContent(BaseSliderViewlet):

    def is_enabled(self):
        return self.show() and self.sliderposition() == "above_content"

    def render(self):
        if self.is_enabled():
            return super(SliderAboveContent, self).render()
        else:
            return ""

class SliderBelowContentTitle(BaseSliderViewlet):

    def is_enabled(self):
        return self.show() and self.sliderposition() == "below_content_title"

    def render(self):
        if self.is_enabled():
            return super(SliderBelowContentTitle, self).render()
        else:
            return ""
    
class SliderBelowContent(BaseSliderViewlet):

    def is_enabled(self):
        return self.show() and self.sliderposition() == "below_content"

    def render(self):
        if self.is_enabled():
            return super(SliderBelowContent, self).render()
        else:
            return ""
    
