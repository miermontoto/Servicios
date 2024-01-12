from pyfcm import FCMNotification
from .models import Amigo

push_service = FCMNotification(api_key="AAAA4Y2yU6k:APA91bEh-DchVbhPaWhIjGlzxb6kxa83SgZc8t0N3hzKueBXNXPQ_zzj-xD-FshhrccfITwxy2JBvST5EbD02eTqgN6os_LuGHWVa2aSqPkjtTureOIwxq_j6wz8jnOcD8O9aNNwHVYK")


def notificar_amigos(body):
    amigos = Amigo.query.all()
    devices = [amigo.device for amigo in amigos]
    print("Enviando notificación a", devices)
    push_service.notify_multiple_devices(registration_ids=devices, message_body=body, message_title="Amigos")
