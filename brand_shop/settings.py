from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '296350859876879726314478182277*o_89n34ivwif75of*t6ds4y&xdm1dq^ucv2@'

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
    'multiselectfield',
	'brand_shops_dashboard',
    
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'brand_shop.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'brand_shops_dashboard' / 'templates'],
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

WSGI_APPLICATION = 'brand_shop.wsgi.application'




# ---------------------------DATABASE CONFIGURATION ----------------------------
# if you want to use sqlite3 database then uncomment below code and comment postgresql code
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}


# <<<<<<<<<<<<<<<< uncomment below code and comment sqlite3 code if you want to use postgresql database >>>>>>>>>>>>>>>>
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql', # change with your database engine name 'django.db.backends.ENGINE_NAME'
#         'NAME': 'DATABASE_NAME',  # change with your database name
#         'USER': 'USER_NAME',      # change with your user name
#         'PASSWORD': 'PASSWORD',   # change with your password
#         'HOST': 'localhost',      # Or an IP Address that your DB is hosted on
#         'PORT': '5432',           # Make sure to change the port number to the correct one for your DB
#     }
# }
# -------------------------END DATABASE CONFIGURATION ----------------------------




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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [
	BASE_DIR / 'brand_shops_dashboard' / 'static',
]



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'