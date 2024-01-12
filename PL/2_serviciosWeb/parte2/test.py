from pyfcm import FCMNotification

push_service = FCMNotification(
                    api_key="AAAA4Y2yU6k:APA91bEh-DchVbhPaWhIjGlzxb6kxa83SgZc8t0N3hzKueBXNXPQ_zzj-xD-FshhrccfITwxy2JBvST5EbD02eTqgN6os_LuGHWVa2aSqPkjtTureOIwxq_j6wz8jnOcD8O9aNNwHVYK")
message_title = "Hola desde Python!"
message_body = "Este mensaje ha sido enviado desde python"

result = push_service.notify_single_device(
                        registration_id=registration_id,
                        message_title=message_title,
                        message_body=message_body)
print(result)
