"""Short script to check if CUDA is available on the system."""

import sys

from loguru import logger as log

try:
    # pyright: ignore[reportMissingImports]
    import torch  # noqa
except ImportError as e:
    log.error("torch could not be imported, exiting.")
    log.error(e)
    log.info("Installed packages matching 'torch':")
    log.info(help("modules torch"))
    sys.exit(1)

is_cuda = torch.cuda.is_available()
if is_cuda:
    log.info("CUDA is available! GPU:")
    gpu = torch.device("cuda")
    log.info(torch.cuda.get_device_name(gpu))
else:
    log.info("Torch was imported, but CUDA is not available. Using CPU.")
    gpu = torch.device("cpu")
