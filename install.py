
# installer for the demo-skin extension

import configobj
from setup import ExtensionInstaller

try:
    # Python 2
    from StringIO import StringIO
except ImportError:
    # Python 3
    from io import StringIO

# what we want in weewx.conf
extension_config = """
[StdReport]

    # this came from the demo-skin extension
    [[demo-skin]]
        skin = demo-skin
        HTML_ROOT = demo-skin
        enable = false
"""
extension_dict = configobj.ConfigObj(StringIO(extension_config))

# files to drop into place
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

def loader():
    return MySkinInstaller()

class MySkinInstaller(ExtensionInstaller):
    def __init__(self):
        super(MySkinInstaller, self).__init__(
            version="0.3",
            name='demo-skin',
            description='demo minimalist custom skin',
            author="Vince Skahan",
            author_email="vinceskahan@gmail.com",
            config=extension_dict,
            files=files_dict
        )


# optionally you might also have
#   report_services='string_here',
#   archive_services=['something', somethingelse'],
#   process_services='something',
#
