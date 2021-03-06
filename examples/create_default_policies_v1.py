#!/usr/bin/env python
#
# Create the default set of policies given the falco rules file.
# Existing policies with the same name are unchanged. New policies
# as needed will be added. Returns JSON representing the new
# policies created.
#

import os
import sys
import json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdSecureClientV1


def usage():
    print('usage: %s <sysdig-token>' % sys.argv[0])
    print('You can find your token at https://secure.sysdig.com/#/settings/user')
    sys.exit(1)


#
# Parse arguments
#
if len(sys.argv) != 2:
    usage()

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdSecureClientV1(sdc_token, 'https://secure.sysdig.com')

ok, res = sdclient.create_default_policies()

#
# Return the result
#
if ok:
    print(json.dumps(res, indent=2))
else:
    print(res)
    sys.exit(1)
