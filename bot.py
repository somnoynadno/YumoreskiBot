import os
import random
import vk_api

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType

from core import get_random_anek

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
COMMUNITY_ID = int(os.getenv("COMMUNITY_ID", 0))


def main():
        bot_session = vk_api.VkApi(token=BOT_TOKEN)
        VK = bot_session.get_api()

        while True:
            longpoll = VkBotLongPoll(bot_session, COMMUNITY_ID)
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    print(event)

                    text = event.object["message"]["text"].lower()
                    if "анек" in text or "юмор" in text:
                        try:
                            VK.messages.send(
                                random_id=random.randint(1, 10000000000),
                                message=str(get_random_anek()['items'][0]['text']),
                                chat_id=event.chat_id
                            )
                        except Exception as e:
                            print(str(e))
                            VK.messages.send(
                                random_id=random.randint(1, 10000000000),
                                message='Ля, не вышло =(',
                                chat_id=event.chat_id
                            )


if __name__ == '__main__':
    main()
