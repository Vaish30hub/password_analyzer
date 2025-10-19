import hashlib
import requests

def hash_password(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

def check_breach(password):
    """
    Check if password has been exposed in data breaches.
    Returns: True = Found, False = Not found, None = API error
    """
    if not password or len(password.strip()) == 0:
        return None

    try:
        
        sha1_hash = hash_password(password.strip())
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]

      
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        headers = {
            'User-Agent': 'MyPasswordApp v1.0'
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        
        for line in response.text.splitlines():
            h = line.split(':')[0]
            if h == suffix:
                return True  
        return False  

    except requests.exceptions.Timeout:
        return None
    except requests.exceptions.ConnectionError:
        return None
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None

