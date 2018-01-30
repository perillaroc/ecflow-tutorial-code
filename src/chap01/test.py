import os
import ecflow

print("Creating suite definition")
defs = ecflow.Defs()
suite = defs.add_suite("test")
suite.add_variable("ECF_HOME", os.path.join(os.getenv("HOME"), "course"))
suite.add_task("t1")
