# PyGB version 0.4(alpha)
A simple, easy to use grade book script.

PyGB (short for Python GradeBook) was created as a result of my position as a TA
for a freshman-level "career exploration" class. As a TA, I did not have access
to the university-wide grading system, and so created the first variant of PyGB
to fulfill my need for grade-tracking software that was portable and legible.

=== INSTALLATION AND USE ===

NOTE: PyGB currently only supports Python3. If you do not have Python3 installed
[download](https://www.python.org/downloads/) the latest version.

MAC OS X (now macOS)

1.Download the latest [release](https://github.com/JasonHandy/PyGB/releases).
Make sure to download the `PYGB.ZIP` file, __NOT__ the source code.

2.Unzip folder and place in your `Applications` folder

3.Open folder and start pygb.command (you can pin this to your dock for easier 
access.)

=== CHANGES FROM VERSION 0.3(ALPHA) ===

1. Added comments to code to improve documentation in certain sections

2. Formatted XML documents created by the app (no longer one gigantic line)

3. Fixed bug where uppercase names would result in blank grade reports

4. Updated `EditXML.py`, included changes to XML creation.


=== FAQs/BUG FIXES ===

1. _"When I try to run the command file, my system says I don't have permission!"_
    To fix this problem, enter the following commands in your Terminal:
    - `cd /Applications/PYGB`
    - `chmod +x pygb.command`
    This will turn the command file into an executable if it wasn't already, and
    should fix the problem.
    

