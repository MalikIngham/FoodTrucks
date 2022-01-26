
# FoodTrucks

This a full-stack web app that displays San Francisco foodtrucks on a table and
allows for the user to sort by multiple columns and add new trucks to the
record.

The data of San Francisco's foodtrucks can be found [here](https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat).

A copy of the data is included in the repo so it is not necessary to download it.

## Technologies used

Back end:

Python 3.7.5,
Flask 1.1.2.
Jinja2

Front end:
HTML.
Bootstrap5,
Jquery,
Javascript


## Installation

To get the project up and running (assuming you have atleast python 3+ installed).

Replace <ENV NAME> with a name of your choice.

```bash
  git clone https://github.com/MalikIngham/FoodTrucks.git

  pip3 install virtualenv

  python3 -m virtualenv <ENV NAME>

  source <ENV NAME>/bin/activate

  pip3 install -r requirements.txt

```

From here you are able to run the program 

```bash
    python3 flaskapp.py

```
  
  
## Documentation

The coding challenge asked me to create a REST service that returns a set of food trucks, 
assuming the dataset includes data from many cities with millions of records each, using 
language native data structures to implement in-memory data store, avoiding usage of query and/or
ORM frameworks all while spending no more than 3 hours on the solution.

I chose Python and the Flask framework as it's the combo I use frequently that allows me
to spin up results very quickly and effeciently.

One of the challenges I experienced while solving this problem is to come up with a creative 
way to manage all of the data in the CSV. Usually I would just offload the csv into databases
like MYSQL/REDIS/MongoDB and write queries to get whatever data is necessary. But in this solution I decided
to use a dictionary to store all the data. Dictionary lookups are O(1) and since the keys are hashed
it allows for low memory usage.

From there I used the `pandas.dataframe` class to convert the dictionary into a presentable table.
I passed in the dataframe table using `render_template` and then used the jQuery DataTables 
library. The Datatables library now makes it easier for the user to search per column and navigate
the table, as just passing in the dataframe argument to html displays the entire table to front end
users.

And Lastly I used HTML, Bootstrap, and CSS to clean up the front end to make it more appealing on
the eyes not only for desktop users but also mobile users.


## Trade-offs
Originally I planned on using just pandas dataframe class to sort and display data to the users.
But after coding a few lines I realized roughly 10+ conditionals where needed and the code would be messy/hard to follow.

Had I had more time to spend on the project I would've loved to include a map view of some sort using 
Bing Maps, OpenStreetMap, etc. Maps are a more effecient and friendly
way of displaying information to the users without overwhelming them with blocks of text. 
