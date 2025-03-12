import os

from utilities.cf import CloudFlareUtil as cf
from utilities.logger import Logger
from utilities.helper import get_ip

from dotenv import load_dotenv

log = Logger()
load_dotenv()

api_key = os.getenv("CLOUDFLARE_API_KEY", None)
cloudflare_account = os.getenv("CLOUDFLARE_ACCOUNT_ID", None)
zone_id = os.getenv("CLOUDFLARE_ZONE_ID", None)
dns_record_id = os.getenv("CLOUDFLARE_DNS_RECORD_ID", None)
a_record_name = os.getenv("CLOUDFLARE_A_RECORD_NAME", None)

log.info(f"Loaded environment variables from .env file.")
data = {
    "api_key": api_key,
    "cf_account": cloudflare_account,
    "zone_id": zone_id,
    "dns_record_id": dns_record_id,
    "a_record_name": a_record_name
}

cf_client = cf(data)

if cf_client.no_empty_data_values():
    current_ip, ip_status = get_ip()
    if ip_status:
        valid_token = cf_client.verify_token()

        if valid_token:

            update_result = cf_client.update_zone_record(ip=current_ip)

            if update_result:
                log.info(f"Successfully updated zone record ({a_record_name}) with value of: {current_ip}")
            else:
                log.failure(f"Failed to update zone record ({a_record_name}) with value of: {current_ip}")
    else:
        log.failure("Exiting script due to failure grabbing IP.")
else:
    log.failure(f"A value was empty in the .env file, please fill in all values.")
