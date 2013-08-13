# -*- coding: utf-8 -*-
'''
Created on Aug 11, 2013

@author: moloch

    Copyright 2012 Root the Box

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''

from uuid import uuid4
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import synonym
from sqlalchemy.types import Unicode, Integer, String
from models.BaseGameObject import BaseObject
from models import dbsession
from string import ascii_letters, digits


class Hint(BaseObject):
    ''' 
    Holds the source code for a box which can be purchased from the source code market 
    '''

    uuid = Column(String(36), unique=True, nullable=False, default=lambda: uuid4())
    box_id = Column(Integer, ForeignKey('box.id'), nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(Unicode(1024), nullable=False)

    @classmethod
    def all(cls):
        ''' Returns a list of all objects in the database '''
        return dbsession.query(cls).all()

    @classmethod
    def by_id(cls, ident):
        ''' Returns a the object with id of ident '''
        return dbsession.query(cls).filter_by(id=ident).first()

    @classmethod
    def by_uuid(cls, uuid):
        ''' Returns a the object with a given uuid '''
        return dbsession.query(cls).filter_by(uuid=unicode(uuid)).first()

    @classmethod
    def by_box_id(cls, bid):
        return dbsession.query(cls).filter_by(box_id=bid).all()

    def to_dict(self):
        return {
            'price': str(self.price),
            'description': self.description,
        }
