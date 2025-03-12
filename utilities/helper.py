import httpx

from utilities.logger import Logger

log = Logger()

def get_ip():
    try:
        request = httpx.get('https://icanhazip.com')
        ip = request.text.rstrip()
        log.info(f"IP address was found to be: {ip}")
        return ip, True
    except:
        log.failure(f"Failed to gather IP address from icanhazip.com.")
        return "0.0.0.0", False