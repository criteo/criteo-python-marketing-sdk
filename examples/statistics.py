import re
import sys

import criteo_marketing as cm
from criteo_marketing import Configuration

GRANT_TYPE = 'client_credentials'

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError("You need to specify the CLIENT_ID and the CLIENT_SECRET")

    configuration = Configuration()
    configuration.username = sys.argv[1]
    configuration.password = sys.argv[2]

    client = cm.ApiClient(configuration)

    auth_api = cm.AuthenticationApi(client)
    auth_response = auth_api.o_auth2_token_post(client_id=client.configuration.username,
                                                client_secret=client.configuration.password,
                                                grant_type=GRANT_TYPE)
    token = auth_response.token_type + " " + auth_response.access_token

    stats_api = cm.StatisticsApi(client)
    stats_query_message = cm.StatsQueryMessageEx(
        report_type="CampaignPerformance",
        dimensions=["CampaignId"],
        metrics=["Clicks"],
        start_date="2019-01-01",
        end_date="2019-01-31",
        format="Csv")

    # Use the method with 'with_http_info' if you want to retrieve the filename
    # Otherwise, you can directly call the get_stats method and write the return value to a file
    [response_content, http_code, response_headers] = stats_api.get_stats_with_http_info(token, stats_query_message)
    if 200 == http_code:
        content_disposition = response_headers["Content-Disposition"]
        if content_disposition:
            filename = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?', content_disposition).group(1)

            # $> file Extract_20190101_20190131.csv
            # Extract_20190101_20190131.csv: UTF-8 Unicode (with BOM) text, with CRLF line terminators
            with open(filename, "w+") as f:
                f.write(response_content)
