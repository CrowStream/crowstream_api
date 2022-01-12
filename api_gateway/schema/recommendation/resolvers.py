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
        #data = requests.get(CATALOGUE_MS_URL+'/filter_by_genre_just_id/'+genre).json()
        #video_list_1 = []
        #for dicc in data:
        #    video_list_1.append(dicc['id'])
        #print(video_list_1)
        video_list = [1,2,3]#video_list = requests.get(CATALOGUE_MS_URL+'/filer_by_genre/'+genre) #sacar lista de videos
        return requests.get(RECOMMENDATION_MS_URL+'recommendation/rate_video_list',json={'profile_id':profile_id,'video_list':video_list, 'n_videos': n_videos}).json()['videos']
    
    

class TrainModel(graphene.Mutation):
    trained = graphene.Boolean()

    def mutate(self, info):
        #print("Recommendation URL", os.getenv('RATING_MS_URL'))
        like = [
            ["1",1],
            ["2",2],
            ["3",3],
            ["4",4],
            ["5",5]
        ]
        #rating_data = requests.get(RATING_MS_URL+'/getLikedVideos').json()
        #like = []
        #for rating in rating_data['likes']:
        #    like.append([rating['user_id'], rating['video_id']])

        #dislike = []
        #for rating in rating_data['dislikes']:
        #    dislike.append([rating['user_id'], rating['video_id']])

        dislike = [["1",5],["2",4],["3",2],["4",3],["5",1]]#dislike = requests.get(RATING_MS_URL+'')
        #reproduction_data = requests.get(REPRODUCTION_MS_URL+'/click-count-metadata').json()
        
        #clicks = []
        #watchs = []
        #for data in reproduction_data:
        #    if data['click_description']:
        #        clicks.append([data['user_id'], data['video_id']])
        #    if data['click_video']:
        #        watchs.append([data['user_id'], data['video_id']])

        click = [
            ["1",1],["1",2],["1",3],["1",4],["1",5],
            ["2",1],["2",2],["2",3],["2",4],["2",5],
            ["3",1],["3",2],["3",3],["3",4],["3",5],
            ["4",1],["4",2],["4",3],["4",4],["4",5],
            ["5",1],["5",2],["5",3],["5",4],["5",5]
        ]
        watch = [
            ["1",1],["1",5],["2",2],["2",4],["3",3],["3",2],["4",4],["4",3],["5",5],["5",1]
        ]#watch = requests.get(REPRODUCTION_MS_URL+'')
        #print(like)
        return requests.get(RECOMMENDATION_MS_URL+'recommendation/train_model',json={'like': like, 'dislike': dislike, 'click': click, 'watch': watch}).json()


class Mutation(graphene.ObjectType):
    train_model = TrainModel.Field()
