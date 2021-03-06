import graphene

import ingredients.schema
import users.schema

class Query(ingredients.schema.Query,users.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(users.schema.Mutation, graphene.ObjectType,):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)