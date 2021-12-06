"""Catalogue Video Resolvers"""

import graphene
import requests
import os

from .type_defs import Video
CATALOGUE_MS_URL = os.getenv('CATALOGUE_MS_URL')


class Query(graphene.ObjectType):
    """Gift card query resolvers"""
    retrieve_video_by_id = graphene.Field(Video, video_id=graphene.Int())

    def resolve_retrieve_video_by_id(parent, info, video_id):
        """Retrieve video by id resolver"""
        print(os.getenv('CATALOGUE_MS_URL'))
        dict = requests.get(f'{CATALOGUE_MS_URL}/filter_by_id/{video_id}').json()[0]
        video_dict = {}
        video_dict["id"] = dict["v"]["id"]
        video_dict["description"] = dict["v"]["properties"]["description"]
        video_dict["release_year"] = dict["v"]["properties"]["release_year"]
        video_dict["video_name"] = dict["v"]["properties"]["video_name"]
        print(video_dict)
        return video_dict
    