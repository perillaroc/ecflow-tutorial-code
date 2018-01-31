import ecflow

try:
    ci = ecflow.Client('login05', 33083)
    ci.sync_local()                                   # get server definition, by sync with client defs
    ecflow.PrintStyle.set_style( ecflow.Style.DEFS )  # set printing to show structure

    print(ci.get_defs())                              # print the returned suite definition
except RuntimeError as e:
    print("Failed:", e)