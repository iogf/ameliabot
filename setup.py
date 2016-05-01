#! /usr/bin/env python

from distutils.core import setup

setup(name="ameliabot",
      version="1.0.0",
      packages=["ameliabot", 
                "ameliabot.plugins",
                'ameliabot.plugins.quote'],
      scripts=['amelia'],
      package_data={'ameliabot': ['ameliarc', '/ameliabot/ameliarc'],
                    'ameliabot.plugins.quote':['quote_database', '/ameliabot/plugins/quote/quote_database']},
      author="Iury O. G. Figueiredo",
      author_email="ioliveira@id.uff.br")




















