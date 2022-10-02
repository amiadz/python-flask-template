from app import app
from app import db_util

db = db_util.db

@app.route('/health-check', methods=['GET'])
def healthy():
    db.engine.execute('SELECT 1')

    return ''