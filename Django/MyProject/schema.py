import graphene
from webapp.schema import Query as Song_query

class Query(Song_query):

    pass

schema = graphene.Schema(query=Query)
