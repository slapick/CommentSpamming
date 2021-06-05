import vk_api, json, time, random

with open('config.json', 'r', encoding = "utf-8") as f:
    data = json.load(f)

token = data['token']
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

owner_iddd = data["owner_id"]
post_iddd = data["post_id"]
delay = data["delay"]
message = data["text"]
number = data["number"]

def main():
    for i in range(number):
        try:
            rndm = random.randint(0, len(message) - 1)
            print(rndm)
            vk.wall.createComment(owner_id=owner_iddd, post_id=post_iddd, message=message[rndm])
            print(f"Оставлен коммент: {message[rndm]}")
        except Exception as e:
            print(repr(e))
            print("Комментарий не оставлен!")
        time.sleep(delay)
    print(f"Накрутка закончена! ({i + 1} комментариев)")

if __name__ == "__main__":
    main()