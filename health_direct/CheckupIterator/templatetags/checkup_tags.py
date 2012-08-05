'''
Created on Aug 3, 2012

@author: juan
'''
from django.template.loader import get_template
from django import template
from django.conf import settings

register = template.Library()

@register.tag(name="CheckupDisplay")
def do_CheckupDisplay(parser, token):
    try:
        tag_name, appName, checkupId = token.split_contents()
    except ValueError:
        msg = '%r tag requires two arguments' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CheckupDisplayNode(appName, checkupId)
         

class CheckupDisplayNode(template.Node):
    def __init__(self,appName,checkupId):
        self.appName = template.Variable(appName)
        self.checkupId = template.Variable(checkupId)
    def render(self,context): #Determine how to correctly use context parameter
        #if self.app not in settings.INSTALLED_APPS:
        #    return '' # @todo: raise an error here 
        
        # From djangobook:
        # Like template filters, these rendering functions should fail
        # silently instead of raising errors. The only time that template
        # tags are allowed to raise errors is at compilation time.
        
        # find self.app (maybe it will be a path)
        # find template folder for app.path
        appNameVal = str(self.appName.resolve(context)) 
        template = appNameVal + '.html'
        t = get_template(appNameVal + '/templates/' + template)
        
        #Now we're tasked with filling this context with the data we'll receive from the id
        
        return t.render(context)