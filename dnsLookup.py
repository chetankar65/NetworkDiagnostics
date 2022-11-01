# Import libraries
#from tkinter import EXCEPTION
import dns.resolver
  
def get_ip_address(domain):
    nameservers = []
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for val in answers:
            nameservers.append((domain, val.to_text()))
        return nameservers
    except Exception:
        return False
        # domain doesn't exist

def get_nameservers(domain):
    nameservers = []
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        for val in answers:
            nameservers.append((domain, val.to_text()))
        return nameservers
    except Exception:
        return False
        # print that name server is not configured

def check_status(domain):
    if (get_nameservers(domain)):
        if (not get_ip_address(domain)):
            print("Domain doesn't exist.")
    else:
        print("Nameserver doesn't exist.")

#get_nameservers('google.com')
