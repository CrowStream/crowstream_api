"""Invoice Resolvers"""

import graphene
import requests
import os

from .type_defs import InvoiceInput, Invoice

USER_MS_URL = f'http://{os.getenv("USER_MS_HOST")}:{os.getenv("USER_MS_PORT")}'
PAYMENT_MS_URL = f'http://{os.getenv("PAYMENT_MS_HOST")}:{os.getenv("PAYMENT_MS_PORT")}'


class Query(graphene.ObjectType):
    """Invoice query resolvers"""
    retrieve_invoice_by_id = graphene.Field(Invoice)
    retrieve_invoices_by_account_id = graphene.NonNull(graphene.List(Invoice))

    def resolve_retrieve_invoice_by_id(parent, info, invoice_id):
        token = info.context.META.get('HTTP_AUTHORIZATION')
        user_data = requests.get(f'{USER_MS_URL}/whoAmI/', headers={'Authorization': token}).json()
        response = requests.get(f'{PAYMENT_MS_URL}/invoices/{invoice_id}').json()
        if user_data['id'] != response['account_id']:
            return None
        return response
    
    def resolve_retrieve_invoices_by_account_id(parent, info):
        token = info.context.META.get('HTTP_AUTHORIZATION')
        user_data = requests.get(f'{USER_MS_URL}/whoAmI/', headers={'Authorization': token}).json()
        data = {'account_id': user_data['id']}
        return requests.get(f'{PAYMENT_MS_URL}/invoices', json=data).json()


class CreateInvoice(graphene.Mutation):
    """Create Invoice Mutation"""
    invoice = graphene.Field(Invoice, required=True)

    class Arguments:
        """Mutation arguments"""
        invoice = InvoiceInput(required=True)
    
    @staticmethod
    def mutate(root, info, invoice=None):
        """Mutation"""
        response = requests.post(f'{PAYMENT_MS_URL}/invoices', json=invoice).json()
        return CreateInvoice(invoice=Invoice(
            id = response['id'],
            account_id = response['account_id'],
            amount = response['amount'],
            created_at = response['created_at'],
            limit_date = response['limit_date'],
            payment_id = response['payment_id'],
            state = response['state']
        ))


class UpdateInvoice(graphene.Mutation):
    """Update Invoice Mutation"""
    invoice = graphene.Field(Invoice, required=True)

    class Arguments:
        """Mutation arguments"""
        invoice_id = graphene.ID(required=True)
        invoice = InvoiceInput(required=True)
    
    @staticmethod
    def mutate(root, info, invoice_id=None, invoice=None):
        """Mutation"""
        response = requests.put(f'{PAYMENT_MS_URL}/invoices/{invoice_id}', data=invoice).json()
        return UpdateInvoice(invoice=Invoice(
            id = response['id'],
            account_id = response['account_id'],
            amount = response['amount'],
            created_at = response['created_at'],
            limit_date = response['limit_date'],
            payment_id = response['payment_id'],
            state = response['state']
        ))


class DeleteInvoice(graphene.Mutation):
    """Delete Invoice Mutation"""
    boolean = graphene.Field(graphene.Boolean)

    class Arguments:
        """Mutation arguments"""
        invoice_id = graphene.ID(required=True)
    
    @staticmethod
    def mutate(root, info, invoice_id=None):
        """Mutation"""
        request = requests.delete(f'{PAYMENT_MS_URL}/invoices/{invoice_id}')
        if request.status_code == 200:
            return DeleteInvoice(boolean=True)
        return DeleteInvoice(boolean=False)


class DeleteInvoices(graphene.Mutation):
    """Delete Invoices Mutation"""
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
        requests.delete(f'{PAYMENT_MS_URL}/invoices', json=data)
        return DeleteInvoice(boolean=None)


class Mutation(graphene.ObjectType):
    create_invoice = CreateInvoice.Field()
    update_invoice = UpdateInvoice.Field()
    delete_invoice = DeleteInvoice.Field()
    delete_invoices = DeleteInvoices.Field()
