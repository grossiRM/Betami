README.TXT


         MF2005-FMP2 (MODFLOW-2005 - Version: 1.6.01 and FMP2 - Version 1.0.00)
         Three-dimensional finite-difference ground-water flow model


NOTE: Any use of trade, product or firm names is for descriptive purposes 
      only and does not imply endorsement by the U.S. Government.

This version of MODFLOW is referred to as MF2005-FMP2 in order to distinguish
it from older versions of the code and other versions of MODFLOW. 
This version of MODFLOW-2005 is packaged for personal computers using the Microsoft 
Windows XP or Vista operating systems.  Executable files for personal computers are provided 
as well as the source code.  The source code can be compiled to run on other computers.

IMPORTANT: Users should review the file MF2005_FMP2.txt for a description of, and
references for, this software. Users should also review the file release.txt,
which describes changes that have been introduced into MF2005-FMP2 with each
official release; these changes may substantially affect users.

Instructions for installation, execution, and testing of MODFLOW-2005 are
provided below.



                            TABLE OF CONTENTS

                         A. DISTRIBUTION FILE
                         B. INSTALLING
                         C. EXECUTING THE SOFTWARE
                         D. TESTING
                         E. COMPILING


A. DISTRIBUTION FILE

The following self-extracting distribution file is for use on personal
computers:

         mf2005fmp2v1_0_00.exe

The distribution file contains:

          Compiled runfiles and source code for MF2005-FMP2.
          Supplementary MF2005-FMP2 documentation in PDF and text files.
          Test data sets.

The distribution file is a self-extracting program.  Execution of the
distribution file creates numerous individual files.  The extraction
program allows you to specify the directory in which the files should
be restored.  The installation instructions assume that the files are
restored into directory C:\WRDAPP.  The following directory structure
will be created in C:\WRDAPP:


   |
   |--MF2005FMP2.1_0
   |  |--bin          ;        MODFLOW-2005 executables for personal computers
   |  |--doc          ;        Documentation files
   |  |--example_model;        Input and output and spreadhseets to run verification tests and understand new FMP2 features with Example Model
   |  |--src          ;        MF2005-FMP2 source code for use on any computer
   |     |hydprograms ;        Source for hydrograph post processing program


It is recommended that no user files are kept in the mf2005fmp2.1_0 directory
structure.  If you do plan to put your own files in the mf2005fmp2.1_0
directory structure, do so only by creating additional subdirectories.

Included in directory mf2005fmp2.1_0\doc are various documentation files.  Some
of them are Portable Document Format (PDF) files. The PDF files are readable
and printable on various computer platforms using Acrobat Reader from Adobe.
The Acrobat Reader is freely available from the following World Wide Web
site:
      http://www.adobe.com/


B. INSTALLING

To make the executable versions of MODFLOW-2005 accessible from any
directory, the directory containing the executable (mf2005.1_6\bin)
should be included in the PATH environment variable.  Also, if a
prior release of MODFLOW-2005 is installed on your system, the
directory containing the executables for the prior release should
be removed from the PATH environment variable.

As an alternative, the executable files, mf2k5_fmp2.exe and mf2k5_fmp2_64.exe,
in the mf2005fmp2.1_0\bin directory can be copied into a directory already
included in the PATH environment variable. THe mf2k5_fmp2_64 is for running on 64-bit 
Windows operating system.

       HOW TO ADD TO THE PATH ENVIRONMENT VARIABLE
                  WINDOWS XP SYSTEMS
             
From the Start menu, select Settings and then Control Panel.  Double click
System and select the Advanced tab.  Click on Environment Variables.  If
a PATH user variable already is defined, click on it in the User Variables
pane, then click Edit.  In the Edit User Variable window, add
";C:\WRDAPP\mf2005fmp2.1_0\bin" to the end of the Variable Value (ensure that
the current contents of the User Value are not deleted) and click OK.  If
a PATH user variable is not already defined in the User variables pane of
the Environment Variables window, click New.  In the New User Variable
window, define a new variable PATH as shown above.  Click OK.  Click OK
in the Environment Variables window and again in the System Properties
window.  Initiate and use a new Windows Command window.

       HOW TO ADD TO THE PATH ENVIRONMENT VARIABLE
                 WINDOWS VISTA SYSTEMS
             
