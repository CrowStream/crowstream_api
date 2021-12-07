"""Schema"""

# Utilities
import graphene

# Crowstream API Gateway
from .user import *
from .support import *
from .recommendation import *
from .reproduction import *
from .payment import *
from .rating import *
from .catalogue import *


class Query(
    user.account.resolvers.Query,
    recommendation.resolvers.Query, 
    user.profile.resolvers.Query,
    support.post.resolvers.Query, 
    support.support_request.resolvers.Query,
    reproduction.click_metadata.resolvers.Query,
    reproduction.video_metadata.resolvers.Query,
    payment.invoice.resolvers.Query,
    payment.payment_entity.resolvers.Query,
    payment.payment_method.resolvers.Query,
    payment.gift_card.resolvers.Query,
    catalogue.video.resolvers.Query
):
    """Class to join all query resolvers in a simple class."""
    pass


class Mutation(
    user.account.resolvers.Mutation,
    user.profile.resolvers.Mutation,
    support.post.resolvers.Mutation,
    support.support_request.resolvers.Mutation,
    recommendation.resolvers.Mutation,
    reproduction.click_metadata.resolvers.Mutation,
    reproduction.video_metadata.resolvers.Mutation,
    payment.invoice.resolvers.Mutation,
    payment.payment_entity.resolvers.Mutation,
    payment.payment_method.resolvers.Mutation,
    payment.gift_card.resolvers.Mutation,
    rating.likevideo.resolvers.Mutation
):
    """Class to join all mutations resolvers in a simple class."""
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
