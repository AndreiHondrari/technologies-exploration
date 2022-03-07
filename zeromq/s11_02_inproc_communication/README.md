# In-process communication

## Overview

A program declares two threads, one thread binding in PULL mode and another
thread connecting to the first thread in PUSH mode.

The PUSH thread keeps sending messages, and the PULL thread keeps receiving
them.

## How to test

- start the main program

## Observation

One thread keeps sending, and the other thread keeps receiving.

## When to use this

When you want to communicate between threads of the same program.
