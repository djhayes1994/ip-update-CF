# Script for updating an existing A record in CloudFlare's DNS

Updates an A record in a CloudFlare DNS zone.

## Description

Utilizing variables defined in a .env file (use example.env to create) this script will perform the following tasks:

1. It will grab the current external IP address of the host it is running from by making a http request to https://icanhazip.com.
2. It will attempt to verify token validity with CloudFlare
3. If the token is valid an attempt will be made to update the existing DNS record in the DNS Zone in CloudFlare.

This script largely exists for instances where a service is hosted on a server without a static IP.

This should be run on a cron schedule from the server/device that is hosting the service.

## Getting Started

### Dependencies

* httpx
* dotenv
* datetime

### Installing

* Clone the git repo to the server/device running the service.
* Copy the example.env file and name the copy .env
* Fill out the required details such as the API key, Zone ID, DNS Record ID, Record Name, and Account ID.
* Run ```pip install -r requirements.txt```

### Executing program

* To run the script it is recommended that you run it via something like crontab on a set schedule so the IP address is always up to date in CloudFlare.

## Authors

Contributors names and contact info

Daniel Hayes
