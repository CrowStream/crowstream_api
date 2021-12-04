import graphene
from .user import *
from .support import *

import graphene


class Query(support.post.resolvers.Query, user.account.resolvers.Query):
    pass

schema = graphene.Schema(query=Query)