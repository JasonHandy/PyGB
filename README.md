# PyGB version 0.5(alpha)
A simple, easy to use grade book app.

PyGB (short for Python GradeBook) was created as a result of my position as a TA
for a freshman-level "career exploration" class. As a TA, I did not have access
to the university-wide grading system, and so created the first variant of PyGB
to fulfill my need for grade-tracking software that was portable and legible.

=== INSTALLATION AND USE ===

NOTE: PyGB currently only supports Python3. If you do not have Python3 installed
[download](https://www.python.org/downloads/) the latest version.

MAC OS X (now macOS)

1.Download the latest [release](https://github.com/JasonHandy/PyGB/releases).
Make sure to download the `.ZIP` file, __NOT__ the source code.

2.Unzip folder and place into your `Applications` folder

3.Open folder and start pygb.command (you can pin this to your dock for easier 
access.)

=== CHANGES FROM VERSION 0.4 ===

1. Added more documentation to source code

2. Updated error handling to ensure that grade books both exist and are 
populated with students.

3. Removed global variables from all modules

4. Updated UI and closed inescapable menu loops

5. Added rudimentary class statistics


=== FAQs/BUG FIXES ===

1. _"When I run the command file, my system says I don't have permission!"_

    To fix this problem, enter the following commands in your Terminal:
    - `cd /Applications/PYGB`
    - `chmod +x pygb.command`
    This will turn the command file into an executable if it wasn't already, and
    should fix the problem.
    
2. _"For some reason, I don't want to download Python3, will PyGB be available
for systems with only Python2 installed?"_

    Not in the near future, as keeping two versions of software current is more
    work than I would like to dedicate to this project. Once the final release
    of PyGB is out (probably v1.0), I may work on porting it to Python2.
