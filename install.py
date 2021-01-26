
# installer for the demo-skin extension

import configobj
from setup import ExtensionInstaller

try:
    # Python 2
    from StringIO import StringIO
except ImportError:
    # Python 3
    from io import StringIO

#--------- extension info ----------

EXTENSION_VER="0.3"

EXTENSION_NAME="demo-skin"
EXTENSION_DESC="demo minimalist custom skin"
EXTENSION_AUTH="Vince Skahan"
EXTENSION_EMAIL="vinceskahan@gmail.com"

#--------- main installer ---------

def loader():
    return MySkinInstaller()

class MySkinInstaller(ExtensionInstaller):
    def __init__(self):
        super(MySkinInstaller, self).__init__(
            version=EXTENSION_VER,
            name=EXTENSION_NAME,
            description=EXTENSION_DESC,
            author=EXTENSION_AUTH,
            author_email=EXTENSION_EMAIL,
            config=extension_dict,
            files=files_dict
            )


# optionally you might also have the following
#   report_services='string_here',
#   archive_services=['something', somethingelse'],
#   process_services='something',

#----------------------------------
#         config stanza
#----------------------------------

extension_config = """
[StdReport]

    # this came from the demo-skin extension
    [[demo-skin]]
        skin = demo-skin
        HTML_ROOT = demo-skin
        enable = false
"""
extension_dict = configobj.ConfigObj(StringIO(extension_config))

#----------------------------------
#        files stanza
#----------------------------------

files=[
  ('skins/demo-skin',
    [
      'skins/demo-skin/index.html.tmpl',
      'skins/demo-skin/mystyle.css',
      'skins/demo-skin/skin.conf'
    ],
  )
]
files_dict = files

#---------------------------------
#          done
#---------------------------------
