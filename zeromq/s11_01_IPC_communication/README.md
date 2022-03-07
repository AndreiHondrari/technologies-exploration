# Inter Process Communication - Basic

## Overview

- proc1 connects to proc2 in PUSH mode.
- proc2 binds in PULL mode.

## How to test

Start both of the processes in any order. You can start multiple proc1
instances.

## Observation

proc2 will receive messages from proc1 instances. There is a socket file that
was spawned alongside the processes.

## Warning

The location of the socket file is really important. If the socket file is not
reached correctly, then each process might be referring to different sockets
with the same name.

## When to use this

When you have different programs on the same machine that need to exchange
information.

## Some examples

- a file downloader notifies a file processor that it finished downloading all
  the required files
- a text indexer finished indexing and it has to notify the web service that
  triggered the indexing, that it finished.
- notify a reporting program that a scheduled job started running
