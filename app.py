from flask import Flask, render_template
from flask_cors import CORS
from config import Config
from models import db
from routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    
    # 初始化数据库
    db.init_app(app)
    
    # 注册蓝图
    app.register_blueprint(user_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)