import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://josedom24:usuario1234@josedom24.mysql.pythonanywhere-services.com/josedom24$tienda'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://LuisSL.mysql.pythonanywhere-services.com/LuisSL$Video'


#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False
