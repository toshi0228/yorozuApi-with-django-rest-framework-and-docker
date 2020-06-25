from django.db import models
from django.utils import timezone
from .profile import Profile


class Review(models.Model):

    class Meta:
        verbose_name_plural = "レビュー"

    # review_content = models.TextField("レビュー内容")

    # review_score = models.IntegerField("評価点数")

    is_positive_score = models.BooleanField(
        verbose_name='ポジティブ得点', default=False)

    is_negative_score = models.BooleanField(
        verbose_name="ネガティブ得点", default=False)

    sender_yorozu_id = models.ForeignKey(
        "Profile", verbose_name="送信者(ユーザー)", on_delete=models.CASCADE, related_name="review_sender", default="")

    receiver_yorozu_id = models.ForeignKey(
        "Profile", verbose_name="受信者(万屋)", on_delete=models.CASCADE, related_name="review_receiver", default="")

    created_at = models.DateTimeField("作成日", default=timezone.now)
    updated_at = models.DateField("更新日", auto_now=True)

    def __str__(self):
        return f'{self.receiver_yorozu_id}:{self.created_at}'


# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# related_nameは、他のmodelのrelated_nameと同じになるとエラーになる
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
