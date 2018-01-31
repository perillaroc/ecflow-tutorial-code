import ecflow

try:
    ci = ecflow.Client('login05', 33083)
    ci.sync_local()                                   # get server definition, by sync with client defs

    ecflow.PrintStyle.set_style( ecflow.Style.STATE )  # set printing to show structure
    print(ci.get_defs())                              # print the returned suite definition

    ecflow.PrintStyle.set_style(ecflow.Style.MIGRATE)  # set printing to show structure and state, and node history
    print(ci.get_defs())

except RuntimeError as e:
    print("Failed:", e)
