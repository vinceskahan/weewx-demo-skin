
# installer for the demo-skin extension

from setup import ExtensionInstaller

def loader():
    return MySkinInstaller()

class MySkinInstaller(ExtensionInstaller):
    def __init__(self):
        super(MySkinInstaller, self).__init__(
            version="0.2",
            name='demo-skin',
            description='demo minimalist custom skin',
            author="Vince Skahan",
            author_email="vinceskahan@gmail.com",
            config={
                'StdReport': {
                    'demo-skin': {
                        'skin': 'demo-skin',
                        'HTML_ROOT': 'demo-skin'
                        }
                }
            },
            files=[
                 ('skins/demo-skin',
                    [
                        'skins/demo-skin/index.html.tmpl',
                        'skins/demo-skin/mystyle.css',
                        'skins/demo-skin/skin.conf'
                    ],
                 ),
            ]
        )
