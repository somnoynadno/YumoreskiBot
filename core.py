import os
import vk

from random import randint
from time import sleep


FUNNY_THRESHOLD = 2000
SLEEP_INTERVAL = 0.5

token = os.getenv('ACCESS_TOKEN')
session = vk.Session(access_token=token) 
vk_api = vk.API(session)


def get_random_anek(funny_only=False):
	while True:
		sleep(SLEEP_INTERVAL) # prevent vk.exceptions.VkAPIError: Too many requests per second

		count = vk_api.wall.get(v=5.81, domain='https://vk.com/jumoreski', owner_id=-92876084, count=1)["count"]

		c = randint(0, count)
		r = vk_api.wall.get(v=5.81, domain='https://vk.com/jumoreski', owner_id=-92876084, count=1, offset=c)

		if len(r['items']) == 0:
			continue

		r = r['items'][0]

		if not funny_only:
			return r
		elif r["likes"]["count"] > FUNNY_THRESHOLD:
			return r
