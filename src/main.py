import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

api_token = "90b54d3d736030ed7444d4b905adaecff7b896653ff71c4dd58e6d0d0bc85f37dd0e20a07546fd1a5a693"
vk_session = vk_api.VkApi(token=api_token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == "как дела?" or event.text == "чо как":
            if event.from_chat():
                vk.message_send(chat_id=event.chat_id, message="Всё путем, чувак")
