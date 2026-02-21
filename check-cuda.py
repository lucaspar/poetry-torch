"""Short script to check if CUDA is available on the system."""

import sys

from loguru import logger as log


def check_cuda_device() -> tuple[bool, str | None]:
    """Checks if CUDA is available on the system.

    Returns:
        True if CUDA is available, False otherwise.
        The name of the GPU if CUDA is available, or None if not.
    """
    try:
        import torch  # pyright: ignore[reportMissingImports]
    except ImportError as e:
        log.error("torch could not be imported, exiting.")
        log.error(e)
        log.debug("Installed packages matching 'torch':")
        log.debug(help("modules torch"))
        sys.exit(1)

    is_cuda = torch.cuda.is_available()
    device_name: str | None = None
    if is_cuda:
        gpu = torch.device("cuda")
        device_name = torch.cuda.get_device_name(gpu)
    else:
        gpu = torch.device("cpu")
    return is_cuda, device_name


if __name__ == "__main__":
    is_available, device_name = check_cuda_device()
    if is_available:
        log.info(f"CUDA is available! GPU: {device_name}")
    else:
        log.warning("CUDA is not available on this system.")
