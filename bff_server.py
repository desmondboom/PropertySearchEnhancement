from clip_client import Client
from docarray import Document, DocumentArray
from flask import Flask, request
import json

client = Client('grpc://0.0.0.0:61000')

with open("./listing-details.json", "r") as listing:
    property_details_json = json.load(listing)

property_details = property_details_json['data']['listings']
property_details_size = len(property_details)
print("size of property details: ", property_details_size)

property_docs = DocumentArray(
    map(
        lambda detail: Document(
            tags=detail,
            uri=detail['media']['mainImage']['templatedUrl']
        ),
        property_details
    )
)
property_docs = client.index(property_docs)
print("Init Done")

flask_app = Flask(__name__)

@flask_app.route('/search', methods=['GET', 'POST'])
def search_with_texts():
    searchWord = request.args.get('key', '')
    limit = request.args.get('limit', 4, int)
    result = client.search([searchWord], limit)
    return result['@m', 'tags']
    