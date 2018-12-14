from __future__ import print_function

import sys
from pprint import pprint

import criteo_marketing
from criteo_marketing import Configuration

# There is only one accepted GRANT_TYPE
GRANT_TYPE = 'client_credentials'


def get_token(client):
    auth_api = criteo_marketing.AuthenticationApi(client)
    token = auth_api.o_auth2_token_post(client_id=marketing_client.configuration.username,
                                        client_secret=marketing_client.configuration.password,
                                        grant_type=GRANT_TYPE)
    return token.token_type + " " + token.access_token


def get_advertisers_campaigns(client, token=''):
    advertisers = criteo_marketing.AdvertisersApi(client)
    advertiser_id = 45749

    api_response = advertisers.get_campaigns(advertiser_id, token)
    pprint(api_response)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError("You need to specify the CLIENT_ID and the CLIENT_SECRET")

    configuration = Configuration()
    configuration.username = sys.argv[1]
    configuration.password = sys.argv[2]

    marketing_client = criteo_marketing.ApiClient(configuration)

    valid_token = get_token(marketing_client)

    get_advertisers_campaigns(marketing_client, valid_token)