From the Start menu, select Settings and then Control Panel.  Select
System & Maintenance followed by System.  Choose the Advanced System
option.  Select the Settings Task, and then select the Environmental
Variables button.  In the System Variables pane, select the PATH
variable followed by Edit.  In the Edit window, add
";C:\WRDAPP\mf2005fmp2.1_0\bin" to the end of the Variable Value (ensure
that the current contents of the User Value are not deleted) and click
OK. Click OK in the Environment Variables window and then exit from the
control panel windows.  Initiate and use a new Windows Command window.


C. EXECUTING MODFLOW-2005

Two MF2005-FMP2 runfiles for use on personal computers are provided. 
mf2k5_fmp2.exe is the 32-bit version of MODFLOW-2005 (version 1.6.01) with FMP2
version 1.0). It uses mixed single and double precision for
computations and internal data storage, which was determined to be useful
for a wide range of simulations.  There are situations in which speed and 
precision are inadequate, which can be indicated by difficulty attaining
solver convergence or poor budget error and excessibley long runtimes.  
Accordingly, a runfile that uses 64-bit precision is provided -- mf2k5_fmp2_64.exe. 
If mixed precision is suspected of causing problems in a simulation or or slow runtimes are 
problematic of parameter estimation settings, the same simulation can be run using the 64-bit runfile.  
Input for the two runfiles is the same. In fact the source code is identical for
both. The 64-bit precision runfile is created by using a compiler option
that raises the precision and can take advantage of increased speed of the 64-bit 
operating system.

The advantage for using 64-bit technology is additional precision and computational speed,
The disadvantage are unformatted (binary) files that are doubled in size.  
(Binary files are used for saving head, drawdown, and budget data.) This penalty is 
frequently not very significant.  Typical computers have adequate memory to run most simulations in 64-bit mode, 
are 2 to 8 times as fast performing than 32-bit run file, and have
abundant disk space for storing binary output files.

After the executable files in the mf2005fmp2.1_0\bin directory are installed
in a directory that is included in your PATH, MF2005-FMP2 is initiated in
a Windows Command-Prompt window or windows batch file using one of the following commands:

          mf2k5_fmp2_dbg32 [Fname] or  mf2k5_fmp2_rls32 [Fname]
or
          mf2k5_fmp2_dbg64 [Fname] or   mf2k5_fmp2_rls64 [Fname]

The optional Fname argument is the name file.  If no argument is used,
the user is prompted to enter the name file.  If the name file ends in
".nam", then the file name can be specified without including ".nam". 
For example, if the name file is named abc.nam, then the simulation can
be run using mixed precision by entering:

          mf2k5_fmp2_rls32 abc

The data arrays in MF2005-FMP2 are dynamically allocated, so models
are not limited by hard-coded array limits. However, it is best to have
enough random-access memory (RAM) available to hold all of the required
data.  If there is less available RAM than this, the program will use
virtual memory, but this slows computations significantly.

Some of the files written by MF2005-FMP2 are unformatted files. The structure
of these files depends on the precision of the data in the program,
the compiler, and options in the Fortran write statement.  Any program
that use the unformatted files produced by MF2005-FMP2 must read the files
in the same way they were written. For example, Zonebudget and Modpath
use unformatted budget files produced by MF2005-FMP2.  Current versions of
Zonebudget and Modpath automatically detect the precision of the data in
unformatted files and the runfiles provided by the USGS are compatible
with the structure of the unformatted files produced by this release of
MF2005-FMP2.

Another example of unformatted files is head files that are generated by
one MF2005-FMP2 simulation and used in a following simulation as initial
heads.  Both simulations must be run using an executable version of
MF2005-FMP2 that uses the same unformatted file structure.  MF2005-FMP2 does
not automatically detect precision of the data in these files, so both
simulations must be run using a runfile having the same precision (32-bit or 64-bit).

