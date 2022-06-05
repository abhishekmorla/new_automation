import shodan
SHODAN_API_KEY = "your_api_key" # edit the "your_api_key"

api = shodan.Shodan(SHODAN_API_KEY)
limit = 2000 # set the limit according to your query credits
counter = 0

try:
    # Search Shodan
    # Show the results

    for result in api.search_cursor('your_shodan_dork'): # edit the "your_shodan_dork"
        print '%s' % result['ip_str']
        counter += 1
        if counter >= limit:
            break

except shodan.APIError as e:
    print('Error: %s' % e)
