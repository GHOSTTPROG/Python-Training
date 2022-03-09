
def function1():
    a, b, c = 1, 2, 3

    print(
        f"[BEFORE-FUNC1] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")

    def function2():
        # For changing nonlocal variables from outer scope, you should use nonlocal. see nonlocal_scope3.py
        a, b, c = 11, 12, 13

        print(
            f"[FUNC2] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")

    function2()
    print(
        f"[AFTER-FUNC1] a: {a}, id(a): {id(a)}| b: {b}, id(b): {id(b)}| c: {c}, id(c): {id(c)}")


function1()
