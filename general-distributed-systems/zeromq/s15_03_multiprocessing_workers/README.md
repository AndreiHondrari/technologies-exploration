# Multiprocessing REQ/REP dynamic worker repliers

## Overview

Similar to multithreaded repliers, but in this case we use the multiprocessing
module to circumvent the Global Interpreter Lock from Python and to truly
parallelise work between repliers.
