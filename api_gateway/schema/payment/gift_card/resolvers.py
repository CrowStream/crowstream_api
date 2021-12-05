"""Gift Card Resolvers"""

import graphene
import requests
import os

from .type_defs import GiftCardInput, GiftCard

PAYMENT_MS_URL = f'http://{os.getenv("PAYMENT_MS_HOST")}:{os.getenv("PAYMENT_MS_PORT")}'


class Query(graphene.ObjectType):
    """Gift card query resolvers"""
    retrieve_card_by_id = graphene.Field(GiftCard)
    retrieve_card_by_code = graphene.Field(GiftCard)

    def resolve_retrieve_card_by_id(parent, info, card_id):
        """Retrieve card by id resolver"""
        return requests.get(f'{PAYMENT_MS_URL}/gift-cards/{card_id}').json()
    
    def resolve_retrieve_card_by_code(parent, info, card_code):
        """Retrieve card by code resolver"""
        data = {'card_code': card_code}
        return requests.get(f'{PAYMENT_MS_URL}/gift-cards', json=data).json()


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
        response = requests.put(f'{PAYMENT_MS_URL}/gift-cards/{card_id}', data=card).json()
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
