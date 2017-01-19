 sp17-i524
----------

Class submissions for Spring 2017 i524

#. You will be assigned a **homework id** (or HID in the rest of this document).
#. You will be assigned a **project id** (or PID in the rest of this document).
#. Clone this repository
#. Keep your fork up to date https://help.github.com/articles/syncing-a-fork/

Before submitting, use the `check-paper.sh` and `check-project.sh`
script to check for some common submission errors.


Paper submissions
----------------

Copy the `paper_template` directory into the appropriate
`paper#/HID`. For example: if my HID is `sp17-st000`::


  $ cp paper_template paper1/sp17-st000


Before submitting, run the `check-paper.sh` script on your submission
to catch some common submission errors::


  $ ./check-paper.sh paper#/HID


When ready to submit, create a pull request to
https://github.com/cloudmesh/sp17-i524 with the subject in the form
`paper# HID`. For example: `paper1 sp17-st000`


Project submissions
------------------

Copy the `project_template` directory into the `projects/PID`
directory. For example::

$ cp project_template projects/sp17-p000


Before submitting, run the `check-project.sh` script to catch some
common errors::

$ ./check-project.sh projects/PID


When ready tp submit, create a pull request tp
https://github.com/cloudmesh/sp17-i524 with the subject in the form
`project PID`. For example: `project sp17-p000`.
