"""Invoice Type Defs"""

import graphene


class InvoiceInput(graphene.InputObjectType):
    """Invoice GraphQL Input"""
    amount = graphene.NonNull(graphene.Float, name='amount')
    created_at = graphene.NonNull(graphene.String, name='created_at')
    limit_date = graphene.NonNull(graphene.String, name='limit_date')
    payment_id = graphene.Int(name='payment_id')
    state = graphene.NonNull(graphene.Int, name='state')

class Invoice(graphene.ObjectType):
    """Invoice GraphQL Type"""
    id = graphene.ID(name='id')
    account_id = graphene.NonNull(graphene.String, name='account_id')
    amount = graphene.NonNull(graphene.Float, name='amount')
    created_at = graphene.NonNull(graphene.String, name='created_at')
    limit_date = graphene.NonNull(graphene.String, name='limit_date')
    payment_id = graphene.Int(name='payment_id')
    state = graphene.NonNull(graphene.Int, name='state')
