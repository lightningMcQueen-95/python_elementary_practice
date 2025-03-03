def outer():
    print("hello i am outer function")

    def inner():
        print("hello i am inner function")

    inner()

#main
outer()
print("that's all")
