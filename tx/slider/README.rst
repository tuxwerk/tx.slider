TX Slider
=========

Plone image slideshow based on the cycle2 jquery lib 

Homepage: https://github.com/tuxwerk/tx.slider

Configuration
-------------

The effect, transition speed and pause and type of navigation (arrows or bullets) can be set globaly for all siders in the Plone Control Panel. Individual sliders can overload the settings. Predefined CSS classes for individual layouts can also be set there (See section: Layout).

Security
--------

The Add-On defines following permissions:

*tx.slider: Add slider*

Adding and removing sliders on content. (Default: Site Administrator and Editor)

*tx.slider: Edit slider*

Editing of sliders. (Default: Site Administrator and Editor)

*tx.slider: Manage slider settings*

Can manage the configuration in Plone Control Panel. (Default: Site Administrator)
    
Layout
------

For all slides
~~~~~~~~~~~~~~

All slides of a page can be configured by assigning a CSS class. The classes and display names are configured through the Plone Control Panel. The add on has the following predefined configurations for different aspect ratios:

* tx-slider-16-9
* tx-slider-2-1
* tx-slider-4-3
* tx-slider-square

For single slides
~~~~~~~~~~~~~~~~~

CSS classes can also be assigned to single slides. The classes and display names are configured through the Plone Control Panel. The add on has a predefined example class:

* tx-slide-important

CSS Styles
~~~~~~~~~~

The layout of the slides can be altered by CSS. You can define new CSS classes in your theme product and set them in the Plone Control Panel.

You can use following CSS to overload the height of slides (Add the CSS class 'tx-slider-10-1' in the add on configuration)::

  /* set aspect ratio 10:1 */
  .tx-slider-container.tx-slider-10-1 {
    padding-bottom: 10%;
  }

Single slides can be styled as following (Add the CSS class 'red-slide' in the single slide configuration)::

  /* show heading on red background */
  .red-slide h2.tx-slide-heading {
    background: red;
  }
  
The slides are rendered with following HTML Code::

 <div class="tx-slider-container tx-slider-UID tx-slider-CLASS">
   <div class="cycle-slideshow">
     <div class="tx-slide tx-slide-CLASS">
       <div class="tx-slide-content">
         <h2 class="tx-slide-heading">Heading</h2>
         <div class="tx-slide-text">
           <p>
	     A paragraph.
	   </p>
         </div>
       </div>
     </div>
     ...
   </div>
 </div>

The previous and next buttons::

 <div class="tx-slider-container tx-slider-UID tx-slider-CLASS">
   <div class="cycle-next"></div>
   <div class="cycle-prev"></div>
   ...
 </div>

The pager::

 <div class="tx-slider-container tx-slider-UID tx-slider-CLASS">
   <div class="cycle-slideshow">
     <div class="cycle-pager">
       <span class="cycle-pager-active">•</span>
       <span>•</span>
       ...
     </div>
   </div>
 </div>

