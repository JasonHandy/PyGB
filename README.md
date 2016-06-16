# PyGB version 0.3
A simple, easy to use grade book script.

PyGB (short for Python GradeBook) was created as a result of my position as a TA
for a freshman-level "career exploration" class. As a TA, I did not have access
to the university-wide grading system, and so created the first variant of PyGB
to fulfill my need for grade-tracking software that was portable and legible.

=== INSTALLATION AND USE ===

NOTE: PyGB currently only supports Python3. If you do not have Python3 installed
[download](https://www.python.org/downloads/) the latest version.

MAC OS X (now macOS)

1.Download the latest [release](https://github.com/JasonHandy/PyGB/releases)

2.Unzip folder and place in your `Applications` folder

3.Open folder and start pygb.command (you can pin this to your dock for easier 
access.)

=== CHANGES FROM VERSION 0.2(ALPHA) ===

1. Fixed code relating to file operations while exporting XML files to .txt 
documents. Made use of `with` statement to avoid potential errors.

2. Renamed python files to more easily discern functionality

3. Added ability to create new gradebook. Also added central save folder named
(`Gradebooks`)

4. Changed format of XML files, making them easier to create and parse

