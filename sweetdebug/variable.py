import typing


def sweetshow(
    locals_: dict, length: int = 40, exclude: typing.List[str] = ["self", "sweetshow"]
):
    def RecursivePrint(k, v, depth: int = 0):
        if isinstance(v, typing.Mapping):
            for key, value in v.items():
                print(f"{key}: {RecursivePrint(k=k, v=value, depth=depth + 1)}")
        elif isinstance(v, typing.Sequence):
            for v0 in v:
                RecursivePrint(k=k, v=v0, depth=depth + 1)
        else:
            if hasattr(v, "shape"):  # if Tensor
                strv = str(v.shape)
                if hasattr(v, "dtype"):
                    strv += " " + str(v.dtype)
            else:
                strv = str(v)
            if len(strv) > length:
                strv = strv[: length // 2] + strv[length // 2 :]
            print(f"{k} : {'['*depth} {strv} {']'*depth}")

    for k, v in locals_.items():
        if k not in exclude:
            RecursivePrint(k, v)
