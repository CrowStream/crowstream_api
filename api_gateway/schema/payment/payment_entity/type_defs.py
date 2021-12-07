"""Payment Type Defs"""

import graphene


class PaymentInput(graphene.InputObjectType):
    """Payment GraphQL Input"""
    method_id = graphene.NonNull(graphene.Int, name='method_id')
    amount_applied = graphene.NonNull(graphene.Float, name='amount_applied')
    payment_date = graphene.NonNull(graphene.String, name='payment_date')
    description = graphene.String(name='description')
    status = graphene.NonNull(graphene.Int, name='status')

class Payment(graphene.ObjectType):
    """Payment GraphQL Type"""
    id = graphene.ID(name='id')
    account_id = graphene.NonNull(graphene.String, name='account_id')
    method_id = graphene.NonNull(graphene.Int, name='method_id')
    amount_applied = graphene.NonNull(graphene.Float, name='amount_applied')
    payment_date = graphene.NonNull(graphene.String, name='payment_date')
    description = graphene.String(name='description')
    status = graphene.NonNull(graphene.Int, name='status')
