import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
import random
from response import answer, hello

api_token = "0688315e5f32dbf06067e661df17c802b21388116366eeccb7fa8cf4f5a53680dc5ee2cd016d74430c007"
vk_session = vk_api.VkApi(token=api_token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk=vk_session, group_id="174632651")

for event in longpoll.listen():
    to_me = event.message.text.split(" ", 1)[0]
    if (
        event.type.name == "MESSAGE_NEW"
        and event.from_chat
        and to_me == "[club174632651|@smap_l]"
    ):
        text_from_chat = event.message.text.split(" ", 1)[1].lower()
        print(text_from_chat)
        if text_from_chat == "привет" or text_from_chat == "здравствуй":
            if event.from_chat:
                chat_id = event.message.conversation_message_id
                peer_id = event.message.peer_id
                vk.messages.send(
                    message=hello(), random_id=random.getrandbits(32), peer_id=peer_id,
                )

        if text_from_chat == "как дела?" or text_from_chat == "чо как":
            if event.from_chat:
                chat_id = event.message.conversation_message_id
                peer_id = event.message.peer_id
                vk.messages.send(
                    message=answer(), random_id=random.getrandbits(32), peer_id=peer_id,
                )

