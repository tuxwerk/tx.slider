from setuptools import setup, find_packages
import os

version = '1.1.2'

setup(name='tx.slider',
      version=version,
      description="Image slideshow based on the cycle2 jquery lib.",
      long_description='%s\n%s' % (
          open("README.rst").read(),
          open(os.path.join("docs", "HISTORY.txt")).read()
      ),
      classifiers=[
          "Framework :: Plone",
          "Framework :: Plone :: 4.3"
      ],
      keywords='plone slideshow',
      author='Marek Kralewski',
      author_email='info@tuxwerk.de',
      url='https://github.com/tuxwerk/tx.slider/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['tx'],
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'test': [
              'plone.app.testing',
          ]
      },
      install_requires=[
          'setuptools',
          'plone.app.z3cform',
          'collective.js.jqueryui',
          'Products.CMFPlone >=4.3, <5.0'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """)
