sp17-i524
----------

Repository: https://github.com/cloudmesh/sp17-i524

Class submissions for Spring 2017 i524

Prerequisites
~~~~~~~~~~~~~

You will be assigned a **homework id** (or `HID` in the rest of this document).
You can verify your HID in `this Piazza
thread <https://piazza.com/class/ix39m27czn5uw?cid=31>`_.

You will be assigned a **project id** (or `PID` in the rest of this document).

Additionally, we assume you have a GitHub account an uploaded your SSH key:

- `Linux Instructions <https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/#platform-linux>`_
- `Windows Instructions <https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/#platform-windows>`_
- `Mac Instructions <https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/#platform-mac>`_
   
We will be referring to your GitHub username as ``YOUR_GITHUB_USERNAME`` in the rest of this document.

Setup Git
~~~~~~~~~

1. First, make sure that git on your computer is configured properly. For
example::

  $ git config --global user.name "Albert Zweistein"
  $ git config --global user.email albert.zsweistein@gmail.com

   
2. Fork this repository by clicking the "Fork" button on the top right of this page.
   You will be redirected to a new page.
   Verify that your github username is in the url. Eg::
   
      https://github.com/YOUR_GITHUB_USERNAME/sp17-i524
   
3. Clone your forked repository::

    git clone git@github.com:YOUR_GITHUB_USERNAME/sp17-i524.git
   
4. Add the upstream repository https://help.github.com/articles/configuring-a-remote-for-a-fork/  ::

   $ git remote add upstream https://github.com/cloudmesh/sp17-i524
   

Setting up Each Homework Assignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set up your paper or project using the ``setup`` script. You can
always check the script usage with::

  $ ./setup
  
Thus, if you are getting ready to work on paper and your `HID` is
`S17-EX-0000`, you would run::

  $ ./setup paper1 S17-EX-0000

This creates an *S17-EX-0000* directory under *paper1*, and places a
paper template there. You will use that template as the starting point
for your paper or project.

**NOTE**: You should frequently keep your fork up to date https://help.github.com/articles/syncing-a-fork/  ::

   $ git fetch upstream
   $ git merge upstream/master
   
**NOTE** You should also periodically push your changes to your fork::
   
     $ git push origin master


Working with LaTeX and the Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to make sure that LaTeX is installed on your computer. There
are different LaTeX environments for different operating systems. We
recommend `TeXLive <http://www.tug.org/texlive>`_ for Linux, `MacTeX
<http://www.tug.org/mactex/>`_ for OSX, `TexLive
<http://www.tug.org/texlive>`_ for Windows. In addition, there are
online LaTeX environments that you can use independent of what your OS
is. One we recommend is `ShareLaTeX <https://www.sharelatex.com/>`_.

If you have a LaTeX environment set up on your compute, you can compile the template by using the *make* utility that comes with the template. For example::

  $ cd paper1/S17-EX-0000
  $ make

This will compile the contents of the *report.tex* file in the template directory, resolve the references in *references.bib* and create a *report.pdf* file that you can then look at in your favorite PDF viewer.

If you are using an online environment like ShareLaTeX, you will need to import the template files into it and compile the template that way.

From here on, you can edit *report.tex* and *references.bib* to complete your paper or project.


Submission
~~~~~~~~~~

First, make sure your repository is synchronized with the *upstream*::

  $ git fetch upstream
  $ git rebase upstream/master

Build your report using the ``make`` command.

Push your changes and submit a pull request::

  $ git push origin master

Once you are done with your paper or project, you will need to generate a pull request to 

When ready to submit, create a pull request to
https://github.com/cloudmesh/sp17-i524 with the subject in the form
`paper# HID`. For example: `paper1 S17-EX-0000`


