#!/bin/python3

import os
import sys

def contacts(queries):
    contacts = []
    count = 0
    count_list=[]
    for i in queries:
        if i[0] == "add":
            contacts.append(i[1])
        elif i[0] == "find":
            for j in contacts:
                if j.find(i[1]) != -1:
                    count+=1
            count_list.append(count)
            count = 0
    return(count_list)
queries_rows = int(input())
queries = []
for _ in range(queries_rows):
    queries.append(input().rstrip().split())

result = contacts(queries)
print(result)
