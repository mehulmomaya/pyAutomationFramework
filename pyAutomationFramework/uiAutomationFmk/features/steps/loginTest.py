from behave import *
import time

use_step_matcher("re")

# @given('goto kelloggs microsite')
# def step_impl(context):
#     context.browser.get('https://pdnAccess:greasemonkey@kelloggsfamilyrewards.pdn.retaileriq.com')
#     time.sleep(6)
# @given('goto kelloggsfamilyrewards.pdn.retaileriq.com microsite and login with mmomaya@quotient.com and Testing_123')


@given('goto {url} microsite and login with {emailid} and {password}')
def step_impl(context,url,emailid,password):
    pdnurl = 'https://pdnAccess@greasemonkey/'+url+'/stores'
    context.browser.get(pdnurl)
    context.browser.find_element_by_xpath("//a[contains(text(), 'Log In')]").click()
    time.sleep(6)
