Github content
--------------
There are at least two branches in this repository:

The `pelican-content` branch contains the source files for the site. It is
also the production branch, so don't make drastic changes to this branch.

The site is served out of the `master` branch. `ghp-import` is used to
push content from the `pelican-content` branch to the `master` branch.
The push destroys all content in `master`, so don't make any edits in this
branch.

To make changes to the site content, checkout a new branch::

    $ git branch -b pelican-dev

Then make changes in this branch, and debug the site with::

  $ make publish
  
Inspect the html in the `output/` directory.

Then::

  $ make github
  
to push all the content.

TODO
----
- Update people page
- Add protein blurb on front pagee
- Add transparent mountain pic to footer
