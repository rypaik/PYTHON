[A Simple Way to Trace Code in Python | by Edward Krueger | Towards Data Science](https://towardsdatascience.com/a-simple-way-to-trace-code-in-python-a15a25cbbf51)

USAGE:
``` python

from tracefunc import tracefunc

@tracefunc
def show_args_and_kwargs(*args, **kwargs):
    return

if __name__ == "__main__":

    show_args_and_kwargs(10)
    show_args_and_kwargs(color="red")
    show_args_and_kwargs(10, 200, color="blue", type="dog"

```



TODO: Lookup functools.wrap()
