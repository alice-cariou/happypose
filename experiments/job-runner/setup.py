"""
Copyright (c) 2022 Inria & NVIDIA CORPORATION & AFFILIATES. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


# Standard Library
from os import path

# Third Party
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

setup(
    name="job-runner",
    version="0.0.1",
    description="A simple utility for running jobs.",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "runjob=job_runner.runjob:main",
        ]
    },
)
