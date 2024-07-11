import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__) #app
mysql = MySQL(server)

#config for server/app
server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST") #resolves to localhost
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")

@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization #request needs authentication header (user/pass) 
    if not auth:
        return "Missing credentials", 401
    
    #check db for user and pass
    