from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.ycdoi.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta