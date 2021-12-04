"""Schema"""

# Utilities
import graphene

# Crowstream API Gateway
from .user import *
from .support import *


class Query(
    user.account.resolvers.Query,
    user.profile.resolvers.Query,
    support.post.resolvers.Query, 
    support.support_request.resolvers.Query
):
    """Class to join all query resolvers in a simple class."""
    pass


class Mutation(
    user.account.resolvers.Mutation,
    user.profile.resolvers.Mutation,
    support.post.resolvers.Mutation,
    support.support_request.resolvers.Mutation
):
    """Class to join all mutations resolvers in a simple class."""
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
