"""Payment Resolvers"""

import graphene
import requests
import os

from .type_defs import PaymentInput, Payment

USER_MS_URL = os.getenv('USER_MS_URL')
PAYMENT_MS_URL = os.getenv('PAYMENT_MS_URL')


class Query(graphene.ObjectType):
    """Payment query resolvers"""
    retrieve_payment_by_id = graphene.Field(Payment, payment_id=graphene.ID(name='payment_id'))
    retrieve_payments_by_account_id = graphene.NonNull(graphene.List(Payment))

    def resolve_retrieve_payment_by_id(parent, info, payment_id):
        response = requests.get(f'{PAYMENT_MS_URL}/payments/{payment_id}').json()
        if 'id' not in response.keys():
            return None
        return response
    
    def resolve_retrieve_payments_by_account_id(parent, info):
        token = info.context.META.get('HTTP_AUTHORIZATION')
        user_data = requests.get(f'{USER_MS_URL}/whoAmI/', headers={'Authorization': token}).json()
        data = {'account_id': user_data['id']}
        return requests.get(f'{PAYMENT_MS_URL}/payments', params=data).json()


class CreatePayment(graphene.Mutation):
    """Create Payment Mutation"""
    payment = graphene.Field(Payment, required=True)

    class Arguments:
        """Mutation arguments"""
        payment = PaymentInput(required=True)
    
    @staticmethod
    def mutate(root, info, payment=None):
        """Mutation"""
        token = info.context.META.get('HTTP_AUTHORIZATION')
        user_data = requests.get(f'{USER_MS_URL}/whoAmI/', headers={'Authorization': token}).json()
        payment['account_id'] = user_data['id']
        response = requests.post(f'{PAYMENT_MS_URL}/payments', json=payment).json()
        return CreatePayment(payment=Payment(
            id = response['id'],
            account_id = response['account_id'],
            method_id = response['method_id'],
            amount_applied = response['amount_applied'],
            payment_date = response['payment_date'],
            description = response['description'],
            status = response['status']
        ))


class UpdatePayment(graphene.Mutation):
    """Update Payment Mutation"""
    payment = graphene.Field(Payment, required=True)

    class Arguments:
        """Mutation arguments"""
        payment_id = graphene.ID(required=True)
        payment = PaymentInput(required=True)
    
    @staticmethod
    def mutate(root, info, payment_id=None, payment=None):
        """Mutation"""
        response = requests.put(f'{PAYMENT_MS_URL}/payments/{payment_id}', json=payment).json()
        return UpdatePayment(payment=Payment(
            id = response['id'],
            account_id = response['account_id'],
            method_id = response['method_id'],
            amount_applied = response['amount_applied'],
            payment_date = response['payment_date'],
            description = response['description'],
            status = response['status']
        ))


class DeletePayment(graphene.Mutation):
    """Delete Payment Mutation"""
    boolean = graphene.Field(graphene.Boolean)

    class Arguments:
        """Mutation arguments"""
        payment_id = graphene.ID(required=True)
    
    @staticmethod
    def mutate(root, info, payment_id=None):
        """Mutation"""
        request = requests.delete(f'{PAYMENT_MS_URL}/payments/{payment_id}')
        if request.status_code == 200:
            return DeletePayment(boolean=True)
        return DeletePayment(boolean=False)


class Mutation(graphene.ObjectType):
    create_payment = CreatePayment.Field()
    update_payment = UpdatePayment.Field()
    delete_payment = DeletePayment.Field()
