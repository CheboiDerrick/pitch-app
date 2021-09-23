

class Config:
    """
    General configuration parent class
    """

    SQLALCHEMY_DATABASE_URI = (
            "postgresql+psycopg2://moringa:Mjamaica101@localhost/pitchesapp"
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    """
    Production configuration child class
    Args:
        Config: The parent configuration class with Generl configuration settings
    """

    pass


class DevConfig(Config):
    """
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """

    DEBUG = True


config_options = {"development": DevConfig, "production": ProdConfig}