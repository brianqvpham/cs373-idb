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
            offset = int(args.get('offset', 0))
            limit = int(args.get('limit', 10))
            resource = resource[offset:offset+limit]
        return schema.dump(resource).data

    def search(self, Model, schema, andf, orf):
        return {
            "and": schema.dump(Model.query.filter(andf).limit(10).all()).data,
            "or": schema.dump(Model.query.filter(orf).limit(10).all()).data
        }

class OrganizationStore(DBStore):
    def get(self, id=None, **args):
        if(id):
            schema = OrganizationSchemaNested
        else:
            schema = OrganizationSchema
        return super().get(Organization, schema, id, **args)

    def search(self, words):
        andf = and_(*[Organization.name.like('%{}%'.format(x)) for x in words])
        orf = or_(*[Organization.name.like('%{}%'.format(x)) for x in words])
        return super().search(Organization, OrganizationSchema(many=True), andf, orf)

class CountryStore(DBStore):
    def get(self, id=None, **args):
        if(id):
            schema = CountrySchemaNested
        else:
            schema = CountrySchema
        return super().get(Country, schema, id, **args)

    def search(self, words):
        andf = and_(*[Country.name.like('%{}%'.format(x)) for x in words])
        orf = or_(*[Country.name.like('%{}%'.format(x)) for x in words])
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
                    and_((*[Article.title.like('%{}%'.format(x)) for x in words])),
                    and_((*[Article.description.like('%{}%'.format(x)) for x in words])),
                )

        orf = or_(
                    (*[Article.title.like('%{}%'.format(x)) for x in words]),
                    (*[Article.description.like('%{}%'.format(x)) for x in words]),
                )
        return super().search(Article, ArticleSchema(many=True), andf, orf)

