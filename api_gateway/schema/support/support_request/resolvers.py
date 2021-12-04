""" Support Request Resovlers"""

# Utilities
import graphene
import requests
import os

# Crowstream API Gateway
from .type_defs import SupportRequest, SupportRequestInput


SUPPORT_MS_URL = 'http://{0}:{1}'.format(os.getenv('SUPPORT_MS_HOST'), os.getenv('SUPPORT_MS_PORT'))

class Query(graphene.ObjectType):
    """Support Request query resolvers"""
    retrieve_all_support_request = graphene.NonNull(graphene.List(SupportRequest))
    retrieve_support_request_by_id = graphene.Field(SupportRequest, id_support_request=graphene.ID(name='id_support_request'))
    
    def resolve_retrieve_all_support_request(parent, info):
        """Retrieve all support request resolver"""
        return requests.get('{0}/support_requests/'.format(SUPPORT_MS_URL)).json()
    
    def resolve_retrieve_support_request_by_id(parent, info, id_support_request):
        """Retrieve support request by id resolver"""
        return requests.get('{0}/support_requests/{1}/'.format(SUPPORT_MS_URL, id_support_request)).json()


class CreateSupportRequest(graphene.Mutation):
    """Create Support Request Mutation"""

    support_request = graphene.Field(SupportRequest, required=True)

    class Arguments:
        """Mutation Arguments"""
        support_request = graphene.Field(SupportRequestInput, required=True)
    
    @staticmethod
    def mutate(root, info, support_request=None):
        """Mutation"""
        pass


class UpdateSupportRequest(graphene.Mutation):
    """Update SupportRequest Mutation"""

    support_request = graphene.Field(SupportRequest, required=True)

    class Arguments:
        """Mutation Arguments"""
        id_support_request = graphene.Field(graphene.ID, required=True)
        support_request = graphene.Field(SupportRequestInput, required=True)

    @staticmethod
    def mutate(root, info, support_request=None):
        """Mutation"""
        pass


class DeleteSupportRequest(graphene.Mutation):
    """Delete Support Request Mutation"""

    boolean = graphene.Field(graphene.Boolean)

    class Arguments:  
        """Mutation Arguments"""
        id_support_request = graphene.Field(graphene.ID, required=True)

    @staticmethod
    def mutate(root, info, boolean=None):
        """Mutation"""
        pass


class Mutation(graphene.ObjectType):
    """Class to compile all Mutations"""
    create_support_request = CreateSupportRequest.Field()
    update_support_request = UpdateSupportRequest.Field()
    delete_support_request = DeleteSupportRequest.Field()