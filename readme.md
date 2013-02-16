MongOSM
=======

MongOSM is a set of Python utilities that manipulate OSM data in MongoDB:

- `insert_osm_data.py` reads an OSM file and writes it to a MongoDB database.
- `map_server.py` uses Werkzeug to start a WSGI server that responds to the
  read-only OSM APIs and most of the XAPI-style predicate queries.
- `apply-osmchange.py` is currently not tested, but it is supposed to read
  minutely change files from planet.osm.org and keep the MongoDB database
  up to date.

Installation
------------

1. Grab MongoDB 1.9+ (2.0 is best) from http://mongodb.org/.
2. Unpack mongodb and run it.
3. Install dependencies with pybuilder: `sudo pyb install_dependencies`
4. Grab some OSM XML data.
5. Run `python insert_osm_data.py <OSM filename>` and wait.
6. Run `python map_server.py`
7. Browse to http://localhost:5000/api/0.6/node/1 to verify a (probably empty)
   response.
