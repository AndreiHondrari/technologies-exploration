# Putting a filter in the middle of the message

## Overview

The publisher binds and sends 3 types of messages:

- cat1 <message>
- <message> cat2
- cat3 <message>

## How to test

- spawn the subscriber
- spawn the publisher

Notice that `<message> cat2` is not received because filtering works only by
matching the prefix of the message

## Conclusion

Filtering works only for the prefix.
