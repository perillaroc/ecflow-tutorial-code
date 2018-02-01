all: def

.PHONY: def replace

def:
	python test.py


replace:
	ecflow_client --host=login05 --port=33083 --suspend=/test
	ecflow_client --host=login05 --port=33083 --replace=/test ../../../build/course/test.def