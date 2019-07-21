from setuptools import setup, find_packages
import sdist_upip


setup(name='notes-pico',
      version='0.9',
      description="""A note-taking example web application for Picoweb web pico-framework. (Ported from Flask original)""",
      long_description=open('README.rst').read(),
      url='https://github.com/pfalcon/notes-pico',
      author='Charles Leifer, Paul Sokolovsky',
      author_email='pfalcon@users.sourceforge.net',
      license='Public Domain',
      cmdclass={'sdist': sdist_upip.sdist},
      packages=['notes_pico', 'notes_pico.templates'],
      install_requires=['picoweb', 'utemplate', 'pycopy-logging',
        'pycopy-pkg_resources', 'pycopy-btreedb'])
