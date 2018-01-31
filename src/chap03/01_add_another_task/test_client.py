import os
from pathlib import Path
import ecflow

home = os.path.abspath(Path(Path(__file__).parent, "../../../build/course"))
try:
    print("Loading definition in 'test.def' into the server")
    ci = ecflow.Client('login05', '33083')
    ci.delete("/test")
    ci.load(str(Path(home, "test.def")))
    ci.begin_suite("test")
except RuntimeError as e:
    print("Failed:", e)
