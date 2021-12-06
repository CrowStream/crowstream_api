"""Invoice Type Defs"""

import graphene


class InvoiceInput(graphene.InputObjectType):
    """Invoice GraphQL Input"""
    account_id = graphene.NonNull(graphene.String)
    amount = graphene.NonNull(graphene.Float)
    created_at = graphene.NonNull(graphene.DateTime)
    limit_date = graphene.NonNull(graphene.DateTime)
    payment_id = graphene.Int()
    state = graphene.NonNull(graphene.Int)

class Invoice(graphene.ObjectType):
    """Invoice GraphQL Type"""
    id = graphene.ID(name='id')
    account_id = graphene.NonNull(graphene.String, name='account_id')
    amount = graphene.NonNull(graphene.Float, name='amount')
    created_at = graphene.NonNull(graphene.DateTime, name='created_at')
    limit_date = graphene.NonNull(graphene.DateTime, name='limit_date')
    payment_id = graphene.Int(name='payment_id')
    state = graphene.NonNull(graphene.Int, name='state')
