#hello world
import builtins
names = [name for name, function in sorted(vars(builtins).items())]
print(names)
