"""Gift Card Type Defs"""

from os import name
import graphene


class GiftCardInput(graphene.InputObjectType):
    """Gift Card GraphQL Input"""
    card_code = graphene.NonNull(graphene.String, name='card_code')
    amount = graphene.NonNull(graphene.Float, name='amount')
    is_active = graphene.NonNull(graphene.Boolean, name='is_active')
    expiration_date = graphene.NonNull(graphene.String, name='expiration_date')

class GiftCard(graphene.ObjectType):
    """Gift Card GraphQL Type"""
    id = graphene.ID(name='id')
    card_code = graphene.NonNull(graphene.String, name='card_code')
    amount = graphene.NonNull(graphene.Float, name='amount')
    is_active = graphene.NonNull(graphene.Boolean, name='is_active')
    expiration_date = graphene.NonNull(graphene.String, name='expiration_date')
