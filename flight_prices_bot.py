import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('RAPIDAPI_FLIGHTS_URL')
token = os.getenv('RAPIDAPI_FLIGHTS_TOKEN')
host = os.getenv('RAPIDAPI_FLIGHTS_HOST')

# Number of passengers
adults=3
#children=0
#infants=0

# Source/Destination
# For cities, use format 'City:city-name_statecode_countrycode' (e.g., 'City:buenos-aires_ba_ar')
# For countries, use format 'Country:countrycode' (e.g., 'Country:AR')
# Source and destination can be combined for displaying multiple options, by separating with commas. (e.g., 'City:miami_fl_us,Country:US')
source="City:buenos-aires_ba_ar"
destination="miami_fl_us"

# Dates - use format 'YYYY-MM-DDTHH:MM:SS'
outbound_start_date="2026-07-20T00:00:00"
outbound_end_date="2026-07-31T00:00:00"
#inbound_start_date="2026-08-10T00:00:00"
#inbound_end_date="2026-08-20T00:00:00"

# Bags
handbags=1
holdbags=1

# Cabin class:  ECONOMY,ECONOMY_PREMIUM,BUSINESS,FIRST_CLASS
cabinClass="ECONOMY"

# Price filters
minPrice=100
maxPrice=800

# Sort by options and query limit: Sort by QUALITY,PRICE,DURATION,SOURCE_TAKEOFF,DESTINATION_LANDING. Limit is the maximum number of results to return.
sortBy="PRICE"
sortOrder="ASCENDING" # or DESCENDING
limit=20

# Maximum stops count: 0 for non-stop, 1 for one stop, etc.
maxStopsCount=0

# Outbound days of the week: Comma-separated list of days (e.g., "MONDAY,TUESDAY,WEDNESDAY")
outboundDaysOfWeek="SUNDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,MONDAY,TUESDAY"

# Apply mixed classes: true or false depending on whether you want to allow mixed cabin classes in the search results
applyMixedClasses="true"

# Allow return from different city: true or false depending on whether you want to allow return flights from a different city
allowReturnFromDifferentCity="true"

# Allow change inbound source/destination: true or false depending on whether you want to allow changes to inbound source/destination
allowChangeInboundDestination="true"
allowChangeInboundSource="true"

# Allow different station connection: true or false depending on whether you want to allow connections through different stations
allowDifferentStationConnection="true"

# Enable self transfer: true or false depending on whether you want to enable self-transfer options
enableSelfTransfer="true"

# Allow overnight stopover: true or false depending on whether you want to allow overnight stopovers
allowOvernightStopover="true"

# Enable true hidden city: true or false depending on whether you want to enable true hidden city options. 
# True hidden city ticketing involves booking a flight with a layover in the desired destination and then not taking the final leg of the journey. Not all airlines allow this practice.
enableTrueHiddenCity="false"

# Enable throw away ticketing: true or false depending on whether you want to enable throw away ticketing options. 
# Throw away ticketing involves booking a flight with a layover in the desired destination and then discarding the final leg of the journey. Not all airlines allow this practice.
enableThrowAwayTicketing="false"



# Construct querystring
querystring = {"source":source,
               "destination":destination,
               "currency":"usd",
               "locale":"en_US",
               "adults":str(adults),
               #"children":str(children),
               #"infants":str(infants),
               "handbags":str(handbags),
               "holdbags":str(holdbags),
               "cabinClass":cabinClass,
               "sortBy":sortBy,
               "sortOrder":sortOrder,
               "applyMixedClasses":applyMixedClasses,
               "allowReturnFromDifferentCity":allowReturnFromDifferentCity,
               "allowChangeInboundDestination":allowChangeInboundDestination,
               "allowChangeInboundSource":allowChangeInboundSource,
               "allowDifferentStationConnection":allowDifferentStationConnection,
               "enableSelfTransfer":enableSelfTransfer,
               "allowOvernightStopover":allowOvernightStopover,
               "enableTrueHiddenCity":enableTrueHiddenCity,
               "enableThrowAwayTicketing":enableThrowAwayTicketing,
               "priceStart":str(minPrice),
               "priceEnd":str(maxPrice),
               "maxStopsCount":str(maxStopsCount),
               "outbound":outboundDaysOfWeek,
               "transportTypes":"FLIGHT",
               "contentProviders":"FLIXBUS_DIRECTS,FRESH,KAYAK,KIWI",
               "limit":str(limit),
               "outboundDepartmentDateStart":outbound_start_date,
               "outboundDepartmentDateEnd":outbound_end_date
               #"inboundDepartureDateStart":inbound_start_date,
               #"inboundDepartureDateEnd":inbound_end_date
}

# Sample querystring with all options included
'''
querystring = {"source":"City:buenos-aires_ba_ar",
               "destination":"City:miami_fl_us",
               "currency":"usd",
               "locale":"en_US",
               "adults":"1",
               "children":"1",
               "infants":"1",
               "handbags":"1",
               "holdbags":"1",
               "cabinClass":"ECONOMY",
               "sortBy":"QUALITY",
               "sortOrder":"ASCENDING",
               "applyMixedClasses":"true",
               "allowReturnFromDifferentCity":"true",
               "allowChangeInboundDestination":"true",
               "allowChangeInboundSource":"true",
               "allowDifferentStationConnection":"true",
               "enableSelfTransfer":"true",
               "allowOvernightStopover":"true",
               "enableTrueHiddenCity":"false",
               "enableThrowAwayTicketing":"false",
               "priceStart":"100",
               "priceEnd":"1000",
               "maxStopsCount":"0",
               "outbound":"SUNDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,MONDAY,TUESDAY",
               "transportTypes":"FLIGHT",
               "contentProviders":"FLIXBUS_DIRECTS,FRESH,KAYAK,KIWI",
               "limit":"20",
               "inboundDepartureDateStart":"2026-07-22T00:00:00",
               "inboundDepartureDateEnd":"2026-07-30T00:00:00",
               "outboundDepartmentDateStart":"2026-08-05T00:00:00",
               "outboundDepartmentDateEnd":"2026-08-15T00:00:00"
}
'''

headers = {
	"x-rapidapi-key": f"{token}",
	"x-rapidapi-host": f"{host}"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())