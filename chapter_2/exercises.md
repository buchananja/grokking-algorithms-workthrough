# 2.1
- When there are many inserts and few reads within a data structure, a linked 
list is more appropriate than an array. 
- Inserting items into a linked list takes O(1) as no items need to be moved to 
accomodate the new data, however inserting data into an array anywhere other 
than the end takes O(n) time as items must change index.
- When a data structure is read many times, indexes of an array allow data to
be quickly accessed in O(1). Conversely, a linked list requires O(n) time to 
read an item as each subsequent index must be accessed to reveal the location 
of the next item until the target is found.

# 2.2
- If building an application for a restaurant where orders are added to the 
beginning and removed from the end, and orders must be processed in an ordered
queue a linked list is an appropriate data structure.
- Removing and adding items to the beginning and end of a linked lists takes 
O(1) time as these positions do not require pointers from other elements of the
list.
- A linked list also requires elements to be accessed in sequential order which
maintains the order that restaurant food orders arrive (First-In, First-Out).
- In short, a resaurant will make frequent insertions/deletions but infrequent
reads in this context.
- An array would require the entire set of orders to be shifted by the number
of orders added. As such, for every new order at the beginning the entire array 
would shift by 1 place. This would also require new memory to be availible at 
the end of the array, which may not be the case.
- A linked list would allow new orders to take new places in memory that are
not contiguous with the current list of orders, preventing the entire structure
from having to be moved in memory, as might happen with an array.
- An array would further lack an order of orders like a linked list requiers
and allows.

# 2.3
- If designing a usernaming system using binary search to locate users for a
social media application an array would be preferable to a linked list.
- An array allows for random and instantaneous access of elements by index. A
binary search (assuming a sorted array) would therfore be able to randomly
access values at given indexes, taking O(1) time.
- Conversely, traversing a linked list takes O(n) time as every element needs 
to be visited to locate the target index; A binary search cannot efficiently
be used to locate data in a linked list (compared to an array) as every index 
needs to be traversed.
- While a binary search runs in O(log n) time on an array, which provides 
random access, it would perform in O(n) time on a linked list which only 
provides sequential access.

# 2.4
- When accounting for the insertion and deletion of users in an array of a
social media application several considerations must be made.
- Firstly, each insertion and deletion requires elements following the 
operation to index shift by one place, taking O(n) time. However, adding users
to the end of an array takes O(1) time as no shifting needs to occur.
- Secondly, when using binary search on an array of users, indexes will change
if users are added to the beginning or within the array.
- If using an array to track current logins, frequent insertions and deletions
would require frequent index shifting. If the array was updating in real-time
a binary search may find incorrect users as indexes for the targets would 
change in operation.
- A linked list may be more appropriate for tracking logins as this requires
frequent insertions and deletions, but relatively infrequent reads.

# 2.5
- If using an array of linked lists where indexes of the array contain the data
containing the names of the first character of user surnames and the linked
list contain users with corresponding name, this is likely to perform better
than using either an array or a linked list in isolation.
- The array would allow the namespace of users to be categorised into blocks
of names, drastically reducing the length of the initial search (26 indexes, 
one for each letter of the English alphabet); This would allow instantaneous 
random access to any letter.
- An array allows for frequent reads but infrequent insertions/deletions (new
letters are extremely unlikely to be added to the alphabet in English).
- Searching for names inside the linked list would allow users to be 
alphabetically sorted using pointers. As such, frequent insertions and 
deletions would be efficiently supported, however reads would be inefficient.
- Searching for users within the linked list would be less efficient than an
array, however insertions and deletions are frequent which arrays accomodate
inefficiently.
- This structure is known as a hash table and allows for efficient searching of
categories and efficient insertions and deletions within categories.