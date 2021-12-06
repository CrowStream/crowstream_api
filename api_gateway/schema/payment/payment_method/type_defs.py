"""Payment Method Type Defs"""

import graphene


class PaymentMethodInput(graphene.InputObjectType):
    """Payment Method GraphQL Input"""
    gift_card_id = graphene.Int(name='gift_card_id')
    card_number = graphene.String(name='card_number')
    card_expiry_date = graphene.String(name='card_expiry_date')
    card_security_number = graphene.String(name='card_security_number')

class PaymentMethod(graphene.ObjectType):
    """Payment Method GraphQL Type"""
    id = graphene.ID(name='id')
    account_id = graphene.NonNull(graphene.String, name='account_id')
    gift_card_id = graphene.Int(name='gift_card_id')
    card_number = graphene.String(name='card_number')
    card_expiry_date = graphene.String(name='card_expiry_date')
    card_security_number = graphene.String(name='card_security_number')
