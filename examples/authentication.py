from __future__ import print_function

import logging
import sys
from pprint import pprint

import criteo_marketing
from criteo_marketing import Configuration

# There is only one accepted GRANT_TYPE
GRANT_TYPE = 'client_credentials'

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError("You need to specify the CLIENT_ID and the CLIENT_SECRET")

    configuration = Configuration()
    configuration.username = sys.argv[1]
    configuration.password = sys.argv[2]

    # Enable/Disable debug httplib and criteo_marketing packages
    # logging.basicConfig(level=logging.DEBUG)
    # configuration.debug = True

    client = criteo_marketing.ApiClient(configuration)

    # Get a valid token. The configuration is accessible through the client
    auth_api = criteo_marketing.AuthenticationApi(client)
    auth_response = auth_api.o_auth2_token_post(client_id=client.configuration.username,
                                                client_secret=client.configuration.password,
                                                grant_type=GRANT_TYPE)
    # Token type is always "BEARER"
    token = auth_response.token_type + " " + auth_response.access_token

    # Reuse the same client to benefit from the configuration in order to automatically refresh expired token
    portfolio_api = criteo_marketing.PortfolioApi(client)

    portfolio_response = portfolio_api.get_portfolio(token)
    pprint(portfolio_response)
