# Ventilator with kill switch

## Overview

Apart from using a ventilator -> workers -> sink setup, we add a task_count
sockets on ventilator (as connecter) and sink side (as binder) that will allow
the ventilator to inform the sink on how many tasks it wants to distribute
amongst the workers.

The workers will also have a kill socket subscriber, with which they will
connect to the sink (posing as publisher), that enables the sink to issue a kill
signal to all workers that it has finished gathering all the results from them,
so they can cleanly shut themselves down.

## How to test

- run the sink
- run several workers
- fire the ventilator

## Observations

The setup will run its normal operation, distributing tasks, workers processing
the tasks, and then finally the sink gathering the results, but with an extra
sequence of steps:

- the ventilator, before distributing the tasks, will send the total number of
  tasks to the sink
- after the sink counted all the results from the workers and it has seen that
  it matches the number of tasks reported by the ventilator, it will send an
  event for kill towards the subscriber workers
- the workers will shut themselves down
- the sink will make a clean exit

## When to use this

When you want to start a complete system for processing some numbers and you
want the system to make a clean exit after finalising.

## Some examples

- one time aerospace simulations
- scraping of information from multiple sources coming from a limited list of
  targets
