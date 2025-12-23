'''
utlis.py

this file contains helper functions for the url based feature extraction.
each function takes a url as input and returns a numerical value that
helps identify phishing characteristics

'''
import ipaddress
from urllib.parse import urlparse


def get_url_length(url):
    '''
    Returns the total length of the URL.
    Phishing URLs are often longer to hide the real domain.
    '''
    return len(url)

 
def has_ip_address(url):
    '''
        Checks whether the URL uses an IP address instead of a domain name.
    Legitimate websites almost never use raw IP addresses.
    
    Returns:
        1 if IP address is found, else 0

    '''
    try:
        host = urlparse(url).hostname
        if host is None:
            return 0
        ipaddress.ip_address(host)
        return 1
    except ValueError:
        return 0
    
def count_hyphens(url):
    '''
    Counts the number of hyphens '-' in the URL.
    Hyphens are commonly used in phishing URLs to mimic brand names.
    '''

    return url.count('-')


def dot_count(url):
    '''
    Counts the number of dots '.' in the URL.
    A high dot count often indicates multiple subdomains.
    '''
    
    return url.count('.')


def count_at_symbols(url):
    '''
   Counts the number of '@' symbols in the URL.
    URLs with '@' are highly suspicious.
    '''
    return url.count('@')


def has_https(url):
    """
    Checks whether the URL uses HTTPS.
    HTTPS alone does not guarantee legitimacy, but HTTP is riskier.
    
    Returns:
        1 if HTTPS is used, else 0
    """
    scheme = urlparse(url).scheme
    if scheme == 'https':
        return 1
    else:
        return 0
    

def count_subdomains(url):
    """
    Counts the number of subdomains in the URL.
    Excessive subdomains are a strong phishing indicator.
    """
    host = urlparse(url).hostname
    if host is None:
        return 0
    dot_count = host.count('.')
    return max(0,dot_count-1)
  
def flag_words_counts(url):
    """
    Counts suspicious keywords commonly found in phishing URLs.
    More matches increase phishing likelihood.
    """
    flag_words = [
    "login", "signin", "verify", "secure", "account", "update",
    "confirm", "password", "bank", "payment", "alert", "suspend",
    "unlock", "reset", "wallet", "billing", "refund"
]
    url = url.lower()
    count = 0
    for word in flag_words:
        if word in url:
            count+=1
    return count


def count_encoded_chars(url):
    """
    Counts encoded characters (%) in the URL path.
    Encoded paths are often used to obfuscate malicious intent.
    """
    path = urlparse(url).path
    if path is None:
        return 0
    return path.count("%")


def get_query_length(url):
    """
    Returns the length of the query string.
    Long query strings may hide malicious payloads.
    """
    query = urlparse(url).query
    if  not query :
        return 0
    return len(query)
    


