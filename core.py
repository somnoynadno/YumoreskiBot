import os
import vk

from random import randint


token = os.getenv('ACCESS_TOKEN')
session = vk.Session(access_token=token) 
vk_api = vk.API(session)


def get_random_anek():
	count = vk_api.wall.get(v=5.81, domain='https://vk.com/jumoreski', owner_id=-92876084, count=1)["count"]

	c = randint(0, count)
	r = vk_api.wall.get(v=5.81, domain='https://vk.com/jumoreski', owner_id=-92876084, count=1, offset=c)

	return r
