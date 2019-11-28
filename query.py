"""
(This is a file-level docstring.)
This file contains all required queries to MongoDb.
"""
from pymongo import MongoClient

db = MongoClient().test


def query1(minFare, maxFare):
    """ Finds taxi rides with fare amount greater than or equal to minFare and less than or equal to maxFare.  

    Args:
        minFare: An int represeting the minimum fare
        maxFare: An int represeting the maximum fare

    Projection:
        pickup_longitude
        pickup_latitude
        fare_amount

    Returns:
        An array of documents.
    """
    docs = db.taxi.find(
        # TODO: implement me
        {'fare_amount': 
            {
                '$gte': minFare, 
                '$lte': maxFare
            }
        },
        {
            '_id': 0,
            'pickup_longitude': 1,
            'pickup_latitude': 1,
            'fare_amount': 1
        }
    )

    result = [doc for doc in docs]
    return result


def query2(textSearch, minReviews):
    """ Finds airbnbs with that match textSearch and have number of reviews greater than or equal to minReviews.  

    Args:
        textSearch: A str representing an arbitrary text search
        minReviews: An int represeting the minimum amount of reviews

    Projection:
        name
        number_of_reviews
        neighbourhood
        price
        location

    Returns:
        An array of documents.
    """
    docs = db.airbnb.find(
        {
            '$text': {
                '$search': textSearch
            },
            'number_of_reviews': {
                '$gte': minReviews
            }
        },
        {
            '_id': 0,
            'name': 1,
            'number_of_reviews': 1,
            'neighbourhood': 1,
            'price': 1,
            'location': 1
        }
    )

    result = [doc for doc in docs]
    return result


def query3():
    """ Groups airbnbs by neighbourhood_group and finds average price of each neighborhood_group sorted in descending order.  

    Returns:
        An array of documents.
    """
    docs = db.airbnb.aggregate(
    # TODO: implement me
    
    { '$group': { '_id': "neighbourhood", 'avg_price': { '$avg': "price" } } },
    {'$sort': {'avg_price': -1}}
    
    )

    result = [doc for doc in docs]
    return result


def query4():
    """ Groups taxis by pickup hour. 
        Find average fare for each hour.
        Find average manhattan distance travelled for each hour.
        Count total number of rides per pickup hour.
        Sort by average fare in descending order.

    Returns:
        An array of documents.
    """
    docs = db.taxi.aggregate(
        # TODO: implement me

    [{ '$group': { '_id': "pickup_datetime", # Groups taxis by pickup hour
    
    'avg_fare': {'$avg': 'fare_amount'}}}, # Find average fare for each hour.

    # Find average manhattan distance travelled for each hour
    
    {'avg_dist': {'$avg': { '$abs': 
    
    { 
    
    {'$add:' [ {'$subtract:' [ 'pickup_longitude', '$ropoff_longitude']}, 
    {'$subtract': [ "pickup_longitude", "dropoff_longitude" ]} ]}
    
    } } }
    
    }, 
    

    { '$group': { '_id': "pickup_datetime", 'total_num': {"passenger_count"} } }, # Count total number of rides per pickup hour.

    {'$sort': {'avg_fare': -1}} # Sort by average fare in descending order.
        
    ]
    )

    result = [doc for doc in docs]
    return result

def query5(latitude, longitude):
   """ Finds airbnbs within 1000 meters from location (longitude, latitude) using geoNear.

   Args:
       latitude: A float representing latitude coordinate
       longitude: A float represeting longitude coordinate

   Projection:
       dist
       name
       neighbourhood
       neighbourhood_group
       price
       room_type

    
   """
   docs = db.airbnb.aggregate([
    # TODO: implement me 
       {
           '$geoNear': {
               'near': {'type': 'Point', 'coordinates': [longitude, latitude]},
               'distanceField': 'dist.calculated',
               'maxDistance': 1000,
               'spherical': False
           }
       },
       {
           '$project': {
               '_id': 0,
               'dist': 1,
               'name': 1,
               'neighbourhood': 1,
               'neighbourhood_group': 1,
               'price': 1,
               'room_type': 1
           }
       },
       {
           '$sort': {'dist': 1}
       }
   ])
   result = [doc for doc in docs]
   return result