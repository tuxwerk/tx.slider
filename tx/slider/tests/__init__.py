from Products.CMFCore.utils import getToolByName
from tx.slider.testing import SLIDER_INTEGRATION_TESTING, SLIDER_FUNCTIONAL_TESTING
from plone.app.testing import setRoles
import unittest
from plone.app.testing import TEST_USER_ID
from tx.slider.interfaces import ISliderLayer
from zope.interface import alsoProvides
from Testing.ZopeTestCase import Functional


class BaseTest(unittest.TestCase):

    layer = SLIDER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.app = self.layer['app']
        alsoProvides(self.request, ISliderLayer)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def tearDown(self):
        pass

    def uninstall(self):
        setup_tool = getToolByName(self.portal, 'portal_setup')
        setup_tool.runAllImportStepsFromProfile(
            'profile-tx.slider:uninstall')

    def create_object(self, id, type_name, parent=None):
        if parent:
            return parent[parent.invokeFactory(type_name=type_name, id=id)]
        else:
            return self.portal[self.portal.invokeFactory(
                type_name=type_name, id=id)]


class BaseFunctionalTest(BaseTest, Functional):

    layer = SLIDER_FUNCTIONAL_TESTING
