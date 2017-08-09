#!/usr/bin/env python3

import argparse
import os
import sys
import requests
import time
from internetarchive import get_item
from pyfc4.models import *
from bs4 import BeautifulSoup


try:
    fedora_root = os.environ["FEDORA"]
except KeyError:
    print("Please set the environment variable FEDORA")
    sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument("item", help="IA item id")
args = parser.parse_args()
item_name = args.item

repo = Repository(fedora_root, None, None, context={
                  'pcdm': 'http://pcdm.org/models#'})

try:
    local_item = BasicContainer(repo, item_name)
    local_item.create(specify_uri=True)
except:
    local_item = repo.get_resource(item_name)

print(f'+ Container:\t {local_item.uri}')


# IA item
item = get_item(item_name)

# crosswalk metadata from IA json to DC
metadata_crosswalk = {
    'title': 'dc.title',
    'creator': 'dc.creator',
    'uploader': 'dc.contributor',
    'identifier-access': 'dc.identifier',
    'identifier-ark': 'dc.identifier',
    'language': 'dc.language',
    'date': 'dc.date',
    'subject': 'dc.subject',
    'mediatype': 'dc.type',
    'collection': 'dc.relation'

}

for k, v in metadata_crosswalk.items():
    try:
        if isinstance(item.metadata[k], list):
            [local_item.add_triple(
                eval(f'local_item.rdf.prefixes.{v}'), value) for value in item.metadata[k]]
        else:
            local_item.add_triple(
                eval(f'local_item.rdf.prefixes.{v}'), item.metadata[k])
    except:
        pass

# local_item.add_triple(local_item.rdf.prefixes.rdf.type,
        #   local_item.rdf.prefixes.pcdm.Object)

# description may contain html, sanitized to text
try:
    description = BeautifulSoup(str(item.metadata['description']), "lxml")
    description_text = description.get_text('\n')
    local_item.add_triple(local_item.rdf.prefixes.dc.description,
                          description_text)
except:
    pass


local_item.update()

for item_file in item.files:
    url = f'http://{item.d1}{item.dir}/{item_file["name"]}'
    content_type = requests.head(url).headers.get('content-type')
    print(f'- Binary:\t {url} ({content_type})')

    local_file = Binary(repo, f'{item_name}/files/{item_file["name"]}')

    local_file.headers['Content-Location'] = url
    local_file.headers['Content-Type'] = content_type

    local_file.create(specify_uri=True)
    time.sleep(5)
