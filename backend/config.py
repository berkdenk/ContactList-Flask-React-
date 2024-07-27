from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

''' Python'da mevcut modülün adını belirtir. Bu, Flask'ın uygulamanın dosya adını ve 
konumunu kullanarak bir çalışma kök dizinini belirlemesine ve gerekli dosyaları bulmasına olanak tanır.'''
app=Flask(__name__)
'''CORS işlemi, sunucu tarafında yapılandırılmalıdır. Flask uygulamasında, flask_cors modülü kullanılarak 
bu işlem gerçekleştirilir. CORS(app) ifadesi, Flask uygulamasının CORS 
ayarlarını yapılandırmak için flask_cors modülünün CORS sınıfını kullanır.
 Bu, Flask uygulamasının tüm rotalarına CORS kurallarını uygulamak için gereklidir.'''
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#create a database instant and give us a access 'sqlite:///mydatabase.db'
db=SQLAlchemy(app)
