To do:


Update with the General check
lib + fct ordrer
Delete reexplanation
Intro
Interlude: add FileNotFoundError

ex06:

ft_filter:
explain "Valid" input
List fct conversion can failed but in the filterstring we know what is passing to list
so dont need too handle but in the tester its not possible for test04 to test06

ex08:
explain "Valid" input


try and except best practice:
https://python.land/deep-dives/python-try-except
https://jerrynsh.com/stop-using-exceptions-like-this-in-python/
https://jerrynsh.com/python-exception-handling-patterns-and-best-practices/
https://devblogs.microsoft.com/python/idiomatic-python-eafp-versus-lbyl/


EAFP vs LBYL

EAFP: 
Try first: Attempt the operation

LBYL:

Validate first: Check all conditions before computation

Mix,...

LBYL allow to have a better message error handling


(Re)Raise:

Quick Comparison Table
Syntax	Exception Type	Traceback	Original Context
raise	Same	Original	✅ Preserved
raise e	Same	New	❌ Lost
raise ValueError(e)	New	New	❌ Lost
raise ValueError("msg")	New	New	❌ Lost
raise ValueError("msg") from e	New	New + Original	✅ Chained


Best Practices
Use raise when you want to handle but still propagate the same exception
Use raise e when you want to re-raise from current location
Use raise ... from e when you want to replace the exception but keep original context
Avoid raise ValueError(e) - it's usually not what you want
