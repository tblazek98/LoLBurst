#!/usr/bin/env python3

import json
import pprint
import time

def initialize_champs():
    with open("champion.json") as f:
        champdata = json.load(f)
        champnames = [champdata["data"][thing]["name"] for thing in champdata["data"].keys()]

    return champnames
    #itemdata = json.load(open("item.json"))
    #itemnames = [itemdata['data'][item]['name'] for item in itemdata['data']]

class Base:
    def __init__(self):
        self.data = None

    def insert(self, data):
        pass

    def search(self, key):
        start = time.time()
        if (key):
            results = []
            key = key.lower()
            for elm in self.data:
                if elm.lower().startswith(key):
                    results.append(elm)
            end = time.time()
            print("Time elapsed Base:", end - start)
            return results
        else:
            return []

    def p(self):
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(', '.join(self.data))

class UnsortedList(Base):
    def __init__(self):
        self.data = []

    def insert(self, data):
        for elm in data:
            self.data.append(elm)

class SortedList(Base):
    def __init__(self):
        self.data = []

    def insert(self, data):
        for elm in data:
            self.data.append(elm.lower())

        self.data.sort()

    def search(self, key):
        if key:
            results = []
            key = key.lower()
            found = False
            for elm in self.data:
                if elm.lower().startswith(key):
                    found = True
                    results.append(elm)
                elif found:
                    return results
            return results
        else:
            return []

        # for i, elm in enumerate(data):
        #     if not self.data:
        #         self.data.append(elm)
        #     else:
        #         for j, elm2 in enumerate(self.data):
        #             if elm < elm2:
        #                 break
        #         self.data.insert(j, elm)

# class Node():
#     def __init__(self):
#         self.string = None
#         self.children = dict()
#
#     def insert(self, word, index=0):
#         # Gets the current letter of the word wanting to be added
#         curr = word[index]
#         # checks if that letter is already a child
#         if curr not in self.children:
#             self.children[curr] = Node()
#
#         if index + 1 == len(word):
#             #if last letter in the word, then update the string value of the Node class
#             self.children[curr].string = word
#         else:
#             #if not the last letter, you want to insert the rest of the word to the tree
#             self.children[curr].insert(word, index+1)
#
#     def get_trie(self, search, index):
#         x = [] #initialize empty list
#         for key, value in self.children.items(): #goes through all the children
#         #checks to see if on the right level of the Trie or if the key is the same as the current letter
#             if index >= len(search) or key.lower() == search[index].lower():
#                 if value.string and value.string.startswith(search): #Adds the word to the list
#                     x.append(value.string)
#                 if bool(value.children): #if there are children
#                     if index < len(search):
#                         x += value.get_trie(search, index + 1)
#                     else:
#                         x += value.get_trie(search, index)
#
#         return x
#
# class Trie():
#     def __init__(self):
#         self.root = Node()
#
#     def insert(self, data):
#         for elm in data:
#             self.root.insert(elm)
#
#     def search(self,data, index=0):
#         return self.root.get_trie(data, index)










# class Node():
#     def __init__(self, val):
#         self.value = val
#         self.children = []
#         self.word = None
#
#     def insert(self, word, index=0):
#         original = word
#         wordnew = word[index:]
#         if len(wordnew) > 0:
#             s = wordnew[0]
#             wordnew = wordnew[1:]
#             set = False
#             for char in self.children:
#                 if char.value.lower() == s.lower():
#                     char.insert(original, index+1)
#                     set = True
#                     break
#             if not set:
#                 tmp = Node(s)
#                 self.children.append(tmp)
#                 tmp.insert(original, index+1)
#
#         else:
#             self.word = original
#
#     def search(self, pref):
#         curr = pref
#         node = self
#         x = []
#         while len(curr) > 0:
#             set = False
#             for char in node.children:
#                 if char.value.lower() == curr[0].lower():
#                     node = char
#                     curr = curr[1:]
#                     set = True
#                     break
#             if not set:
#                 return x
#         if node.word:
#             x.append(node.word)
#         x = node.r_child(x)
#         return x
#
#     def r_child(self, x):
#         currlist = self.children
#         if len(currlist) > 0:
#             for child in currlist:
#                 if child.word:
#                     x.append(child.word)
#                 x = child.r_child(x)
#
#         return x
#
#
# class Trie():
#     def __init__(self):
#         self.root = Node("")
#
#     def insert(self, data):
#         for elm in data:
#             self.root.insert(elm)
#
#     def search(self,data):
#         return self.root.search(data)















# class Node():
#     def __init__(self, val):
#         self.value = val
#         self.children = {}
#         self.word = None
#         self.end = False
#
#     def insert(self, word, index=0):
#         original = word
#         wordnew = word[index:]
#         if len(wordnew) > 0:
#             s = wordnew[0]
#             wordnew = wordnew[1:]
#             set = False
#             for char in self.children.keys():
#                 if char.lower() == s.lower():
#                     if not self.children[char].end:
#                         self.children[char].word = None
#                     self.children[char].insert(original, index+1)
#                     set = True
#                     break
#             if not set:
#                 tmp = Node(s)
#                 tmp.word = original
#                 self.children[s] = tmp
#                 tmp.insert(original, index+1)
#
#         else:
#             self.word = original
#             self.end = True
#
#     def search(self, pref):
#         curr = pref
#         node = self
#         x = []
#         while len(curr) > 0:
#             set = False
#             for char in node.children.keys():
#                 if char.lower() == curr[0].lower():
#                     node = node.children[char]
#                     curr = curr[1:]
#                     set = True
#                     break
#             if not set:
#                 return x
#         if node.word:
#             x.append(node.word)
#         x = node.r_child(x)
#         return x
#
#     def r_child(self, x):
#         currlist = self.children
#         if len(currlist) > 0:
#             for child in currlist.keys():
#                 if currlist[child].word:
#                     x.append(currlist[child].word)
#                 x = currlist[child].r_child(x)
#         return x
#
#
# class Trie():
#     def __init__(self):
#         self.root = Node("")
#
#     def insert(self, data):
#         for elm in data:
#             self.root.insert(elm)
#
#     def search(self,data):
#         return list(set(self.root.search(data)))

# ^^ BEST ONE SO FAR I THINK

class Trie():
    def __init__(self):
        self.root = {"data": {}}

    def insert(self, data):
        for elm in data:
            currlist = self.root
            for char in elm:
                if char.lower() in currlist['data'].keys():
                    currlist = currlist['data'][char.lower()]
                else:
                    currlist['data'][char.lower()] = {"data": {}}
                    currlist = currlist['data'][char.lower()]

            currlist['word'] = elm

    def search(self,data):
        start = time.time()
        currlist = self.root
        #print("hello")
        #print(currlist)
        for char in data:
            if char in currlist['data'].keys():
                currlist = currlist['data'][char]
            else:
                return []
        x = self.print_dictionary(currlist)
        end = time.time()
        print("Time elapsed Trie:", end-start)
        return x

    def print_dictionary(self, currlist):
        x = []
        #print(currlist)
        if 'word' in currlist.keys():
            x.append(currlist['word'])
        for key in currlist['data'].keys():
            #print(key, currlist.keys())
            # if 'word' in currlist.keys():
            #     x.append(currlist['word'])
            x += self.print_dictionary(currlist['data'][key])

        return x



if __name__ == '__main__':
    initialize_champs()
