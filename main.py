import os
import json
import vk  

from flask import Flask
from flask_cors import CORS, cross_origin

from random import randint


""" CORE """

token = os.getenv('ACCESS_TOKEN')
session = vk.Session(access_token=token) 
vk_api = vk.API(session)


def get_count():
	r = vk_api.wall.get(v=5.54, domain='https://vk.com/jumoreski', owner_id=-92876084, count=1)

	return r["count"]


def get_random_anek(count):
	c = randint(0, count)
	r = vk_api.wall.get(v=5.54, domain='https://vk.com/jumoreski', owner_id=-92876084, count=1, offset=c)

	return r["items"][0]["text"]


""" COUNTROLLER """

stub = Flask(__name__)
cors = CORS(stub)


@stub.route('/random_anek')
@cross_origin()
def random_anek(methods=['GET']):
	c = get_count()
	anek = get_random_anek(c)

	return anek


if __name__ == "__main__":
	stub.run(host="0.0.0.0", port=7777, debug=False)