## Python Flask Template

### The stack

1. python - runtime
2. flask - Framework
3. SqlAlchemy - ORM
4. postgres - DB

---

## Configuration

In order to run the server, there is config.py in the repo.

## Installation

## How To Run

1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

4. Then create local db: 
```
$ python
$ >>> from app.db_util import db
$ >>> db.create_all()
$ >>> exit()
```

5. Finally start the web server:
```
$ (env) python app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```