# Caching

Caching is a system design concept that involves storing frequently accessed data in a location that is easily and quickly accessible.


## Benefits
* Improves application performance due to faster read/write speeds
* Prevents read/write strains on the db

## Pitfalls
* App performance might be delayed due to a huge amount of cache misses
* Limited memory
* Volatile storage
* not up-to-date data

## Types of Cache
* Browser cache
* Memory cache
* Distributed cache
* CPU cache


## Caching management techniques
With caches having a limited portion of storage to use, the following techniques are leveraged to effectively manage memory
* L.R.U. - Least recently used
* M.R.U. - Most recently used
* L.F.U. - Least frequently used
* F.I.F.O. - First In First Out
* L.I.F.O. - Last in First Out
