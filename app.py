from app import app

print(app.config['SQLALCHEMY_DATABASE_URI'])
if __name__ == "__main__":
    app.run(debug=True)
