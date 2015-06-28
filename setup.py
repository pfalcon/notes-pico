from setuptools import setup, find_packages


setup(name='notes-pico',
      version='0.2',
      description="""A note-taking example web application for Picoweb
web pico-framework. (Ported from Flask original)""",
      url='https://github.com/pfalcon/notes-pico',
      author='Charles Leifer, Paul Sokolovsky',
      author_email='pfalcon@users.sourceforge.net',
      license='To be clarified',
      packages=['notes_pico', 'notes_pico.templates.compiled'],
      install_requires=['picoweb', 'uorm', 'utemplate', 'micropython-re-pcre'])
