import httpx
import os

from utilities.logger import Logger
from dotenv import load_dotenv

log = Logger()
load_dotenv()


def get_ip():
    try:
        request = httpx.get('https://icanhazip.com')
        ip = request.text.rstrip()
        log.info(f'IP address was found to be: {ip}')
        return ip, True
    except:
        log.failure(f'Failed to gather IP address from icanhazip.com.')
        return '0.0.0.0', False


def var_loader():
    api_key = os.getenv('CLOUDFLARE_API_KEY', None)
    cloudflare_account = os.getenv('CLOUDFLARE_ACCOUNT_ID', None)
    zone_id = os.getenv('CLOUDFLARE_ZONE_ID', None)
    dns_record_id = os.getenv('CLOUDFLARE_DNS_RECORD_ID', None)
    a_record_name = os.getenv('CLOUDFLARE_A_RECORD_NAME', None)

    log.info(f'Loaded environment variables from .env file.')

    return {
        'api_key': api_key,
        'cf_account': cloudflare_account,
        'zone_id': zone_id,
        'dns_record_id': dns_record_id,
        'a_record_name': a_record_name,
    }
