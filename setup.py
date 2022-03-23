try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description' : 'Supernatural Python Text Game',
	'author' : 'Emily LS',
	'url' : 'url_to_get_it',
	'download_url': 'url_to_download_it',
	'author_email': 'emily.lindsay21@gmail.com'
	'version' : '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts' : [],
	'name' : 'supernaturalgame'
}

setup(**config)

