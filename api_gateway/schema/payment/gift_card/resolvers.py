"""Gift Card Resolvers"""

import graphene
import requests
import os

from .type_defs import GiftCardInput, GiftCard

# PAYMENT_MS_URL = os.getenv('PAYMENT_MS_URL')
PAYMENT_MS_URL = 'http://localhost:8080'


class Query(graphene.ObjectType):
    """Gift card query resolvers"""
    retrieve_card_by_id = graphene.Field(GiftCard, card_id=graphene.ID(name='card_id'))
    retrieve_card_by_code = graphene.Field(GiftCard, card_code=graphene.ID(name='card_code'))

    def resolve_retrieve_card_by_id(parent, info, card_id):
        """Retrieve card by id resolver"""
        response = requests.get(f'{PAYMENT_MS_URL}/gift-cards/{card_id}').json()
        if 'id' not in response.keys():
            return None
        return response
    
    def resolve_retrieve_card_by_code(parent, info, card_code):
        """Retrieve card by code resolver"""
        data = {'card_code': card_code}
        response = requests.get(f'{PAYMENT_MS_URL}/gift-cards', params=data).json()
        if 'id' not in response.keys():
            return None
        return response


class CreateGiftCard(graphene.Mutation):
    """Create Gift Card Mutation"""
    card = graphene.Field(GiftCard, required=True)

    class Arguments:
        """Mutation arguments"""
        card = GiftCardInput(required=True)
    
    @staticmethod
    def mutate(root, info, card=None):
        """Mutation"""
        response = requests.post(f'{PAYMENT_MS_URL}/gift-cards', json=card).json()
        return CreateGiftCard(card=GiftCard(
            id = response['id'],
            card_code = response['card_code'],
            amount = response['amount'],
            is_active = response['is_active'],
            expiration_date = response['expiration_date']
        ))


class UpdateGiftCard(graphene.Mutation):
    """Update Gift Card Mutation"""
    card = graphene.Field(GiftCard, required=True)

    class Arguments:
        """Mutation arguments"""
        card_id = graphene.ID(required=True)
        card = GiftCardInput(required=True)
    
    @staticmethod
    def mutate(root, info, card_id=None, card=None):
        """Mutation"""
        response = requests.put(f'{PAYMENT_MS_URL}/gift-cards/{card_id}', json=card).json()
        return UpdateGiftCard(card=GiftCard(
            id = response['id'],
            card_code = response['card_code'],
            amount = response['amount'],
            is_active = response['is_active'],
            expiration_date = response['expiration_date']
        ))


class DeleteGiftCard(graphene.Mutation):
    """Delete Gift Card Mutation"""
    boolean = graphene.Field(graphene.Boolean)

    class Arguments:
        """Mutation arguments"""
        card_id = graphene.ID(required=True)
    
    @staticmethod
    def mutate(root, info, card_id=None):
        """Mutation"""
        request = requests.delete(f'{PAYMENT_MS_URL}/gift-cards/{card_id}')
        if request.status_code == 200:
            return DeleteGiftCard(boolean=True)
        return DeleteGiftCard(boolean=False)


class Mutation(graphene.ObjectType):
    create_gift_card = CreateGiftCard.Field()
    update_gift_card = UpdateGiftCard.Field()
    delete_gift_card = DeleteGiftCard.Field()
