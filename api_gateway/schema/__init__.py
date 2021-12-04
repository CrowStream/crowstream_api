import graphene
from .user import *
from .support import *

import graphene


class Query(user.account.resolvers.Query, support.post.resolvers.Query, support.support_request.resolvers.Query):
    pass

schema = graphene.Schema(query=Query)