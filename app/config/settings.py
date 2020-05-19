"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g-*=ffi7auc(@po$_q3#n6e&xg%h^r^v4t!5hgoh2o6$#@or08'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'yorozu',
    'corsheaders'
]


# ============================================================
# INSTALLED_APPS
# djangoフレームワークを使う上で必要なINSTALLED_APPS
# rest_framework
# djoser tokenのためのurlを作成 (エンドポイントを作成)
# ============================================================

# ============================================================
# フロントエンドのwebサーバーから、APIアクセルを許可する方法
# todo
# (1)INSTALLED_APPSに'corsheaders'を追加
# (2)MIDDLEWAREに'corsheaders.middleware.CorsMiddleware'を追加
# (3)許可するオリジンを追加 以下の文言をsettingsファイルに追加

# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000',
# ]

# pip install django-core-headers
# ============================================================


# ============================================================
# AUTH_USER_MODEL
# カスタマイズユーザーの設定を反映させるために必要
# なければ、django.adminの時のログインページがusernameのまま
# createsuperuserの設定は変わる。
# アプリケーション名.モデル名
# ============================================================

AUTH_USER_MODEL = 'yorozu.Account'

# ============================================================
# jwtを使う場合の設定
# jwt認証の場合、サードパーティ製のDjangoパーケージを使う。
# (1) pip install djangorestframework-simplejwt
# (2) pip install djoser エンドポイントの作成
# ex)urls.pyに追加
# path('api/auth/', include('djoser.urls.jwt')),
# (3)djangorestframework-simplejwtをdjangoに読み込ませる

# ex)
# http://127.0.0.1:8081/api/auth/jwt/createに
# メールアドレスとpasswordを送るとトークンが帰ってくる
# ============================================================

# ============================================================
# REST_FRAMEWORK
# djangoが標準でサポートしている認証形式を変更する
# DEFAULT_AUTHENTICATION_CLASSES'に# Simple JWTの読み込ませる
# djangoの認証に関して、オーバーライドさせるrイメージだろうか,,,
# ============================================================

# ============================================================
# キャメルケースを、パスカルケースに変換
# pip install djangorestframework-camel-case
# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': (
#         'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
#         'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
#         # Any other renders
#     ),
#     'DEFAULT_PARSER_CLASSES': (
#         # If you use MultiPartFormParser or FormParser, we also have a camel case version
#         'djangorestframework_camel_case.parser.CamelCaseFormParser',
#         'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
#         'djangorestframework_camel_case.parser.CamelCaseJSONParser',
#         # Any other parsers
#     ),
# }
# ============================================================

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # Simple JWTの読み込み
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
        # Any other renders
    ),
    'DEFAULT_PARSER_CLASSES': (
        # If you use MultiPartFormParser or FormParser, we also have a camel case version
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        # Any other parsers
    ),
}

# Simple JWTの設定
SIMPLE_JWT = {
    # トークンをJWTに設定
    'AUTH_HEADER_TYPES': ('JWT',),
    # トークンの持続時間の設定
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60)
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 許可するオリジン
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
]


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "HOST": os.environ.get("DB_HOST"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'
# LANGUAGE_CODE = 'en-us'

# テンプレートファイルに渡す日付は、自動で日本時間(Asia/Tokyo)に変換される
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# ============================================================
# 画像の設定
# static

# STATIC_URL = '/static/'
# 画像を一箇所に集める場所
# 静的ファイル配信用のディレクトリー

# MEDIA_URL = '/media/
# http://127.0.0.1:8000/media/%E3%83%B.jpg
# ============================================================


STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
