#from mymodule import myfunc -> Imports a single module (a module a simply .py script)
from MyMainPackage import some_main_script # -> Imports a module within a package (a package is a directory containing several modules -.py scripts-)
from MyMainPackage.SubPackage import mysubscript # -> Imports a module which is under a 2 level package (a subdirectory of main package)

## If we want to create a package (multiple modules or .py programs within a directory), we need to creatae a __init__.py file on that
# directory, so python will treat all of those modules as part a single package. If you don't specify a __init__.py inside the directory
# with multiple modules (.py sripts), you won't be able to call them using the "from [directory/package] import [module].[function]" syntax.

some_main_script.report_main()
mysubscript.sub_report()
