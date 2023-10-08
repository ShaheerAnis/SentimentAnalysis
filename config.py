
class Config:
    SESSION_PERMANENT = True
    SESSION_USE_SIGNER = True
    SECRET_KEY = 'your-secret-key'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_KEY_PREFIX = 'your_prefix:'
    SESSION_COOKIE_SECURE = True  # Requires HTTPS
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=DRIVER%3D%7BSQL+Server+Native+Client+11.0%7D%3BServer%3DDESKTOP-RGGQBCN%5CSQLEXPRESS%3BDatabase%3DSentimentAnalysis%3BTrusted_Connection%3Dyes%3BPort%3D1433"
    