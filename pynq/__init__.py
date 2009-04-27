#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from os.path import dirname, abspath, join
root_path = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, root_path)

from pynq.providers import CollectionProvider
from pynq.parser import ExpressionParser

def From(provider):
   return Query(provider)

class Query(object):
   def __init__(self, provider):
      if isinstance(provider, (list, tuple)):
         self.provider = CollectionProvider()
      else:
         self.provider = provider
      self.expressions = [] 
      self.parser = ExpressionParser()
      
   def where(self, clause):
      self.expressions.append(self.parser.parse(clause))
      return self
