"""
Requirements:
Implement a key value store. 
Once written, if there is a crash, make sure you can recover. 
If crash happens in during write, then that doesnt have to be recovered. 

Talk about tradeoffs in the implementation.
Write tests to verify the solution


Use the starter code
"""


class PFS:
    def set(self, key: int, value: int): ...
    def delete(self, key: int): ...
    def get(self): ...
    def free(self): ...


"""
Solution:

Pretty basic key value implenetation so use a dictionary. 
For crash recovery, the most persisitent way is to use a database. SQL ensures ACID, so once written it is persistent. 
Cant use redis bc the values are used in memory. 

>> Dont use a db
Write to a file

>> How to store info in the file
write each key value on update 

>> How 
key value into a yaml, csv, etc...

>> How about delete?
go thru each list, keys must be unique so binary search

>> That works but save each write 
Ok then save the operation

>> elaborate
save to a csv, ex.
INSERT,{key},{value}\n
DELETE,{key}\n

>> OK
[Implements]

>> Test the code, now load using the csv file.

"""


class PFS:
    def __init__(self, file: str):
        self.store = {}
        self.file = file

        # check if load from file
        if self._is_file_not_empty(file):
            self._load_from_file(file)

    def set(self, key: int, value: int):
        if key not in self.store:
            self._write("INSERT", key, value)
            self.store[key] = value

        # raise duplicate keys

    def delete(self, key: int):
        if key in self.store:
            self._write("DELETE", key)
            del self.store[key]

    def get(self, key) -> int:
        return self.store.get(key)

    def exist(self, key) -> bool:
        return key in self.store

    def _write(self, *args):
        line = ",".join(map(str, args)) + "\n"
        with open(self.file, "a") as file:
            file.write(line)

    def _is_file_not_empty(self, file):
        import os

        return os.path.exists(file) and os.path.getsize(file) > 0

    def _load_from_file(self, file):
        def csv_row_generator(file):
            import csv

            with open(file, mode="r", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    yield row

        for row in csv_row_generator(file):
            if row[0] == "INSERT":
                key, value = row[1], row[2]
                self.store[key] = value
            else:
                key = row[1]
                del self.store[key]
