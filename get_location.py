import os
import googlemaps

api_key = 'AIzaSyB8EdFp_2A-7eDNsCeUp_iPTubMfxVClsY'
gm = googlemaps.Client(key=api_key)
geocode_result = gm.geocode('scranton')[0]
print(geocode_result)
