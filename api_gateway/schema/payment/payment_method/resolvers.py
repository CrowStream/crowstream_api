"""Payment Method Resolvers"""

import graphene
import requests
import os

from .type_defs import PaymentMethodInput, PaymentMethod

USER_MS_URL = f'http://{os.getenv("USER_MS_HOST")}:{os.getenv("USER_MS_PORT")}'
PAYMENT_MS_URL = f'http://{os.getenv("PAYMENT_MS_HOST")}:{os.getenv("PAYMENT_MS_PORT")}'


class Query(graphene.ObjectType):
    """Payment method query resolvers"""
    retrieve_payment_method_by_id = graphene.Field(PaymentMethod)
    retrieve_payment_methods_by_account_id = graphene.NonNull(graphene.List(PaymentMethod))

    def resolve_retrieve_payment_method_by_id(parent, info, method_id):
        token = info.context.META.get('HTTP_AUTHORIZATION')
        user_data = requests.get(f'{USER_MS_URL}/whoAmI/', headers={'Authorization': token}).json()
        response = requests.get(f'{PAYMENT_MS_URL}/payment-methods/{method_id}').json()
        if user_data['id'] != response['account_id']:
            return None
        return response
    
    def resolve_retrieve_payment_methods_by_account_id(parent, info):
        token = info.context.META.get('HTTP_AUTHORIZATION')
        user_data = requests.get(f'{USER_MS_URL}/whoAmI/', headers={'Authorization': token}).json()
        data = {'account_id': user_data['id']}
        return requests.get(f'{PAYMENT_MS_URL}/payment-methods', json=data).json()


class CreatePaymentMethod(graphene.Mutation):
    """Create Payment Method Mutation"""
    method = graphene.Field(PaymentMethod, required=True)

    class Arguments:
        """Mutation arguments"""
        method = PaymentMethodInput(required=True)
    
    @staticmethod
    def mutate(root, info, method=None):
        """Mutation"""
        response = requests.post(f'{PAYMENT_MS_URL}/payment-methods', json=method).json()
        return CreatePaymentMethod(method=PaymentMethod(
            id = response['id'],
            account_id = response['account_id'],
            gift_card_id = response['gift_card_id'],
            card_number = response['card_number'],
            card_expiry_date = response['card_expiry_date'],
            card_security_number = response['card_security_number']
        ))


class UpdatePaymentMethod(graphene.Mutation):
    """Update Payment Method Mutation"""
    method = graphene.Field(PaymentMethod, required=True)

    class Arguments:
        """Mutation arguments"""
        method_id = graphene.ID(required=True)
        method = PaymentMethodInput(required=True)
    
    @staticmethod
    def mutate(root, info, method_id=None, method=None):
        """Mutation"""
        response = requests.put(f'{PAYMENT_MS_URL}/payment-methods/{method_id}', data=method).json()
        return UpdatePaymentMethod(method=PaymentMethod(
            id = response['id'],
            account_id = response['account_id'],
            gift_card_id = response['gift_card_id'],
            card_number = response['card_number'],
            card_expiry_date = response['card_expiry_date'],
            card_security_number = response['card_security_number']
        ))


class DeletePaymentMethod(graphene.Mutation):
    """Delete Payment Method Mutation"""
    boolean = graphene.Field(graphene.Boolean)

    class Arguments:
        """Mutation arguments"""
        method_id = graphene.ID(required=True)
    
    @staticmethod
    def mutate(root, info, method_id=None):
        """Mutation"""
        request = requests.delete(f'{PAYMENT_MS_URL}/payment-methods/{method_id}')
        if request.status_code == 200:
            return DeletePaymentMethod(boolean=True)
        return DeletePaymentMethod(boolean=False)


class DeletePaymentMethods(graphene.Mutation):
    """Delete Payment Methods Mutation"""
    boolean = graphene.Field(graphene.Boolean)

    class Arguments:
        """Mutation arguments"""
        pass
    
    @staticmethod
    def mutate(root, info):
        """Mutation"""
        token = info.context.META.get('HTTP_AUTHORIZATION')
        user_data = requests.get(f'{USER_MS_URL}/whoAmI/', headers={'Authorization': token}).json()
        data = {'account_id': user_data['id']}
        requests.delete(f'{PAYMENT_MS_URL}/payment-methods', json=data)
        return DeletePaymentMethods(boolean=None)


class Mutation(graphene.ObjectType):
    create_payment_method = CreatePaymentMethod.Field()
    update_payment_method = UpdatePaymentMethod.Field()
    delete_payment_method = DeletePaymentMethod.Field()
    delete_payment_methods = DeletePaymentMethods.Field()
