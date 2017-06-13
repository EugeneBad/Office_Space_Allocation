.. Room_Allocator documentation master file, created by
   sphinx-quickstart on Tue Jun 13 14:27:42 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Intro: Eugene's Room_Allocator
==============================

Room_Allocator is a python program that is designed to randomise living space and office allocation for fellows and
staff at Andela.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   starting
   features

.. image:: images/Andela.png
    :width: 700px
    :align: center
    :height: 200px
    :alt: alternate text

**Problem Spec**

When a new Fellow joins Andela they are assigned an office space and an optional living space if they choose to opt in.
When a new Staff joins they are assigned an office space only.
An office can accommodate a maximum of 6 people. A living space can accommodate a maximum of 4 people.
The goal of the project is to digitize and randomize a room allocation system for one of Andela Kenya’s facilities called The Dojo.

It is implemented as a command line program which can be run in any terminal (UNIX or Windows) to add
persons, create rooms plus a host of other functions.

.. note::  Done in fulfillment of the first checkpoint as a requirement in the Andela fellowship program..