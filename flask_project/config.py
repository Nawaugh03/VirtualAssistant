class Config:
    SECRET_KEY = 'your_secret_key'
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # Production settings, like database URI

class DevelopmentConfig(Config):
    DEBUG = True
    # Development settings, like SQLite or local resources
