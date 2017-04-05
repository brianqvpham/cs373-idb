from app import db, create_app
from store import store

with create_app().app_context():
    print([x.country for x in store.Organization().get()])


