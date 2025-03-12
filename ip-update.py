from utilities.cf import CloudFlareUtil as cf
from utilities.logger import Logger
from utilities.helper import get_ip, var_loader


log = Logger()

data = var_loader()

cf_client = cf(data)

log.info(f'Successfully initialized Cloud Flare client.')

current_ip, ip_status = get_ip()

if not cf_client.no_empty_data_values():
    log.failure(
        f'A value was empty in the .env file, please fill in all values.'
    )
    exit()

if not ip_status:
    exit()

if not cf_client.verify_token():
    log.failure(
        f'Failed to verify CloudFlare token, token is either invalid or there was an error in the request.'
    )
    exit()

if not cf_client.update_zone_record(ip=current_ip):
    log.failure(
        f"Failed to update zone record ({data['a_record_name']}) with value of: {current_ip}"
    )
    exit()

log.info(
    f"Successfully updated zone record ({data['a_record_name']}) with value of: {current_ip}"
)
