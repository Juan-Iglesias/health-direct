'''
Created on Aug 3, 2012

@author: juan
'''
from django import template
from django.conf import settings
 
class CheckupDisplayNode(template.Node):
    def __init__(self,appName,checkupId):
        self.appName = appName
        self.checkupId = checkupId
    def render(self,context):
        if self.app not in settings.INSTALLED_APPS:
            return '' # @todo: raise an error here 
        