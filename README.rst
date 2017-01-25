sp17-i524
----------

Repository: https://github.com/cloudmesh/sp17-i524

Class submissions for Spring 2017 i524

1. You will be assigned a **homework id** (or HID in the rest of this document).
2. You will be assigned a **project id** (or PID in the rest of this document).
3. Fork this repository by clicking the "Fork" button on the top right of this page.
   Verify that your github username is in the url. Eg::
   
      https://github.com/YOUR_GITHUB_USERNAME/sp17-i524
   
4. Clone your forked repository
5. Add the upstream repository https://help.github.com/articles/configuring-a-remote-for-a-fork/  ::

   $ git remote add upstream https://github.com/cloudmesh/sp17-i524

6. Keep your fork up to date https://help.github.com/articles/syncing-a-fork/  ::

   $ git fetch upstream
   $ git merge upstream/master
   
7. Push your changes to your fork::
   
     $ git push origin master
     
8. Create a pull request

Before submitting, use the `check-paper.sh` and `check-project.sh`
script to check for some common submission errors.



Submissions
-----------

Setup your paper or project using the ``setup`` script.
For example, if my HID is `S17-EX-0000`::

  $ ./setup paper1 S17-EX-0000

This will setup a directory ``paper1/S17-EX-0000`` with all LaTeX
materials to work on.

Please make your changes to ``report.tex``.

Before submitting a pull request, you should run the
``check-paper.sh`` and ``check-project.sh`` scripts as needed::

  $ ./check-paper.sh paper#/HID


When ready to submit, create a pull request to
https://github.com/cloudmesh/sp17-i524 with the subject in the form
`paper# HID`. For example: `paper1 sp17-st000`

