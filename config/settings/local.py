from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='go2f!xp5-4qmz$7nyum^2u(_r4_k25o%ys0bv(wz8%sqgnn709')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
