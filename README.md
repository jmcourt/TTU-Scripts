# TTU-Scripts

Some handy ol' general purpose scripts from my time at TTU.

===== git_commit.sh =====

This one does some git magic.  Pushes the current directory to the master branch on github.  Requires a git to be set up in the directory, and the origin to be pointing at a master branch on github.  Call as ./git_commit.sh "commit message"

===== mode_get.py =====

If you call this inside a directory with .FITS files, this script will generate a .txt file named 'modes' which lists the datamode of all of them.  Requires astropy.

===== xtegxex.sh =====

Scans the current directory for matching RXTE gx1 and gx2 files, and merges them into good ol' goodxenon files (and places them in a subdirectory gx).  Must have FTOOLS installed and initialised.
