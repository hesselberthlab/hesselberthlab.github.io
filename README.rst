Github content
--------------
There are two branches in this repository. The `pelican-content` branch contains the source files for the site.
The site is served out of the `master` branch. `ghp-improt` is used to push content from the `pelican-content` branch to the `master` branch. This means that the push destroys all content in `master`, so don't make any edits in that branch.

While editing the `pelican-content` branch, you can debug the site with::

  $ make publish
  
And inspect the html in the `output/` directory.

Then::

  $ make github
  
to push all the content.

TODO
----
- Add transparent mountain pic to footer
- Add teaching link to side bar
- Figure out menu ordering
- Add Google Scholar link to side bar
