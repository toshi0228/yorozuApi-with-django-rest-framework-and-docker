import uuid
from django.db import models
from django.utils import timezone
from .profile import Profile


class Request(models.Model):
    '''リクエストメッセージのモデル(本契約の前のリクエスト)'''

    class Meta:
        verbose_name_plural = 'リクエスト(仮契約)'

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    sender_yorozu_id = models.ForeignKey(
        "Profile", verbose_name="リクエスト送信者", on_delete=models.CASCADE, related_name="request_sender")

    receiver_yorozu_id = models.ForeignKey(
        "Profile", verbose_name="リクエスト受信者", on_delete=models.CASCADE, related_name="request_receiver")

    # リクエスト受信者(よろず屋)が承認したかどうか
    isApproval = models.BooleanField(verbose_name='リクエストの承認状態', default=False)

    created_at = models.DateTimeField("作成日", default=timezone.now)

    updated_at = models.DateField("更新日", auto_now=True)

    def __str__(self):
        return f'送り主:{self.sender_yorozu_id} 受信者:{self.receiver_yorozu_id}'
