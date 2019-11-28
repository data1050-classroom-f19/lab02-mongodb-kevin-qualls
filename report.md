# Report

1. How is MongoDb different than a SQL database such as MySQL?

<pre>MongoDB is a non-relational database (no keys) ; SQL is a relational database (has keys) - 
MongoDB is collection based ; SQL is table based - 
MongoDB is document based ; SQL is row based</pre>

2. What are the types of indexes in MongoDb and why are they necessary for certain types of queries?

<pre>The TEXT index is necessary to store root words of strings, like ‘neighbourhood_group’ or ‘room_type’ from the AB_NYC_2019.csv data set. 
The GEOSPHERE index (or Geospatial index) is also necessary to eventually visualize the coordinates of the geospatial data
</pre>

3. In what scenarious would you use MongoDb over other alternatives such as MySQL?

<pre>I would use MongoDB if:
I was trying to visualize my data in a heat map, like we did with airbnb’s and taxis.
The dataset I was given had no relations
The dataset was collections and documents-based
</pre>
