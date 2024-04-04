from fyers_api import fyersModel
from fyers_api import accessToken
import time
from pyotp import TOTP
from selenium import webdriver

app_id = 'HKS1PHE7TF-100'
secret_id = 'I4PEPARAWL'
redirect_uri = 'https://trade.fyers.in/api-login/redirect-uri/index.html'
username = 'XS50441'
password = 'i7$pyMbx8MN#'
pin1 = '2'
pin2 = '2'
pin3 = '0'
pin4 = '9'

session = accessToken.SessionModel(
client_id=app_id,
secret_key = secret_id,
redirect_uri=redirect_uri,
response_type = 'code',
grant_type = 'authorization_code')


response = session.generate_authcode()
response

def generate_authcode():
    session = accessToken.SessionModel(client_id=app_id,
    secret_key = secret_id, redirect_uri=redirect_uri,response_type='code',grant_type='authorization_code')    
    response = session.generate_authcode()
    driver=webdriver.Chrome()
    driver.get(response)
    time.sleep(20)
    driver.find_element('xpath','//*[@id="fy_client_id"]').send_keys('XS50441')
    driver.find_element('xpath','//*[@id="clientIdSubmit"]').click()
    t = TOTP(772336).now()
    print(t)
    driver.find_element('xpath','//*[@id="first"]').send_keys(t[0])
    driver.find_element('xpath','//*[@id="second"]').send_keys(t[1])
    driver.find_element('xpath','//*[@id="third"]').send_keys(t[2])
    driver.find_element('xpath','//*[@id="fourth"]').send_keys(t[3])
    driver.find_element('xpath','//*[@id="fifth"]').send_keys(t[4])
    driver.find_element('xpath','//*[@id="sixth"]').send_keys(t[5])
    driver.find_element('xpath','//*[@id="confirmOtpSubmit"]').click()
    time.sleep(5)
    
    driver.find_element_by_id('verify-pin-page').find_element_by_id("first").send_keys(pin1)
    driver.find_element_by_id('verify-pin-page').find_element_by_id("second").send_keys(pin2)
    driver.find_element_by_id('verify-pin-page').find_element_by_id("third").send_keys(pin3)
    driver.find_element_by_id('verify-pin-page').find_element_by_id("fourth").send_keys(pin4)
    
    driver.find_element_by_xpath('//*[@id="verifyPinSubmit"]').click()
    time.sleep(5)
    newurl = driver.current_url
    auth_code = newurl[newurl.index('auth_code')+10:newurl.index('&state')]
    driver.quit()
    return auth_code
    
auth_code= generate_authcode()
