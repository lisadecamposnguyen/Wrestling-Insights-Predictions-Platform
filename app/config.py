import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL","sqlite:///local.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCRAPING_ENABLED = os.getenv("SCRAPING_ENABLED","1") == "1"
    MODEL_PATH = os.getenv("MODEL_PATH","/mnt/model.joblib")