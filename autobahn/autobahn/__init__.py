###############################################################################
##
##  Copyright 2011-2013 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

from _version import __version__
version = __version__ # backward compat.

import util
import choosereactor
import useragent
import flashpolicy
import httpstatus
import utf8validator
import xormasker
import compress
import websocket

## disable import, since it leads to reactor import
## https://twistedmatrix.com/trac/ticket/6849
#import resource

import prefixmap
import wamp
import wamp2
