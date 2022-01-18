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
        dict = requests.get(f'{CATALOGUE_MS_URL}/filter_by_id/{video_id}').json()[0]
        video_dict = {}
        video_dict["id"] = dict["video"]["id"]
        video_dict["description"] = dict["video"]["properties"]["description"]
        video_dict["release_year"] = dict["video"]["properties"]["release_year"]
        video_dict["video_name"] = dict["video"]["properties"]["video_name"]
        video_dict["thumbnail_url"] = dict["video"]["properties"]["thumbnail_url"]
        video_dict["video_url"] = dict["video"]["properties"]["video_url"]
        #Director and Producer
        video_dict["director"] = dict["director"]
        video_dict["producer"] = dict["producer"]
        #Genre
        video_dict["genre"] = dict["genre"]
        print(video_dict)

        return video_dict
    