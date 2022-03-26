# Basic kill interrupt

## Overview

When issuing Ctrl+C the blocking ZMQ event loop should exit, and
KeyboardInterrupt exception should be caught, after which the socket must be
closed and the context terminated.
