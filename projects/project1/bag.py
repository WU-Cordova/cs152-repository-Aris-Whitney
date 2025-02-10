from typing import Iterable, Optional
from ibag import IBag, T

class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.items=[]
        if items:
            for item in items:
                self.add(item)

    def add(self, item: T) -> None:
            if item is None:
                raise TypeError("You can't add nothing to the bag")
            self.items.append(item)
    def remove(self, item: T) -> None:
        self.items.remove(item)
        if item not in self.items:
            raise ValueError("You can't remove this item, it isn't in your bag.")
    def count(self, item: T) -> int:
        return self.items.count(item)
    def __len__(self) -> int:
        return len(self.items)

    def distinct_items(self) -> Iterable[T]:
        distinct_items=set(self.items)
        return distinct_items

    def __contains__(self, item) -> bool:
        if item in self.items:
            return True
        else:
            return False

    def clear(self) -> None:
        return self.items.clear()