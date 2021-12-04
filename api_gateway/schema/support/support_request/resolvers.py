""" Support Request Resovlers"""

# Utilities
import graphene
import requests
import os

# Crowstream Api Gateway
from .type_defs import SupportRequest


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