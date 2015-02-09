.. This Source Code Form is subject to the terms of the Mozilla Public
.. License, v. 2.0. If a copy of the MPL was not distributed with this
.. file, You can obtain one at http://mozilla.org/MPL/2.0/.


============
Key Concepts
============

Authentication
--------------

In order to author content in the MFOS site, you will need to login:

  1. Navigate to **prod.masterfirefoxos.com/admin** (post launch: **www.masterfirefoxos.com/admin**)
  2. Supply the **username** (email) and **password**
  3. Press **Login**

FFOS Versions
-------------

All pages on masterfirefoxos (MFOSS) are associated with a version of Firefox OS. In the CMS this
is accomplished by having a seperate page tree for each version. The version of FFOS is denoted by
the slug, as shown below:

.. image:: images/slug.png

The slug will also appear in urls:

``https://www.masterfirefoxos.com/en/1-1/introduction/``

When adding a new FFOS version or locale changes must also be made by a developer to the settings
file. This is a once per version or locale change.

TinyMCE Editor
--------------

Most of the text entry fields allow you to use a WYSIWYG editor. This makes formatting text easier,
you will not have to enter any HTML tags. To activate the editor click **Activate TinyMCE**
as shown:

.. image:: images/activatetinymce.png

.. warning::

   Do not manually type in HTML tags, if you do and you activate/deactivate TinyMCE your
   tags can get rendered as entities. If this occurs you will need to **edit source** in
   TinyMCE to correct the errors.





