Algebra
================

Usage
------
.. code-block:: python

    from mathematics.algebra import Variable, Term

    x = Variable('x')
    y = Variable('y')
    t = Term([x], 4)
    t1 = Term([y], 3)
    print(t*t1)
    # 12xy
