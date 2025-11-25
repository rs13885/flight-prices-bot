import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('RAPIDAPI_FLIGHTS_URL')
token = os.getenv('RAPIDAPI_FLIGHTS_TOKEN')
host = os.getenv('RAPIDAPI_FLIGHTS_HOST')


adults=input("Number of adults: ")
children=input("Number of children: ")
infants=input("Number of infants: ")


querystring = {"source":"Country:AR",
               "destination":"City:barcelona_es",
               "currency":"usd",
               "locale":"en",
               "adults":"1",
               "children":"0",
               "infants":"0",
               "handbags":"1",
               "holdbags":"0",
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
               "enableTrueHiddenCity":"true",
               "enableThrowAwayTicketing":"true",
               "outbound":"SUNDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,MONDAY,TUESDAY",
               "transportTypes":"FLIGHT",
               "contentProviders":"FLIXBUS_DIRECTS,FRESH,KAYAK,KIWI",
               "limit":"20"}

headers = {
	"x-rapidapi-key": f"{token}",
	"x-rapidapi-host": f"{host}"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())