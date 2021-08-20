# import os

# class Config:
   
#     SECRET_KEY = "MARY102"
#     # # UPLOAD_PHOTOS_DEST = 'app/static/photos'
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


# class ProdConfig(Config):
#     SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://marynjeri:njeri2018@localhost/pitches'

# class DevConfig(Config):
    
#     DEBUG = True

# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig
# }