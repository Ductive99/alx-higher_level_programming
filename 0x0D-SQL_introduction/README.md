# SQL

Data is incredibly important, and managing it is a challenging tasks.
SQL (Structured Query Language) is a way to manage it.

In the past we used JSON file to store data.

### So, Why not store data in flat files?

Well a solid database is expected to be acid which means it guarentees:
- *A***tomicity**: transactions are atomic, which means if a transaction fails, the result will be like it never happened.
- *C***onsistency**: you can define rules for your data, and expect that the data abides by the rules, or else the transaction fails.
- *I***solation**: run two operations at the same time, and you can expect that the result is as though they were ran one after the other. That’s not the case with the JSON file storage you built: if 2 insert operations are done at the same time, the later one will fetch an outdated collection of users because the earlier one is not finished yet, and therefore overwrite the file without the change that the earlier operation made, totally ignoring that it ever happened.
- *D***urability**: unplug your server at any time, boot it back up, and it didn’t lose any data.
