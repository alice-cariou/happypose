from pybind11.setup_helpers import Pybind11Extension, build_ext


def build(setup_kwargs):
    ext_modules = [
        Pybind11Extension(
            "cosypose_cext",
            ["happypose/pose_estimators/cosypose/cosypose/csrc/cosypose_cext.cpp"],
        ),
    ]
    setup_kwargs.update(
        {
            "ext_modules": ext_modules,
            "cmd_class": {"build_ext": build_ext},
            "zip_safe": False,
        },
    )
