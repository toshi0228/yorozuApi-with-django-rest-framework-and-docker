from django.urls import path, include
from yorozu.api import profile, account, message, review, tag, contract, plan, payment


# ======================================================================
# router
# router.register('register', views.AccountViewSet)
# router.register()の引数がurlになる エンドポイントになる
# ex)
# http://127.0.0.1:8081/account/register/
# ======================================================================


app_name = 'yorozu'

urlpatterns = [
    path('account/', account.AccountCreateAPIView.as_view(), name='accountCreate'),
    path('account/<pk>/', account.AccountRetrieveAPIView.as_view()),
    path('profile/', profile.ProfileListCreateAPIView.as_view(), name='profile-list'),
    path('profile/<pk>/', profile.ProfileRetrieveAPIView.as_view()),
    # path('profile/search/', profile.SearchProfileAPIView.as_view()),
    path('search/profile/', profile.SearchProfileAPIView.as_view()),
    path('plan/', plan.PlanListCreateAPIView.as_view(), name='plan'),
    path('plan/<pk>/', plan.PlanRetrieveUpdateAPIView.as_view()),
    path('plan/tag/<pk>/', plan.PlanTagUpdateAPIView.as_view()),
    path('message/', message.MessageListCreateAPIView.as_view(),
         name='sent-message-list'),
    path('messagebox/', message.MessageInBoxListAPIView.as_view()),
    path('review/', review.ReviewListAPIView.as_view()),
    path('review/<pk>', review.ReviewRetrieveAPIView.as_view()),
    path('payment/', payment.PaymentAPIView.as_view()),
    path('payment/customer', payment.CreatePaymentCustomer.as_view()),


    # path('profile/<pk>/', profile.ProfileRetrieveAPIView.as_view()),
    path('tag/', tag.TagListAPIView.as_view(), name='tag-list'),
    # 自分のプランを購入してくれたリスト
    path('contract/', contract.ReceiveContractListCreateAPIView.as_view()),
    # 自分がプランを購入してリスト(課金している人)
    path('contract/me/', contract.MySentContractListAPIView.as_view()),
]


# ===============================================================================
# app_nameに関して
# app_name = includeされたアプリ側の urls.py で指定するプロジェクトにおける名前空間
# app_name = 'yorozu'と書いておけば、testでurlを呼び出すときに、
# reverse('yorozu:accountCreate') のように参照できるようになる。
# 上記では yorozu/ 配下のURLは "yorozu" という名前空間になります。
# ===============================================================================
