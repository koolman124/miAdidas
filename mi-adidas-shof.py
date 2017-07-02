import requests
import json
import time
from classes.GmailDotGen import GmailDotEmailGenerator

#Email
baseemail="imwashed@gmail.com"

#Name
firstName="JarJar"
lastName="IsThisEZmode"

#Gender: M or F
gender="M"

#Birthday Info - No this is not my birthday lol
birthMonth="01"
birthDay="01"
birthYear="1990"

underline='\033[04m'
orange='\033[33m'
lightblue='\033[94m'
red='\033[31m'
green='\033[32m'
purple='\033[35m'
lightgrey='\033[37m'
reset='\033[0m'

accountstogen = raw_input('Enter Desired Accounts to be Entered\t')
accountstogen = int(accountstogen)

for email in \
    (GmailDotEmailGenerator(baseemail).generate())[:accountstogen]:


    headers = {
        'Origin': 'http://www.adidas.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://www.adidas.com/us/mi_ultraboost',
        'Connection': 'keep-alive',
    }

    data = '{"email":"'+email+'","firstName":"'+firstName+'","lastName":"'+lastName+'","gender":"'+gender+'","datepicker":"'+(birthMonth.replace('0',''))+'/'+(birthDay.replace('0',''))+'/'+birthYear+'","dateOfBirth":"'+birthYear+'-'+birthMonth+'-'+birthDay+'","legalCheckbox":"1","countryOfSite":"US","newsletterDomain":"United States","newsletterLanguage":"en","newsletterTypeId":"40000","source":"90893","eventType":"0","sendMail":"N","consents":{"consent":[{"consentType":"AMF","consentValue":"Y","consentVersion":"ADIUS_VER_1"}]}}'

    r=requests.post('https://brand.campaign.adidas.com/api/scv/subscription/newsletter/create', headers=headers, data=data)
    print("Entered " + email)

try:
	dictionary=json.loads(r.text.encode("UTF-8"))
	if(dictionary["success"]):
		print "{} | [ {} ] {}".format(purple+str(time.asctime( time.localtime(time.time()) ))+reset,green+'Success'.center(25,' ')+reset,lightblue+underline+dictionary["euci"]+reset)
	else:
		print "Could not enter"
		print dictionary
except:
	print "You done messed up"
