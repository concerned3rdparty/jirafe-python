#!/usr/bin/env python
"""
Copyright 2014 Jirafe, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class Product:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'is_order': 'bool',
            'is_sku': 'bool',
            'catalog': 'Catalog',
            'name': 'str',
            'code': 'str',
            'ancestors': 'list[str]',
            'base_order': 'BaseProduct',
            'vendors': 'list[Vendor]',
            'brand': 'str',
            'rating': 'number',
            'create_date': 'datetime',
            'change_date': 'datetime',
            'urls': 'Url',
            'images': 'list[Image]',
            'categories': 'Set',
            'attributes': 'Set'

        }


        self.id = None # str
        self.is_order = None # bool
        self.is_sku = None # bool
        self.catalog = None # Catalog
        self.name = None # str
        self.code = None # str
        self.ancestors = None # list[str]
        self.base_order = None # BaseProduct
        self.vendors = None # list[Vendor]
        self.brand = None # str
        self.rating = None # number
        self.create_date = None # datetime
        self.change_date = None # datetime
        self.urls = None # Url
        self.images = None # list[Image]
        self.categories = None # Set
        self.attributes = None # Set
        
