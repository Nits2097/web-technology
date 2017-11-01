from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
import csv
client = RecombeeClient('sns', 'cqLZqZnboKlyVKS7EhhYYyM8BflGRDlizngZbljA3kp67tjd1FKfH3WaXLNSXl7F')
ratings=[]
with open('ml-latest-small/ratings.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        user_id = row[0]
        movie_id = row[1]
        interaction = AddDetailView(user_id, movie_id,#optional parameters:
                cascade_create=True
                )
        ratings.append(interaction)


try:
    print('sending')
    client.send(Batch(ratings))
    print('Send')

except APIException as e:
    print(e)