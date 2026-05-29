# Mini-project report 
Members: David Nordin and Josip Lipovac  
Program: Computer Science
Course: 1DV501
Date of submission: 2022-12-29


## Introduction  
During this project, the group was going to learn about data structures such as hashing and binary search trees. Two large text files from a previous assignment were going to be used as input data in said data structures. The previous assignment is a part of the course 1DV501 and the text files contain a lot of words. One of the files, brian.txt, contains the words from the script of the movie “Monty Python’s Life of Brian” which is in English. The other file, swenews.txt, is a compilation of sentences from Swedish newspapers which obviously is in Swedish. Both of the text files are a word on separate lines. 

This task could be divided into three separate parts:
Count unique words using Python’s set and dictionary.
Implement two data structures: a hash based set and a binary search tree based map.
Use the two data structures to repeat Part 1.  


## Part 1: Count unique words 1
In part 1 the group was going to implement a python program which counts every unique word in the data files using Python’s set and data classes. The set class is going to be used to count the number of unique words in each file. The dictionary class will be used to present the 10 most used words that are larger than 4 in each file. Brian.txt contained 13380 words and swenews.txt contained 15095373 words. However there are duplicate words in these files so this is how the problem was solved.

The program, part1.py, started by importing the os module so the current working directory (cwd) could be reached easily. Then we used a function called get_words where path is the cwd and name is the name of the file. When these get combined the path to the file is open to the program and the file’s content can be used.


```python
def get_words(path, name):
    path += name
```

Then we open the file for reading using the encoding utf-8 so that letters such as Å, Ä and Ö can be used without an error. The file is called “file”.
```python
    with open(path, "r", encoding='utf-8') as file:
```

Then we have “count” which goes up by 1 every time a unique word is presented. The content of the file is then stored in “data”. Then “data” is split into a list called “words” and uses the set function which removes duplicate words as they aren’t necessary for counting unique words. Then for every word in the list “words”, “count” goes up by 1.
```python
        count = 0
        data = file.read()
        words = set(data.split())
        for word in words:
            count += 1
```

Here is when the dictionary class is used to present the 10 most used words. The data from the file is split into a list called words2 and a dictionary called “dct” is created. Then every word in “words2” goes through a loop that adds every word larger than 4 into the dictionary. The word is stored as a key in the dictionary and the number of times a word is used is stored as value. If a word is already a key in the dictionary, the value associated with the word goes up by 1. Otherwise the word is added as a key with the value 1.
```python
        words2 = data.split()
        dct = {}
        for word in words2:
            if len(word) > 4:
                if word in dct:
                    dct[word] = dct[word] + 1
                else:
                    dct[word] = 1
```

Now the content of the dictionary is sorted based on its value, which is how many times the word is used in “value_sorted”. The sorted function results in the words that occur the least gets placed first. Therefore the dictionary gets reversed. Then the program prints out the 10 first elements in the dictionary, which are the elements with the biggest values. Also “count” is returned. 
```python
        value_sorted = sorted(dct.items(), key=lambda tpl: tpl[1])
        value_sorted.reverse()
        for i in range(10):
            print(value_sorted[i][0], ":", value_sorted[i][1])
        print()
        return count
```

 10 most used words from Life of Brian (brian.txt)
Brian - 368
Centurion - 116
 crowd - 101
Mother - 95
right - 77
Crucifixion - 72
Pilate - 68
Pontius - 64
Crowd - 60
Rogers - 52

Number of unique words in Life of Brian: 2416


10 most used words from Swedish News (swenews.txt)
säger - 47502
under - 44905
kommer - 42053
efter - 36406
eller - 30806
också - 30119
andra - 27106
finns - 26793
sedan - 24818
procent - 23451

Number of unique words in Swedish News: 456402


## Part 2: Implementing data structures
The two data structures that were used in this project were a Hashing set and a Binary search tree (bst) Map. Let’s start off with the Hashing set.

The add function starts off by getting the hashing value for the given word, which is stored in “value”. Then if there are no more buckets available in the hash set, “self.size” is set to 0 and a rehash is triggered. Otherwise the program checks if the word isn’t in the bucket with the matching hash value. That is when the word is added to the bucket with the appropriate hash value and “self.size” is increased by 1. 
```python
   def add(self, word):
        value = self.get_hash(word)
        if self.bucket_list_size() == self.size:
            self.size = 0
            self.rehash()
        if word not in self.buckets[value]:
            self.buckets[value].append(word)
            self.size += 1
```

To get the hash value, the function “get_hash” is used. The program starts off with “hash_value” which is given no value and “num” that starts off at 1. Then the ascii value for “i”, the first letter in “word”, is calculated using the function “ord” in a for-loop. The “ord” function returns an integer for a unicode character and the function was found on the website W3schools. The ascii value for “i” with “num” as an exponent is added to “hash_value” and “num” is increased by 1 for each iteration in the for-loop. When the ascii value for each letter has been added to “hash_value”, the value goes through modulo the number of buckets. The result of that calculation is the hash value for a word. 
```python
   def get_hash(self, word):
        hash_value = int()
        num = 1
        for i in word:
            hash_value += ord(i) ** num
            num += 1
        result = hash_value % len(self.buckets)
        return result
```

