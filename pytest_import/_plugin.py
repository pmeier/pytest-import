import importlib
import importlib.util
import pathlib
import pkgutil
import sys

HERE = pathlib.Path(__file__).parent


def import_from_path(path: pathlib.Path):
    if path.is_file():
        name = path.stem
    else:
        name = path.name
        path = path / "__init__.py"

    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def maybe_import_package(path: pathlib.Path) -> None:
    if not path.is_dir():
        return None

    if not (path / "__init__.py").exists():
        return None

    sys.modules[path.name] = import_from_path(path)

    for _, name, is_package in pkgutil.walk_packages([str(path)]):
        # FIXME: do a reverse matching of what pytest does
        if name.startswith("test") or is_package:
            continue

        sys.modules[f"{path.name}.{name}"] = import_from_path(path / f"{name}.py")


def pytest_sessionstart(session) -> None:
    if session.config.option.importmode != "importlib":
        return None

    # FIXME: extract the paths from the session
    for path in (HERE.parent / "tests",):
        maybe_import_package(path)
