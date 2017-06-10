from setuptools import setup, find_packages
import optimize_upip


setup(name='notes-pico',
      version='0.8',
      description="""A note-taking example web application for Picoweb
web pico-framework. (Ported from Flask original)""",
      long_description=open('README.rst').read(),
      url='https://github.com/pfalcon/notes-pico',
      author='Charles Leifer, Paul Sokolovsky',
      author_email='pfalcon@users.sourceforge.net',
      license='Public Domain',
      cmdclass={'optimize_upip': optimize_upip.OptimizeUpip},
      packages=['notes_pico', 'notes_pico.templates'],
      install_requires=['picoweb', 'utemplate', 'micropython-filedb'])
