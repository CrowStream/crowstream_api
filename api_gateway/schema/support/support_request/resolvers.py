"""Support Request Resovlers"""

# Utilities
import graphene
import requests
import os

# Crowstream API Gateway
from .type_defs import SupportRequest, SupportRequestInput


SUPPORT_MS_URL = os.getenv('SUPPORT_MS_URL')
USER_MS_URL = os.getenv('USER_MS_URL')

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
        support_request = SupportRequestInput(required=True, name='support_request')
    
    @staticmethod
    def mutate(root, info, support_request=None):
        """Mutation"""
        token = info.context.META.get('HTTP_AUTHORIZATION')
        user_data = requests.get('{0}/whoAmI/'.format(USER_MS_URL), headers={'Authorization': token}).json()
        support_request['user_id'] = user_data['id']
        res = requests.post('{0}/support_requests/'.format(SUPPORT_MS_URL), json=support_request).json()
        return CreateSupportRequest(
            support_request=SupportRequest(
                _id=res['_id'],
                user_id=res['user_id'],
                request_type=res['request_type'],
                title=res['title'],
                description=res['description'],
                response=res['response'] if 'response' in res else None,
                files=res['files']
            )
        )


class UpdateSupportRequest(graphene.Mutation):
    """Update SupportRequest Mutation"""

    support_request = graphene.Field(SupportRequest, required=True)

    class Arguments:
        """Mutation Arguments"""
        id_support_request = graphene.ID(required=True, name='id_support_request')
        support_request = SupportRequestInput(required=True, name='support_request')

    @staticmethod
    def mutate(root, info, id_support_request=None, support_request=None):
        """Mutation"""
        token = info.context.META.get('HTTP_AUTHORIZATION')
        user_data = requests.get('{0}/whoAmI/'.format(USER_MS_URL), headers={'Authorization': token}).json()
        support_request['user_id'] = user_data['id']
        res = requests.put('{0}/support_requests/{1}/'.format(SUPPORT_MS_URL, id_support_request), json=support_request).json()
        return UpdateSupportRequest(
            support_request=SupportRequest(
                _id=res['_id'],
                user_id=res['user_id'],
                request_type=res['request_type'],
                title=res['title'],
                description=res['description'],
                response=res['response'] if 'response' in res else None,
                files=res['files']
            )
        )

class DeleteSupportRequest(graphene.Mutation):
    """Delete Support Request Mutation"""

    boolean = graphene.Field(graphene.Boolean)

    class Arguments:  
        """Mutation Arguments"""
        id_support_request = graphene.ID(required=True, name='id_support_request')

    @staticmethod
    def mutate(root, info, id_support_request=None):
        """Mutation"""
        requests.delete('{0}/support_requests/{1}/'.format(SUPPORT_MS_URL, id_support_request))
        return DeleteSupportRequest(boolean=None)


class Mutation(graphene.ObjectType):
    """Class to compile all Mutations"""
    create_support_request = CreateSupportRequest.Field()
    update_support_request = UpdateSupportRequest.Field()
    delete_support_request = DeleteSupportRequest.Field()