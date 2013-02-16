from pythonbuilder.core import init, use_plugin, Author

use_plugin("python.core")
use_plugin("python.install_dependencies")

summary = "MongOSM is a set of Python utilities that manipulate OSM data in MongoDB"
description =\
"""
"""

authors = [
           Author("Ian Dees", "ian.dees@gmail.com"),
           ]

url     = "https://github.com/iandees/mongosm"
license = ""

@init
def initialize (project):
    project.build_depends_on("pymongo")
    project.build_depends_on("Werkzeug")
