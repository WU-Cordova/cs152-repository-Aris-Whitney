import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets=Array([LinkedList[Tuple[KT, VT]]() for _ in range(number_of_buckets)])
        self._size=0
        self._load_factor=load_factor
    def __getitem__(self, key: KT) -> VT:
        index=self._default_hash_function(key) % len(self._buckets)
        bucket=self._buckets[index]
        for k, v in bucket:
            if k ==key:
                return v
        raise KeyError(key)


    def __setitem__(self, key: KT, value: VT) -> None:        
        index=self._default_hash_function(key) % len(self._buckets)
        bucket=self._buckets[index]
        for k, v in bucket:
            if k== key:
                bucket.remove((k, v))
                bucket.append((key, value))
                return
        bucket.append((key, value))
        self._size +=1
    def keys(self) -> Iterator[KT]:
        return iter(self)
    
    def values(self) -> Iterator[VT]:
        for bucket in self._buckets:
            for _, v in bucket:
                yield v

    def items(self) -> Iterator[Tuple[KT, VT]]:
        for bucket in self._buckets:
            for pair in bucket:
                yield pair
    def __delitem__(self, key: KT) -> None:
        index=self._default_hash_function(key) % len(self._buckets)
        bucket=self._buckets[index]
        for k, v in bucket:
            if k ==key:
                bucket.remove((k,v))
                self._size -=1
                return
        raise KeyError(key)
    
    def __contains__(self, key: KT) -> bool:
        index=self._default_hash_function(key) % len(self._buckets)
        bucket=self._buckets[index]
        for k, _ in bucket:
            if k ==key:
                return True
        return False
    def __len__(self) -> int:
        return self._size
    
    def __iter__(self) -> Iterator[KT]:
        for bucket in self._buckets:
            for k, _ in bucket:
                yield k
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HashMap):
            return False
        if len(self) != len(other):
            return False
        for key, value in self.items():
            if key not in other or other [key] != value:
                return False
        return True

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)