Finally the rehashing function, “rehash”. It starts off by making a list copy of the content from the buckets. Then new, empty buckets get added to “self.buckets” that is double the amount than before. Essentially, “self.buckets” gets filled with empty buckets that are twice as many as before the rehash. Lastly, the content from the copy list gets added back into “self.buckets” using the “add” function. The content is added back using two for-loops. 

```python
   def rehash(self):
        copy_lst = list(self.buckets)
        self.buckets = [[] for i in range(len(copy_lst) * 2)]
        for lists in copy_lst:
            for content in lists:
                self.add(content)
```


- For the BST based map (BstMap), present (and explain in words):
 	* Python code for the two functions ``put`` and ``max_depth``.
 	* Point out and explain any differences from the given results in ``bst_main.py``.



The “put” function starts off by checking if the key is already in the Bst map. Otherwise the program checks if the key is smaller then it looks into the left subtree. If there is no left child then the key becomes the left child. Otherwise the “put” function gets repeated. The same process is repeated if the value is larger except it features the right child. 
```python
   def put(self, key, value):
        if key == self.key:
            self.value = value
        elif key < self.key:  # if its smaller adds it to the left subtree
            if self.left is None:  # check if there is a left child
                self.left = Node(key, value)
            else:
                self.left.put(key, value)  # add to existing node
        else:  # if its larger adds it to the right subtree
            if self.right is None:  # check if there is a right child
                self.right = Node(key, value)
            else:
                self.right.put(key, value)
```

The “max_depth” starts off by left_depth and right_depth, who both are equal to 0. Then if the left child is not empty then left_depth is added by a recursive function of “max_depth”. Same logic for the right child as well. Then if the value for the “left_depth” is larger than the “right_depth”, “left_depth” + 1 is returned. If the opposite is true, “right_depth” + 1 is returned. 
```python
    def max_depth(self):
        left_depth = 0
        right_depth = 0
        if self.left is not None:
            left_depth += self.left.max_depth()
        if self.right is not None:
            right_depth += self.right.max_depth()
        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1
```



Result of Bst in part 2
{ (Adam,27) (Ceve,37) (Ella,39) (Fred,44) (Owen,40) (Zoe,41) }
Size: 6

Override existing values
{ (Adam,27) (Ceve,100) (Ella,39) (Fred,44) (Owen,40) (Zoe,99) }

Get(Fred): 44
Get(Jonas): None
Max depth: 3
Count leafs: 3

Size: 10
Max depth: 6
Count leafs: 4
To_string:  { (AA,1) (AAA,2) (AAAA,3) (AAAAA,4) (Adam,27) (Ceve,100) (Ella,39) (Fred,44) (Owen,40) (Zoe,99) }

List size and element type: 10 <class 'tuple'>
List content: [('AA', 1), ('AAA', 2), ('AAAA', 3), ('AAAAA', 4), ('Adam', 27), ('Ceve', 100), ('Ella', 39), ('Fred', 44), ('Owen', 40), ('Zoe', 99)]

There are differences when overriding existing values and adding new key pairs to the map. When overriding “(Ceve,37)” and “(Zoe,41)” to “(Ceve,100)” and “(Zoe,99)” there is a difference that is quite obvious. In “bst_main.py” the value becomes updated to the latter of Ceve and Zoe. 

When adding new key pairs to the map, the content of the Bst map, max depth, count leafs and size changes. This is due to the fact that ('AA', 1), ('AAA', 2), ('AAAA', 3) and ('AAAAA', 4) get added to the map. Which obviously changes the size, content, depth and leafs of the Bst.


## Part 3: Count unique words 2
To implement a solution to the Top-10 part of the problem, a function called “top_ten” was added to the python program “part_3.py”. 

The function starts off by getting the leafs, map size and max depth from the Bst map from part 2 using either brian.txt or news.txt as data input. Then the function goes through every word from “words'' while also calling the function get. If the word is larger than 4 and if the word is not nothing then the word gets added to the Bst. If the word already is in the bst then the value increases by 1. 

To print out the top 10 words, a similar method is used as in part 2. The content of the Bst gets sorted based on value, whereas the smaller values get put first. Invert said sorting and now the words with the highest values get put first. Then just print the 10 first elements in the sorted list.
```python
def top_ten(words):
    leafs = bst_map.count_leafs()
    size = bst_map.size()
    max = bst_map.max_depth()
    for word in words:
        bst_words = bst_map.get(word)
        if len(word) > 4:
            if bst_words is not None:
                bst_map.put(word, bst_words + 1)
            else:
                bst_map.put(word, 1)
    print("BST-stats")
    print(f"max depth: {max}")
    print(f"Leaf count: {leafs}")
    print(f"number of nodes: {size}")
    sort_value = sorted(bst_map.as_list(), key=lambda v: v[1], reverse=True)
    print("\nTop 10 words")
    for i in range(10):
        print((sort_value[i][0]), (sort_value[i][1]))
    return ""
```

  10 most used words from Life of Brian (brian.txt)
