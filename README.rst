TX Slider
============
This product allows you to add slideshows to any page on a plone (version 4.3) site. It uses the cycle2 jquery library: http://malsup.com/jquery/cycle2/

See also configuration and layout `README`_:

.. _README: tx/tiles/README.rst

How to use
----------
On a page, click ``Actions`` -> ``Add slider``.

.. image:: docs/images/add-slider.png
   :width: 50%

This opens a setting page for your slides. Slides can be added by clicking ``add new slide``.

.. image:: docs/images/add-new-slide.png

Access the slider configuration through the ``Slider`` tab.

.. image:: docs/images/slider-configuration.png
   :width: 50%

The slides are rendered by viewlets (at portaltop, belowcontenttitle or belowcontent).
	   
.. image:: docs/images/view-slider.png
   :width: 50%

TODO
----
As of now only english and german translation is available.

Installation
------------
* add tx.slider to your eggs sections
* re-run buildout
* install the product in the Control Panel

Uninstall
---------
* Uninstall like normal

Credits and Contributions
-------------------------
* tx.tiles is based on collective.easyslider. Thanks for the ideas!
* University of Freiburg (Technische Fakultät) for sponsoring the package

