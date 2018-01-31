import os
from pathlib import Path
import ecflow

home = os.path.abspath(Path(Path(__file__).parent, "../../../build/course"))
try:
    print("Loading definition in 'test.def' into the server")
    ci = ecflow.Client('login05', '33083')
    ci.load(str(Path(home, "test.def")))  # read definition from disk and load into the server

    print("Restarting the server. This starts job scheduling")
    ci.restart_server()

    print("Begin the suite named 'test'")
    ci.begin_suite("test")

except RuntimeError as e:
    print("Failed:", e)
