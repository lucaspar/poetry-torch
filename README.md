# Installing PyTorch with Poetry

Conditionally installing hardware-accelerated PyTorch with Poetry on different hardware using the same `pyproject.toml` [can be tricky](https://github.com/python-poetry/poetry/issues/6409). This repo serves as a quick lookup for the configuration file and installation commands.

+ [Installing PyTorch with Poetry](#installing-pytorch-with-poetry)
    + [Installation Modes](#installation-modes)
    + [Embedding the choice in a script](#embedding-the-choice-in-a-script)
    + [Trying it out](#trying-it-out)
    + [Switching versions / upgrading](#switching-versions--upgrading)
        + [CUDA](#cuda)

## Installation Modes

| Command                           | Behavior                                                       |
| --------------------------------- | -------------------------------------------------------------- |
| `poetry sync`                     | Does not install PyTorch (import fails).                       |
| `poetry sync -E cpu`              | Installs PyTorch with CPU only.                                |
| `poetry sync -E cuda --with cuda` | Installs the CUDA variant of PyTorch. Expects NVIDIA hardware. |

>[!WARNING]
> The example below is likely not what you want:
>
> | Command               | Behavior                                                                 |
> | --------------------- | ------------------------------------------------------------------------ |
> | `poetry sync -E cuda` | Actually installs the CPU variant of PyTorch without errors or warnings. |

The [`sync` command](https://python-poetry.org/docs/cli#sync) behaves like the old `poetry install --sync`, and it's better suited to keep the current local state in sync with your lock file, as it will also remove dependencies missing from the lock. You probably want to use it instead of `poetry install` to avoid untracked outdated packages in most cases.

## Embedding the choice in a script

```bash
if lspci | grep -i nvidia; then
    poetry sync --extras=cuda --with cuda
else
    poetry sync --extras=cpu
fi
```

## Trying it out

```bash
poetry run python check-cuda.py
```

or

```bash
poetry run python -c "import torch; print(torch.cuda.is_available())"
```

## Switching versions / upgrading

+ [Torch/Python/CUDA Compatibility Matrix of Releases](https://github.com/pytorch/pytorch/blob/main/RELEASE.md#release-compatibility-matrix)
+ [Torchvision Versions (wheels)](https://download.pytorch.org/whl/torchvision/)

### CUDA

+ [CUDA Compute Capability numbers by GPU model](https://developer.nvidia.com/cuda-gpus#compute)
+ [CUDA Version Matrix by Driver Version](https://docs.nvidia.com/deploy/cuda-compatibility/#id3)