Brian - 368
Centurion - 116
crowd - 101
Mother - 95
right - 77
Crucifixion - 72
Pilate - 68
Pontius - 64
Crowd - 60
Rogers - 52

Number of unique words in Life of Brian: 2417

Results from Hashing (Life of Brian)
Bucket list size: 4096
Max bucket size: 5
Zero bucket ratio: 0.56

Results from Bst (Life of Brian)
Total node count: 2416
Max depth: 28
Leaf count: 787


10 most used words from Swedish News (swenews.txt)
säger - 47502
under - 44905
kommer - 42053
efter - 36406
eller - 30806
också - 30119
andra - 27106
finns - 26793
sedan - 24818
procent - 23451

Number of unique words in Swedish News: 456402

Results from Hashing (Swedish News)
Bucket list size: 524288
Max bucket size: 8
Zero bucket ratio: 0.43

Results from Bst (Swedish News)
Total node count: 456402
Max depth: 123
Leaf count: 147374


Max bucket size is the bucket that has the most elements in it. That means that every other bucket has less in them compared to the max bucket size. If max bucket size is equal to 8 that means every other bucket has 7 or less elements in them. Ideally, max bucket size would be as low as possible so that multiple values get spread out evenly across the entire hashing set. However that may be difficult when a hashing set gets a large data input such as with Swedish news. 

Zero bucket ratio is the number of buckets that are empty divided by the total amount of buckets. If a zero bucket ratio is 0.5 that means that half of the buckets are empty. Like with max bucket size, it is ideal if the ratio is as low as possible. Considering the fact that empty buckets aren’t contributing anything and are just taking up space. Also when searching the set, more time will be spent by looking at empty buckets. Therefore, less empty buckets is more optimal.

Max depth is essentially the height of the Bst. It is measured by calculating the amount of nodes from the root node to the farthest leaf node(s). In the best case scenario, the max depth is as low as possible so that it takes less time to calculate the height of the Bst. Another ideal part for the max depth is that there is a balance between the left and right side of the tree where both sides have the same amount max depth and where the leaf nodes are on the same “level”. This is considered as a “balanced tree”.

Leaf count is the amount of nodes that neither have a left or a right child. To count the leaves you have to search through the entire tree so it is ideal if the numbers are as low as possible so less time is spent counting and searching. 


## Project conclusions and lessons learned
We separate technical issues from project related issues.

### Technical issues 
- What were the major technical challanges as you see it? What parts were the hardest and most time consuming?
The most difficult part would be when starting part 2. Looking at the skeleton code and thinking about where to start and what to do was quite challenging. It was getting easier by looking at the provided presentations and searching for explanations on the internet about both hashing and bst. After getting a better understanding of the data structures, implementation became a whole lot easier. Not to say implementing the functions from the skeleton code was easy but it became a lot more clear what you were supposed to program after looking up information about the data structures. 

- What lessons have you learned? What should you have done differently if you now were facing a similar problem.
There are a couple of things we would have done differently if we encountered a similar problem. We would probably try to look through the problem that we were going to solve and divide it based on what would be easy to implement and what would probably require more time. It would be good to start looking at the problem early and to establish a plan on what to start with and stick to it. When we were approaching the problem during this project we, more or less, went in blind and improvised when faced with an obstacle. That was not a very good approach. So it would be better to take a more methodical approach when facing similar problems. 

- How could the results be improved if you were given a bit more time to complete the task.
The results could be improved given more time by maybe consulting a teacher or other students to get feedback on the implemented data structures. It’s quite hard to see flaws in your own work so asking someone else to look at your work, they might see some problem or flaw that you completely missed. Maybe by spending some time comparing results with others and trying to explain why something went better or worse could be beneficial. 


### Project issues
- Describe how your team organized the work. How did you communicate? How often did you communicate?
During part 1 we looked and solved the problems together. That part didn’t take a very long time to finish so we decided to split the work when beginning part 2. David was going to focus on hashing and Josip was going to focus on Bst when we began on part 2. We were checking in on whatever the other was doing and tried to help each other when needed. Both considered this the best way to finish the problem. We communicated both by direct messages, when we were having lectures together and study sessions. We probably communicated, in real life and on the internet, about 3-4 times a week. 

- For each individual team member: 
 	* Describe which parts (or subtasks) of the project they were responsible for. Consider   writing the report as a separate task. Try to identify main contributors and co-contributors.
 	* Estimate hours spend each week (on average)
Part 1: Both contributed about the same.
Part 2: David was the main contributor to Hashing and co-contributed to Bst. Josip was the main contributor to Bst and co-contributed to Hashing.
Part 3: Both contributed about the same. 

Both of us spent, individually and on average, 10-15 hours a week on this project.

 - What lessons have you learned? What should you have done differently if you now were facing a similar project.
We would probably spend more time understanding what the other was doing during part 2 of the project. Maybe explaining what we were supposed to solve and what solution was implemented. Probably also give some feedback on said solution. That would make sure that everyone was on the same page consistently. 
