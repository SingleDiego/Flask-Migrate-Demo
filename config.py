class Config(object):
    """基础配置类"""
    pass

class ProdConfig(Config):
    """生产坏境配置"""
    pass

class DevConfig(Config):
    """开发环境配置"""
    DEBUG = True
    # 数据库路径
    SQLALCHEMY_DATABASE_URI = 'sqlite:///my_app.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
