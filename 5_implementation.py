#IMPORTING NECESSARY 00 LIBRARIES
from tld import get_tld
import pandas as pd
import joblib
import warnings
warnings.filterwarnings("ignore")

    #FEATURE ENGINEERING

#1. IP ADDRESS FUNCTION
#creating a function to check if the given url has ip address in it or not. there are 2 types of ip addresses,
#namely, IPv4 and IPv6, hence two lines of code
import re
def having_ip_address(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
    if match:
        return 1
    else:
        return 0

#2. ABNORMAL URL FUNCTION
from urllib.parse import urlparse
def abnormal_url(url):
    hostname = urlparse(url).hostname
    hostname = str(hostname)
    match = re.search(hostname, url)
    if match:
        return 1
    else:
        return 0


#3. GOOGLE INDEX FUNCTION
#a function to see if the given url is indexed on google
from googlesearch import search
def google_index(url):
    site = search(url, 5)
    return 1 if site else 0


#4. NUMBER OF DOTS FUNCTION
#a function to detect the number of dots(.) in the given url
def count_dot(url):
    count_dot = url.count('.')
    return count_dot


#5. NUMBER OF "WWW" FUNCTION
# a function to detect the number of www's in the given url
def count_www(url):
    url.count('www')
    return url.count('www')


#6. NUMBER OF "@" FUNCTION
#a function to detect the number of @'s in the given url
def count_atrate(url):
    return url.count('@')


#7. NUMBER OF "/" FUNCTION
#a function to detect the number of /'s in the given url
def no_of_dir(url):
    urldir = urlparse(url).path
    return urldir.count('/')


#8. NUMBER OF "//" FUNCTION
#a function to detect the number of //'s in the given url
def no_of_embed(url):
    urldir = urlparse(url).path
    return urldir.count('//')


#9. SHORTENED URL FUNCTION
#a function to see if the url is shortened
def shortening_service(url):
    match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                      'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                      'tr\.im|link\.zip\.net',
                      url)
    if match:
        return 1
    else:
        return 0

#10. NUMBER OF 'https' FUNCTION
#a function to detect the number of 'https' in the given url
def count_https(url):
    return url.count('https')

#11. NUMBER OF 'http' FUNCTION
#a function to detect the number of 'http' in the given url
def count_http(url):
    return url.count('http')

#12. NUMBER OF % FUNCTION
#a function to detect the number of %'s in the given url
def count_per(url):
    return url.count('%')

#13. NUMBER OF ? FUNCTION
#a function to detect the number of ?'s in the given url
def count_ques(url):
    return url.count('?')

#14. NUMBER OF - FUNCTION
#a function to detect the number of -'s in the given url
def count_hyphen(url):
    return url.count('-')

#15. NUMBER OF = FUNCTION
#a function to detect the number of ='s in the given url
def count_equal(url):
    return url.count('=')

#16. URL LENGTH FUNCTION
#a function to get the length of the url
def url_length(url):
    return len(str(url))

#17. HOSTNAME LENGTH FUNCTION
#a function to get the hostname length
def hostname_length(url):
    return len(urlparse(url).netloc)

#18. SUSPICIOUS WORDS FUNCTION
#a function to detect suspicious words, if any.
def suspicious_words(url):
    match = re.search('PayPal|login|signin|bank|account|update|free|lucky|service|bonus|ebayisapi|webscr',url)
    if match:
        return 1
    else:
        return 0

#19. DIGIT COUNTER FUNCTION
#a function to count the number of digits in the given url
def digit_count(url):
    digits = 0
    for i in url:
        if i.isnumeric():
            digits = digits + 1
    return digits

#20. LETTER COUNTER FUNCTION
#a function to count the number of letter in the given url
def letter_count(url):
    letters = 0
    for i in url:
        if i.isalpha():
            letters = letters + 1
    return letters

#21. TOP LEVEL DOMAIN & LENGTH FUNCTION
#a function to get the first directory length
def fd_length(url):
    urlpath= urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0

#22. FIRST DIRECTORY LENGTH
#a function to get the first directory length

def tld_length(tld):#defining a functin to get the length of tld from the column tld creating by above line
    try:
        return len(tld)
    except:
        return -1

#now that we have created all the necessary columns, extracted from url column,
#we will export the data as a csv file and use it later as a pre-processed csv in order to reduce computation time

url_input = str(input('enter url : '))

#all the following are outputs(22 outputs)
url_use_of_ip = having_ip_address(url_input)
url_abnormal_url = abnormal_url(url_input)
url_google_index = google_index(url_input)
url_count_dot = count_dot(url_input)
url_count_www = count_www(url_input)
url_count_atrate = count_atrate(url_input)
url_count_dir = no_of_dir(url_input)
url_count_embed_domian = no_of_embed(url_input)
url_short_url = shortening_service(url_input)
url_count_https = count_https(url_input)
url_count_http = count_http(url_input)
url_count_percent = count_per(url_input)
url_count_ques = count_ques(url_input)
url_count_dash = count_hyphen(url_input)
url_count= count_equal(url_input)
url_url_length = url_length(url_input)
url_hostname_length = hostname_length(url_input)
url_sus_url = suspicious_words(url_input)
url_fd_length = fd_length(url_input)
url_tld = get_tld(url_input, fail_silently=True)
url_tld_length = tld_length(url_tld)
url_count_digits = digit_count(url_input)
url_count_letters = letter_count(url_input)

features = [[url_use_of_ip, url_abnormal_url,url_google_index, url_count_dot, url_count_www,
            url_count_atrate, url_count_dir, url_count_embed_domian,
            url_short_url, url_count_https, url_count_http, url_count_percent,
            url_count_ques, url_count_dash, url_count, url_url_length,
            url_hostname_length, url_sus_url, url_fd_length, url_tld_length,
            url_count_digits, url_count_letters]]

# USING FEATURES FOR LOGISTIC REGRESSION PREDICTION
lr = joblib.load('1_lr_model_new.pkl')
lr_diagnosis = lr.predict(features)[0]
if lr_diagnosis == 'safe':
    lr_result = 0
if lr_diagnosis == 'not safe':
    lr_result = 1

# USING FEATURES FOR RANDOM FOREST PREDICTION
rf = joblib.load('2_rf_model_new.pkl')
rf_diagnosis = rf.predict(features)[0]
if rf_diagnosis == 'safe':
    rf_result = 0
if rf_diagnosis == 'not safe':
    rf_result = 1

# USING FEATURES FOR DECISION TREE PREDICTION
dt = joblib.load('3_dt_model_new.pkl')
dt_diagnosis = dt.predict(features)[0]
if dt_diagnosis == 'safe':
    dt_result = 0
if dt_diagnosis == 'not safe':
    dt_result = 1

# USING FEATURES FOR STACKED MODEL PREDICTION
stacked_model = joblib.load('4_stacked_model_new.pkl')
stacked_model_diagnosis = stacked_model.predict([[lr_result, rf_result, dt_result]])
if stacked_model_diagnosis[0] == 1:
    stacked_model_result = 'safe'
if stacked_model_diagnosis[0] == 0:
    stacked_model_result = 'not safe'

print(f'Logistic Regression result : {lr_diagnosis}')#display this binod
print(f'Random Forest result : {rf_diagnosis}')#display this binod
print(f'Decision Tree result : {dt_diagnosis}')#display this binod
print(f'stacked model result : ',stacked_model_result)#display this binod

