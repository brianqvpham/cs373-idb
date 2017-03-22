from app.app import db, create_app
from app.models import Source

with create_app().app_context():
    db.drop_all()
    db.create_all()
    db.session.add(s)
    db.session.commit()
    print(Source.query.all())


