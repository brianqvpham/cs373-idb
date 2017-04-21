from sqlalchemy import or_, and_
from models import Organization, OrganizationSchema, OrganizationSchemaNested, Country, CountrySchema, CountrySchemaNested, Article, ArticleSchema, ArticleSchemaNested

class DBStore():
    def get(self, Model, Schema, id, **args):
        if(id):
            resource = Model.query.get(id)
            schema = Schema()
        else:
            resource = Model.query.all()
            schema = Schema(many=True)
            page = args.get('page')
            limit = args.get('limit')
            first = page * limit
            resource = resource[first:first+limit]
        return schema.dump(resource).data

    def search(self, Model, schema, andf, orf):
        ands = schema.dump(Model.query.filter(andf).all()).data
        andIds = [x["id"] for x in ands]
        ors = schema.dump(Model.query.filter(orf).all()).data
        ors = [x for x in ors if x["id"] not in andIds]
        return {
            "and": ands,
            "or": ors
        }

class OrganizationStore(DBStore):
    def get(self, id=None, **args):
        if(id):
            schema = OrganizationSchemaNested
        else:
            schema = OrganizationSchema
        return super().get(Organization, schema, id, **args)

    def search(self, words):
        andf = and_(*[Organization.name.ilike('%{}%'.format(x)) for x in words])
        orf = or_(*[Organization.name.ilike('%{}%'.format(x)) for x in words])
        return super().search(Organization, OrganizationSchema(many=True), andf, orf)

class CountryStore(DBStore):
    def get(self, id=None, **args):
        if(id):
            schema = CountrySchemaNested
        else:
            schema = CountrySchema
        return super().get(Country, schema, id, **args)

    def search(self, words):
        andf = and_(*[Country.name.ilike('%{}%'.format(x)) for x in words])
        orf = or_(*[Country.name.ilike('%{}%'.format(x)) for x in words])
        return super().search(Country, CountrySchema(many=True), andf, orf)

class ArticleStore(DBStore):
    def get(self, id=None, **args):
        if(id):
            schema = ArticleSchemaNested
        else:
            schema = ArticleSchema
        return super().get(Article, schema, id, **args)

    def search(self, words):
        andf = or_(
                    and_((*[Article.title.ilike('%{}%'.format(x)) for x in words])),
                    and_((*[Article.description.ilike('%{}%'.format(x)) for x in words])),
                )

        orf = or_(
                    (*[Article.title.ilike('%{}%'.format(x)) for x in words]),
                    (*[Article.description.ilike('%{}%'.format(x)) for x in words]),
                )
        return super().search(Article, ArticleSchema(many=True), andf, orf)

