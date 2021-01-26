
# installer for the demo-skin extension

import configobj
from setup import ExtensionInstaller

try:
    # Python 2
    from StringIO import StringIO
except ImportError:
    # Python 3
    from io import StringIO


#------ extension info ------------

extension_version="0.3",

extension_name='demo-skin',
extension_description='demo minimalist custom skin',
extension_author="Vince Skahan",
extension_author_email="vinceskahan@gmail.com",

#----------- config ---------------

extension_config = """
[StdReport]

    # this came from the demo-skin extension
    [[demo-skin]]
        skin = demo-skin
        HTML_ROOT = demo-skin
        enable = false
"""
extension_dict = configobj.ConfigObj(StringIO(extension_config))

#----------- files ----------------

files=[
  ('skins/demo-skin',
    [
      'skins/demo-skin/index.html.tmpl',
      'skins/demo-skin/mystyle.css',
      'skins/demo-skin/skin.conf'
    ],
  ),
]
files_dict = files

#----------------------------------

def loader():
    return MySkinInstaller()

class MySkinInstaller(ExtensionInstaller):
    def __init__(self):
        super(MySkinInstaller, self).__init__(
            version=extension_version,
            name=extension_name,
            description=extension_description,
            author=extension_author,
            author_email=extension_author_email
            config=extension_dict,
            files=files_dict
        )


# optionally you might also have the following
#   report_services='string_here',
#   archive_services=['something', somethingelse'],
#   process_services='something',
#