This issue of unformatted files is described here so that users will
be aware of the possibility of problems caused by unformatted files. 
Older versions of MODFLOW executables provided by the U.S. Geological
Survey (USGS) may produce different kinds of unformatted files.  The
current form of unformatted file has been used in USGS MODFLOW
executables starting with version 1.2 of MODFLOW-2000.


D. TESTING

Example data sets are provided to verify that MF2005-FMP2 is correctly
installed and running on the system.  The example model may also be looked
at as examples of how to use MF2005-FMP2.  The directory
MF2005FMP2.1_0\example_model contains the input data for running each example. 
Directory MF2005FMP2.1_0\example_model_out contains the output files from running
each example. The example models are described in the file MF2005FMP2.1_0\doc\example_model_instructions.pdf.

The directory MF2005FMP2.1_0\example_model can be used to conveniently run the
tests without destroying the original results in the MF2005FMP2.1_0\example_model_out
directory.  The example_model directory contains MF2005-FMP2 name files, which end
with ".nam", for running the tests that can be run with the batch file example1.bat.  
The example model can be run by entering the name file for the test when executing MF2005-FMP2.  
MF2005-FMP2 should be run in a command-prompt window with the current directory being the
example_model directory or with the example1.bat file.  The output files that are created in the 
example_model_out directory can then be compared to those in MF2005FMP2.1_0\example_model_out.


E. COMPILING

The executable files provided in MF2005FMP2.1_0\bin were created using the Intel
Visual Fortran (11.1.048) and C++ (11.1.048)  compilers.  Although executable versions of the program are provided, 
the source code is provided in the mf2005FMP2.1_0\src directory so that MF2005-FMP2 can be 
recompiled if necessary.  However, the USGS cannot provide assistance to those compiling
MODFLOW. In general, the requirements are a Fortran compiler, a compatible
C compiler, and the knowledge of using the compilers. The compiler options used with the Intel
Fortran compiler that were used to create these executeable versions of MF2005-FMP2 are:

Debug command line for MF2005-FMP2:
/nologo /debug:full  /Od /fpe:0 /module:"$(INTDIR)/" /object:"$(INTDIR)/" /traceback /check:all /libs:static /threads /dbglibs /c

Release command line used for MF2005-FMP2:
/nologo /Od /fpe:0 /Qsave /module:"$(INTDIR)/" /object:"$(INTDIR)/" /libs:static /threads /c

In order to compile the code as Double Precision code the Intel Visual Fortran compilers provide the following compiler option:
/real_size:64
which can be set under "Data" > "Defaul Real KIND" > set to "8 (/real_size:64)"

Newest versions of the Intel Visual Fortran compilers (> 10.1.xx) has compiler options as default when building a new project that have default 
  interface checks that will cause variable declaration conflicts and we recommend when building your mixed Fortan and C++ project, 
  DO NOT use these compiler options:
  (a) under "Diagnostics" > "Generate Inteface Blocks" > Yes /gen-interfaces
  (b) under "Diagnostics" > "Check Routine Interface" > Yes /warn:interfaces

The GMG solver is included in the executeable version of MF2005-FMP2. 
When the GMG solver is to be included, a C compiler and mixed language code must be created.
If a compatible C compiler is not available, the GMG solver can be removed so that only a Fortran compiler
is required.  File Nogmg.txt in the src directory contains instructions for
removing GMG from MODFLOW.

Additional suggestions for compilation can be found at:

http://water.usgs.gov/nrp/gwsoftware/modflow2000/MFDOC/index.html?suggestions_on_compiling.htm

NOTE: In the suggestions for Microsoft Visual Studio 2005 with Intel Fortran Compiler 9.1 --

In gmg1.f after the line containing "SUBROUTINE RESPRINT": 
DO NOT insert line:
          !DEC$ ATTRIBUTES ALIAS:'_resprint' :: RESPRINT
into Subroutine Resprint as suggested.

In Step 15.) Instead of typing "MSVCRT" for "Ignore Specific Library," type "MSVCRTD" for Debug version

