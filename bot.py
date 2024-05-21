import os
import random
import vk_api

from datetime import datetime

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType

from core import get_random_anek

COMMUNITY_ID = int(os.getenv("COMMUNITY_ID", 0))
BOT_TOKEN = os.getenv('BOT_TOKEN')

def main():
        if not BOT_TOKEN:
            print("BOT_TOKEN is not provided, exiting")
            exit(1)

        bot_session = vk_api.VkApi(token=BOT_TOKEN)
        VK = bot_session.get_api()

        while True:
            longpoll = VkBotLongPoll(bot_session, COMMUNITY_ID)
            for event in longpoll.listen():
                # print(event)
                if event.type == VkBotEventType.MESSAGE_NEW:
                    # print(event)
                    if event.chat_id is None:
                        continue
                    def answer(message: str, attachment: str=None):
                        VK.messages.send(
                            random_id=random.randint(1, 10000000000),
                            message=message,
                            chat_id=event.chat_id,
                            attachment=attachment
                        )

                    text = event.object["message"].get("text", "").lower()
                    if "анек" in text or "юмор" in text:
                        try:
                            anek = get_random_anek(funny_only=True)
                        except Exception as e:
                            print(str(e))
                            answer(f'Ничего себе! ({str(e)})')
                            continue

                        text = anek.get('text')
                        date = anek.get('date')
                        likes = anek.get('likes', {}).get('count')
                        attachments = anek.get('attachments')
                        attachment = None
                        if not text:
                            answer('Сегодня без анека =)')
                            continue
                        if attachments is not None:
                            attachment = ','.join(f'{x["type"]}{x[x["type"]]["owner_id"]}_{x[x["type"]]["id"]}' for x in attachments)

                        d = datetime.utcfromtimestamp(date).strftime('%d.%m.%Y')
                        message = f'[{likes} лайков]\n{text}\n\n{d}'

                        try:
                            answer(message, attachment)
                        except Exception as e:
                            print(str(e))
                            answer(f'Ничего себе! ({str(e)})')


if __name__ == '__main__':
    main()
