""" Post Resovlers"""

# Utilities
import json
import graphene
import requests
import os

from requests.api import get

# Crowstream API Gateway

RECOMMENDATION_MS_URL = '{0}'.format(os.getenv('RECOMMENDATION_MS_URL'))
RATING_MS_URL = '{0}'.format(os.getenv('RATING_MS_URL'))
CATALOGUE_MS_URL = '{0}'.format(os.getenv('CATALOGUE_MS_URL'))
REPRODUCTION_MS_URL = '{0}'.format(os.getenv('REPRODUCTION_MS_URL'))

class Query(graphene.ObjectType):
    """Recommendation query resolvers"""
    rate_video_list = graphene.List(graphene.String, profile_id=graphene.String(), genre=graphene.String(), n_videos=graphene.Int())
    
    
    def resolve_rate_video_list(parent, info, profile_id, genre, n_videos):
        """Retrieve all post resolver"""
        #return requests.get(CATALOGUE_MS_URL+'/filter_by_genre_just_id/'+genre).json()
        try:
            data = requests.get(CATALOGUE_MS_URL+'/filter_by_genre_just_id/'+genre).json()
        except:
            "Error fetching catalogue data"
        print("Catalogue data:", data)
        video_list = []
        for dicc in data:
           video_list.append(dicc['id'])
        print(video_list)
        return requests.get(RECOMMENDATION_MS_URL+'recommendation/rate_video_list',json={'profile_id':profile_id,'video_list':video_list, 'n_videos': n_videos}).json()['videos']
    
    

class TrainModel(graphene.Mutation):
    trained = graphene.Boolean()

    def mutate(self, info):
        try:
            rating_data = requests.get(RATING_MS_URL+'/getLikedVideos').json()
        except:
            "Error fetching rating data"
        likes = []
        print(rating_data.keys())
        print("Rating data[likes]: ",rating_data['likes'])
        print("Rating data[dislikes]: ",rating_data['dislikes'])
        for rating in rating_data['likes']:
            likes.append([rating['user_id'], rating['video_id']])

        dislikes = []
        for rating in rating_data['dislikes']:
            dislikes.append([rating['user_id'], rating['video_id']])
        print("Likes: ",likes)
        print("Dislikes: ",dislikes)
        try:
            reproduction_data = requests.get(REPRODUCTION_MS_URL+'/click-count-metadata').json()
        except:
            "Error fetching reproduction data"
            
        clicks = []
        watchs = []
        for data in reproduction_data:
           if data['click_description']:
               clicks.append([data['user_id'], data['video_id']])
           if data['click_video']:
               watchs.append([data['user_id'], data['video_id']])
        print("Clicks:", clicks)
        print("Watchs:", watchs)
        return requests.get(RECOMMENDATION_MS_URL+'recommendation/train_model',json={'like': likes, 'dislike': dislikes, 'click': clicks, 'watch': watchs}).json()


class Mutation(graphene.ObjectType):
    train_model = TrainModel.Field()
