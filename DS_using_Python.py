{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "72c81ff4-1622-4a6a-b54b-a8c7c3c3ff5f",
   "metadata": {},
   "source": [
    " 1. Python basics\n",
    " 2. Data structures, Numpy\n",
    " 3. Pandas dataframes, visualization\n",
    " 4. Data science case studies in python"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45aa3c1a-73ac-4d35-95b7-62e9d6f8beac",
   "metadata": {},
   "source": [
    "# Data structures, Numpy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c8352c0e-0689-4037-be7a-934099e9923d",
   "metadata": {},
   "source": [
    "sudo pip install jupyter \n",
    "\n",
    "jupyter notebook \"to launch\"\n",
    "\n",
    "'#' heading.\n",
    "'##' subheading.\n",
    "\n",
    "from terminal\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3fcdfb0b-57d0-44e8-a9a4-f080ca2f2897",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bhargav\n"
     ]
    }
   ],
   "source": [
    "print(\"Bhargav\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8d2a751d-f023-412c-8ff5-5069c9d637d0",
   "metadata": {},
   "source": [
    "Dictionaries and sets are Containers for non-sequential data\n",
    "\n",
    "Strings, \n",
    "\n",
    "Tuples (), \n",
    "\n",
    "Lists [], \n",
    "\n",
    "Arrays, \n",
    "\n",
    "Dictionary - key-value pairs {}, \n",
    "\n",
    "Sets  sequences of unordered collection of unique data, \n",
    "\n",
    "Range --- range()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "caf3ab19-1eaa-4548-917d-9d11dec0d29a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "learning\n"
     ]
    }
   ],
   "source": [
    "strSample = 'learning' \n",
    " float x = 25.678   #string\n",
    "\n",
    "print(strSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9813df6a-266d-4cc7-b3b9-5d84a3c771ab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "listNumbers = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]  # list with numbers,   multi data type, mutable.\n",
    "print(listNumbers)                               # having Duplicate values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e422c04a-667e-4414-b6de-9ca09a7214f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 'bhargav', 2, 'kumar', 3]\n"
     ]
    }
   ],
   "source": [
    "listSample = [ 1, 'bhargav', 2, 'kumar', 3]\n",
    "print(listSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "de20b1ea-3e2b-435b-a5e2-3da58b586e2a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "array('i', [1, 2, 3, 4])\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "from array import *\n",
    "\n",
    "arrSample = array('i', [1, 2, 3, 4])\n",
    "print(arrSample)\n",
    "\n",
    "for x in arrSample: print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e79efb47-e8f9-4149-a112-8235d4e6ffcd",
   "metadata": {},
   "outputs": [],
   "source": [
    "tupSample = (1, 2, 3, 4, 'py')         # once created not changed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "0964d862-5a22-456f-8a63-0a35ca762c45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 4, 5, 'bhargav')\n"
     ]
    }
   ],
   "source": [
    "tupSample = 1, 2, 3, 4, 5, 'bhargav'\n",
    "print(tupSample)     #tuple packing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6109142c-34c0-48d1-a77f-5d5e3d2b2d3d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{ '1': 'first', '2': 'two', '3': 'three' }"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dictSample = { 1:'first', 2:'two', 3:'three'}\n",
    "dictSample\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "48bb9605-2428-4960-b049-23fdb463eb05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1: 'first', 2: 'two', 3: 'three'}"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict_list = dict([(1,'first'), (2,'two'), (3,'three')])\n",
    "\n",
    "dict_list                                  \n",
    "                  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "6f270934-3b27-498e-bd0a-d788c6d68000",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{24, 25, 31, 65, 'data', 'example'}"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "setSample = {'example', 24, 31, 25, 'data', 65, 65}  # set cannot be element of set,list\n",
    "setSample"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c262d8a4-a80e-4b90-940f-4e48a5eabcde",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "range(1, 12, 4)\n",
      "1\n",
      "5\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "rangeSample=range(1,12,4)        #range(start, stop, step).          used for looping\n",
    "print(rangeSample)\n",
    "\n",
    "for x in rangeSample: print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0bcdcb3f-123c-4f87-bed2-95f0e9129c7a",
   "metadata": {},
   "source": [
    "# Indexing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "561a5ee4-f39e-479e-ab05-63f450617ef5",
   "metadata": {},
   "outputs": [],
   "source": [
    "## String Indexing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5db7bb68-227c-4da5-8f78-366e10b313bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample = 'Bhargav'\n",
    "strSample.index('r')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "7c103c4f-475d-46aa-bbed-31146f1877b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample.index('gav')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "f717046f-0513-475a-aeff-1128c30eeabe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'v'"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample[6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "9fb72b28-4fbb-42fd-961f-4745cd02957f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'g'"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample[-3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "2fcf377e-2075-468f-b7cd-f0add6e374f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'B'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample[-7]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "20b42ebb-e085-494b-880a-a290d79abfbc",
   "metadata": {},
   "source": [
    "## List indexing\n",
    "## list_name.index(element.start,end)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "f8de0578-ed3f-446f-956d-087b5949aa6b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 'bhargav', 6]"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listSample = [1, 2, 3, 'bhargav', 6]\n",
    "listSample"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "cc139850-ecda-4ffa-b4c0-9bc22ab40736",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'listSample' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[9], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mlistSample\u001b[49m\u001b[38;5;241m.\u001b[39mindex(\u001b[38;5;241m1\u001b[39m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'listSample' is not defined"
     ]
    }
   ],
   "source": [
    "listSample.index(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "74643638-c450-473d-8484-d71a9d403073",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'bhargav'"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listSample[3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "9d5d5686-6929-43a0-b868-22c9c1a7a6ba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listSample[-1]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6f7c8cfa-a104-46f6-9347-8753266eaf13",
   "metadata": {},
   "source": [
    "## Array Indexing\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6bcd77c-2eb4-45e4-b366-2d28d9128477",
   "metadata": {},
   "outputs": [],
   "source": [
    "from array import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "90653b57-82f4-49f5-a5dc-3bd2897c2b02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "arrSample = array('i',[1,2,3,4,5])\n",
    "for x in arrSample: print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "2b3b57b3-b2bc-48f0-b29b-0fa9ba70014b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arrSample[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "12fbc2b5-d373-4a1b-b596-818ae2035451",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arrSample.index(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "feb94534-07d3-48f7-876a-7035b1686736",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arrSample[-2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b6ec9ba-12d6-4876-8478-dad4756cfff1",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Tuple indexing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "b32f1837-c68a-4890-8d4e-5298a4884efa",
   "metadata": {},
   "outputs": [],
   "source": [
    "tupSample1 = (1,2,3,4,5,6,'py','bhargav')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "e9200565-d831-447f-8894-0dfb8fe00923",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tupSample1.index(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "a791d657-3f20-4f73-aff1-b032f178b2d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tupSample1.index('bhargav')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "8db95498-c4fa-4c60-82f3-0ef346ffe706",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tupSample1.index('py')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "a00a3cf7-4e17-45d6-97d9-4f6a8a660644",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'bhargav'"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tupSample[5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a194e7dd-c448-4a5b-af75-ee5943e8f229",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Set Indexing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f95f2ec-42cf-4227-b080-82590709156e",
   "metadata": {},
   "outputs": [],
   "source": [
    "setSample = {'example', 24, 56, 48, 'data'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "c741a57a-fd0f-4697-946f-77f92eb8fbd5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'data'"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "setSample[4]        #set obj doesnt support indexing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "a82958e3-a8ff-43d5-a70f-14923302af31",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "setSample.index(24)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "98116127-fd86-44ca-ab7d-4b750487eb35",
   "metadata": {},
   "source": [
    "# Dictionary Indexing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "7c583dc3-936b-49c6-af85-129033a0111b",
   "metadata": {},
   "outputs": [],
   "source": [
    "dictSample1 = {1:'first', 'second':2, 3:3, 'four':'4'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "e8d7546c-d661-4ac0-9e0a-065d74ca06bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dictSample1['second']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "aaac733a-89e5-488c-9204-45308d3d3d3c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'first'"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dictSample1[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f60764ca-6508-457b-a787-9181c2e61867",
   "metadata": {},
   "outputs": [],
   "source": [
    "#range Indexing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "89f3b97f-0291-478d-93d2-e49476b63905",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "5\n",
      "9\n",
      "13\n"
     ]
    }
   ],
   "source": [
    "rangeSample1 = range(1, 15, 4)\n",
    "for x in rangeSample1: print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "ae26f364-3759-4222-a618-4405f4db42a0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rangeSample1.index(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "9096fd8a-bf61-4f06-a171-2887f5e8a0d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rangeSample1.index(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "11f1a1ec-d419-4762-9827-16e5775c961f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rangeSample1[3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "4230d304-6689-48fc-b7c9-8b6861ace2cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rangeSample1[2]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26b97dee-5412-412b-a579-fbed3562e617",
   "metadata": {},
   "source": [
    "## Sequence Data Operatipns: Slicing\n",
    "### slice(stop), slice(start, stop, step)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "401fdcb1-f82f-4e8b-a2ed-178405ec87cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bhargav\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'ra'"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(strSample)\n",
    "strSample[slice(3,6,2)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "9cbb10c6-8e3a-4a60-96a9-e3579a1424a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Bhargav'"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample[:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "99dda962-904f-452b-a172-138f2cec1871",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'rgav'"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample[3:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "341f2beb-65f6-458d-abb9-ff8e96f18154",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Bhargav'"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample[:7]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "daa0193f-c513-490c-a413-f03250955ac2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hra'"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample[1:7:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "9c0bf666-57a3-4304-8d0e-6f4b6b5275c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'argav'"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample[-5:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "3e516543-37bb-4dac-b44e-2646303ea0d0",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unhashable type: 'slice'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[92], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mdictSample\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;241;43m1\u001b[39;49m\u001b[43m:\u001b[49m\u001b[38;5;241;43m3\u001b[39;49m\u001b[43m]\u001b[49m\n",
      "\u001b[0;31mTypeError\u001b[0m: unhashable type: 'slice'"
     ]
    }
   ],
   "source": [
    "dictSample[1:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "11abd719-02ce-4638-a007-42a70b5483cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('example', 24, 31, 25, 'data', 65)"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "setSample"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "f256104a-2e98-4117-bd48-25abceb67c7c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(24, 31, 25, 'data')"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "setSample[1:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "3ff54567-f097-4985-9627-26303d70b012",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "for x in arrSample: print(x)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "3acba781-f3b5-48be-8957-219148a35957",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array('i', [2, 3, 4])"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arrSample[1:4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "db6263c5-0493-4671-83c2-133053b08216",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array('i', [2, 3, 4, 5])"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arrSample[1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "1924eeaa-3742-43c6-943c-0e591bfd190b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array('i', [2, 3, 4])"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arrSample[1:-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "b5548a98-b030-4962-971b-1d8c77e92465",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array('i', [1, 2, 3, 4, 5])"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arrSample[0:]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5f3e5a15-89bb-46b2-975b-9c276968ee5e",
   "metadata": {},
   "source": [
    "## Concatenation\n",
    "#### ,  +    +="
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "03eeaccb-bf1b-4803-9dbb-7314ca818a4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bhargav  python\n"
     ]
    }
   ],
   "source": [
    "print(strSample+' ','python')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "2f972bca-42bb-4ce1-9822-a7f0c7361288",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Bhargav ', 'Python')\n"
     ]
    }
   ],
   "source": [
    "newStr = strSample+' ','Python'\n",
    "print(newStr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "9ea11f12-50cf-4a46-a682-430bb4ca9831",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 'bhargav', 6]\n"
     ]
    }
   ],
   "source": [
    "print(listSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "c33cb25e-47bd-43f3-9e87-f12b65af6181",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 'bhargav', 6, 7, 'py']"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listSample + [7,'py']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2ef0da51-30b1-4ea9-847e-ccb8fde4c18d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "array('i', [1, 2, 3, 4, 3])\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "can only append array (not \"list\") to array",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[14], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28mprint\u001b[39m(arrSample)\n\u001b[0;32m----> 2\u001b[0m \u001b[43marrSample\u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43m[\u001b[49m\u001b[38;5;241;43m6\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m7\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m8\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m9\u001b[39;49m\u001b[43m]\u001b[49m\n",
      "\u001b[0;31mTypeError\u001b[0m: can only append array (not \"list\") to array"
     ]
    }
   ],
   "source": [
    "print(arrSample)\n",
    "arrSample+[6, 7, 8, 9]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "5f568f85-1def-447d-be2b-a8baa99d5f6a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arrSample+array('i',[6, 7, 8, 9])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "f2f9303c-9dad-4b5c-9780-99f9b4ca0be5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('example', 24, 31, 25, 'data', 65)\n"
     ]
    }
   ],
   "source": [
    "print(setSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "8958c2e8-1008-4e92-9c46-e26ca4331065",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 4, 5, 'bhargav', 'th', 'on', 'th', 'on', 'th', 'on')\n"
     ]
    }
   ],
   "source": [
    "print(tupSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "69dfdf86-913c-4fe1-9af0-9c37f82f266c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 4, 5, 'bhargav', 'th', 'on', 'th', 'on', 'th', 'on', '90', 'the')\n"
     ]
    }
   ],
   "source": [
    "tupSample+=('90', 'the')\n",
    "print(tupSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "id": "cf75dbe8-ce63-446f-8c54-ca6757f0e240",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(('example', 24, 31, 25, 'data', 65), 24)\n",
      "((('example', 24, 31, 25, 'data', 65), 24), 24)\n"
     ]
    }
   ],
   "source": [
    "print(setSample)\n",
    "setSample=setSample, 24\n",
    "print(setSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53762348-8c53-40c3-ac51-19a48b776b0e",
   "metadata": {},
   "outputs": [],
   "source": [
    " ## Sequence data operations: Multiplication\n",
    "#### syntax: object*integer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "e7d9f45f-e760-4ce4-b29d-c0867e4c20bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "BhargavBhargavBhargavBhargavBhargavBhargavBhargavBhargavBhargav\n"
     ]
    }
   ],
   "source": [
    "strSample*=3\n",
    "print(strSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "350f2e93-2ef4-4969-afab-04b3cf96d320",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 'bhargav', 6, 1, 2, 3, 'bhargav', 6]"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listSample*2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "d7c9376d-bbb2-42d5-8a30-7cb8ee94bfe1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listSample[1]*2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "3043258d-6122-414d-b821-cf724e653049",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'bhargavbhargav'"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listSample[3]*2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "fee7b580-b018-4a2d-838b-bef10de874fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 4, 5, 'bhargav', 'th', 'on', 'th', 'on', 'th', 'on', '90', 'the')\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "(3, 4, 3, 4)"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(tupSample)\n",
    "tupSample[2:4]*2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "a4540c26-d30c-4e4c-8127-168216e9f9f9",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for *: 'range' and 'int'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[128], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43mrangeSample\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m2\u001b[39;49m\n",
      "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for *: 'range' and 'int'"
     ]
    }
   ],
   "source": [
    "rangeSample*2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ad788e2d-e44c-4754-9760-17ce689f4c3d",
   "metadata": {},
   "source": [
    "## General sequence data methods\n",
    "\n",
    "### String Methods"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "01537dfc-7d21-4c80-8eb5-1d3aa850793e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "learning is fun !\n"
     ]
    }
   ],
   "source": [
    "strSample2 = 'learning is fun !'\n",
    "print(strSample2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "a3e2f3e8-1e40-4361-bedb-908f79fcff58",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Learning is fun !'"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample2.capitalize()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "58d53d03-d895-433b-90c8-82cc3c767191",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'learning is fun !'"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample2.casefold()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "bf24269c-c0a3-469c-8d9b-83189386cf1f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Learning Is Fun !'"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample2.title()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "id": "1c5e1be1-1932-4262-9424-32c386ab3746",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LEARNING IS FUN !\n"
     ]
    }
   ],
   "source": [
    "strSample2 = strSample2.swapcase()\n",
    "print(strSample2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "id": "ed8b6deb-61c3-4f30-b3a1-aabfe2816ea5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'learning is fun !'"
      ]
     },
     "execution_count": 149,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample2.swapcase()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "id": "673e7f7b-32fa-452e-a3bd-cd8ceb10aee4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 145,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample2.find('N')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "id": "15f657b8-6159-48b7-b8fe-83609d9204a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample2.count('N')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "25411575-52ef-4da3-8946-ae0c609abafc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'learning is joyful !'"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample2.replace('fun','joyful')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "864bfad5-f082-4394-a110-613c90c516d2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "strSample2.isalnum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "50b3c719-e837-42c0-8c1f-f9ddbf78f837",
   "metadata": {},
   "outputs": [],
   "source": [
    "name1 = 'GITAA'\n",
    "name2 = 'Pvt'\n",
    "name3 = 'Ltd'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "id": "e6b0bc74-fb78-4070-a9f8-4ffa8bb6762c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "GITAA Pvt. Ltd.\n"
     ]
    }
   ],
   "source": [
    "name = '{} {}. {}.'.format(name1,name2,name3)\n",
    "print(name)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4f3cd5f7-dba1-4186-a7bc-9ce08e109c41",
   "metadata": {},
   "source": [
    "### The below code will show all the functions that we can use for the particular variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "386128f4-7284-412d-9ee4-45c202597887",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']\n"
     ]
    }
   ],
   "source": [
    "print(dir(name))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "id": "d8438873-1181-4723-8871-1e3493a15555",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on class str in module builtins:\n",
      "\n",
      "class str(object)\n",
      " |  str(object='') -> str\n",
      " |  str(bytes_or_buffer[, encoding[, errors]]) -> str\n",
      " |  \n",
      " |  Create a new string object from the given object. If encoding or\n",
      " |  errors is specified, then the object must expose a data buffer\n",
      " |  that will be decoded using the given encoding and error handler.\n",
      " |  Otherwise, returns the result of object.__str__() (if defined)\n",
      " |  or repr(object).\n",
      " |  encoding defaults to sys.getdefaultencoding().\n",
      " |  errors defaults to 'strict'.\n",
      " |  \n",
      " |  Methods defined here:\n",
      " |  \n",
      " |  __add__(self, value, /)\n",
      " |      Return self+value.\n",
      " |  \n",
      " |  __contains__(self, key, /)\n",
      " |      Return key in self.\n",
      " |  \n",
      " |  __eq__(self, value, /)\n",
      " |      Return self==value.\n",
      " |  \n",
      " |  __format__(self, format_spec, /)\n",
      " |      Return a formatted version of the string as described by format_spec.\n",
      " |  \n",
      " |  __ge__(self, value, /)\n",
      " |      Return self>=value.\n",
      " |  \n",
      " |  __getattribute__(self, name, /)\n",
      " |      Return getattr(self, name).\n",
      " |  \n",
      " |  __getitem__(self, key, /)\n",
      " |      Return self[key].\n",
      " |  \n",
      " |  __getnewargs__(...)\n",
      " |  \n",
      " |  __gt__(self, value, /)\n",
      " |      Return self>value.\n",
      " |  \n",
      " |  __hash__(self, /)\n",
      " |      Return hash(self).\n",
      " |  \n",
      " |  __iter__(self, /)\n",
      " |      Implement iter(self).\n",
      " |  \n",
      " |  __le__(self, value, /)\n",
      " |      Return self<=value.\n",
      " |  \n",
      " |  __len__(self, /)\n",
      " |      Return len(self).\n",
      " |  \n",
      " |  __lt__(self, value, /)\n",
      " |      Return self<value.\n",
      " |  \n",
      " |  __mod__(self, value, /)\n",
      " |      Return self%value.\n",
      " |  \n",
      " |  __mul__(self, value, /)\n",
      " |      Return self*value.\n",
      " |  \n",
      " |  __ne__(self, value, /)\n",
      " |      Return self!=value.\n",
      " |  \n",
      " |  __repr__(self, /)\n",
      " |      Return repr(self).\n",
      " |  \n",
      " |  __rmod__(self, value, /)\n",
      " |      Return value%self.\n",
      " |  \n",
      " |  __rmul__(self, value, /)\n",
      " |      Return value*self.\n",
      " |  \n",
      " |  __sizeof__(self, /)\n",
      " |      Return the size of the string in memory, in bytes.\n",
      " |  \n",
      " |  __str__(self, /)\n",
      " |      Return str(self).\n",
      " |  \n",
      " |  capitalize(self, /)\n",
      " |      Return a capitalized version of the string.\n",
      " |      \n",
      " |      More specifically, make the first character have upper case and the rest lower\n",
      " |      case.\n",
      " |  \n",
      " |  casefold(self, /)\n",
      " |      Return a version of the string suitable for caseless comparisons.\n",
      " |  \n",
      " |  center(self, width, fillchar=' ', /)\n",
      " |      Return a centered string of length width.\n",
      " |      \n",
      " |      Padding is done using the specified fill character (default is a space).\n",
      " |  \n",
      " |  count(...)\n",
      " |      S.count(sub[, start[, end]]) -> int\n",
      " |      \n",
      " |      Return the number of non-overlapping occurrences of substring sub in\n",
      " |      string S[start:end].  Optional arguments start and end are\n",
      " |      interpreted as in slice notation.\n",
      " |  \n",
      " |  encode(self, /, encoding='utf-8', errors='strict')\n",
      " |      Encode the string using the codec registered for encoding.\n",
      " |      \n",
      " |      encoding\n",
      " |        The encoding in which to encode the string.\n",
      " |      errors\n",
      " |        The error handling scheme to use for encoding errors.\n",
      " |        The default is 'strict' meaning that encoding errors raise a\n",
      " |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and\n",
      " |        'xmlcharrefreplace' as well as any other name registered with\n",
      " |        codecs.register_error that can handle UnicodeEncodeErrors.\n",
      " |  \n",
      " |  endswith(...)\n",
      " |      S.endswith(suffix[, start[, end]]) -> bool\n",
      " |      \n",
      " |      Return True if S ends with the specified suffix, False otherwise.\n",
      " |      With optional start, test S beginning at that position.\n",
      " |      With optional end, stop comparing S at that position.\n",
      " |      suffix can also be a tuple of strings to try.\n",
      " |  \n",
      " |  expandtabs(self, /, tabsize=8)\n",
      " |      Return a copy where all tab characters are expanded using spaces.\n",
      " |      \n",
      " |      If tabsize is not given, a tab size of 8 characters is assumed.\n",
      " |  \n",
      " |  find(...)\n",
      " |      S.find(sub[, start[, end]]) -> int\n",
      " |      \n",
      " |      Return the lowest index in S where substring sub is found,\n",
      " |      such that sub is contained within S[start:end].  Optional\n",
      " |      arguments start and end are interpreted as in slice notation.\n",
      " |      \n",
      " |      Return -1 on failure.\n",
      " |  \n",
      " |  format(...)\n",
      " |      S.format(*args, **kwargs) -> str\n",
      " |      \n",
      " |      Return a formatted version of S, using substitutions from args and kwargs.\n",
      " |      The substitutions are identified by braces ('{' and '}').\n",
      " |  \n",
      " |  format_map(...)\n",
      " |      S.format_map(mapping) -> str\n",
      " |      \n",
      " |      Return a formatted version of S, using substitutions from mapping.\n",
      " |      The substitutions are identified by braces ('{' and '}').\n",
      " |  \n",
      " |  index(...)\n",
      " |      S.index(sub[, start[, end]]) -> int\n",
      " |      \n",
      " |      Return the lowest index in S where substring sub is found,\n",
      " |      such that sub is contained within S[start:end].  Optional\n",
      " |      arguments start and end are interpreted as in slice notation.\n",
      " |      \n",
      " |      Raises ValueError when the substring is not found.\n",
      " |  \n",
      " |  isalnum(self, /)\n",
      " |      Return True if the string is an alpha-numeric string, False otherwise.\n",
      " |      \n",
      " |      A string is alpha-numeric if all characters in the string are alpha-numeric and\n",
      " |      there is at least one character in the string.\n",
      " |  \n",
      " |  isalpha(self, /)\n",
      " |      Return True if the string is an alphabetic string, False otherwise.\n",
      " |      \n",
      " |      A string is alphabetic if all characters in the string are alphabetic and there\n",
      " |      is at least one character in the string.\n",
      " |  \n",
      " |  isascii(self, /)\n",
      " |      Return True if all characters in the string are ASCII, False otherwise.\n",
      " |      \n",
      " |      ASCII characters have code points in the range U+0000-U+007F.\n",
      " |      Empty string is ASCII too.\n",
      " |  \n",
      " |  isdecimal(self, /)\n",
      " |      Return True if the string is a decimal string, False otherwise.\n",
      " |      \n",
      " |      A string is a decimal string if all characters in the string are decimal and\n",
      " |      there is at least one character in the string.\n",
      " |  \n",
      " |  isdigit(self, /)\n",
      " |      Return True if the string is a digit string, False otherwise.\n",
      " |      \n",
      " |      A string is a digit string if all characters in the string are digits and there\n",
      " |      is at least one character in the string.\n",
      " |  \n",
      " |  isidentifier(self, /)\n",
      " |      Return True if the string is a valid Python identifier, False otherwise.\n",
      " |      \n",
      " |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,\n",
      " |      such as \"def\" or \"class\".\n",
      " |  \n",
      " |  islower(self, /)\n",
      " |      Return True if the string is a lowercase string, False otherwise.\n",
      " |      \n",
      " |      A string is lowercase if all cased characters in the string are lowercase and\n",
      " |      there is at least one cased character in the string.\n",
      " |  \n",
      " |  isnumeric(self, /)\n",
      " |      Return True if the string is a numeric string, False otherwise.\n",
      " |      \n",
      " |      A string is numeric if all characters in the string are numeric and there is at\n",
      " |      least one character in the string.\n",
      " |  \n",
      " |  isprintable(self, /)\n",
      " |      Return True if the string is printable, False otherwise.\n",
      " |      \n",
      " |      A string is printable if all of its characters are considered printable in\n",
      " |      repr() or if it is empty.\n",
      " |  \n",
      " |  isspace(self, /)\n",
      " |      Return True if the string is a whitespace string, False otherwise.\n",
      " |      \n",
      " |      A string is whitespace if all characters in the string are whitespace and there\n",
      " |      is at least one character in the string.\n",
      " |  \n",
      " |  istitle(self, /)\n",
      " |      Return True if the string is a title-cased string, False otherwise.\n",
      " |      \n",
      " |      In a title-cased string, upper- and title-case characters may only\n",
      " |      follow uncased characters and lowercase characters only cased ones.\n",
      " |  \n",
      " |  isupper(self, /)\n",
      " |      Return True if the string is an uppercase string, False otherwise.\n",
      " |      \n",
      " |      A string is uppercase if all cased characters in the string are uppercase and\n",
      " |      there is at least one cased character in the string.\n",
      " |  \n",
      " |  join(self, iterable, /)\n",
      " |      Concatenate any number of strings.\n",
      " |      \n",
      " |      The string whose method is called is inserted in between each given string.\n",
      " |      The result is returned as a new string.\n",
      " |      \n",
      " |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'\n",
      " |  \n",
      " |  ljust(self, width, fillchar=' ', /)\n",
      " |      Return a left-justified string of length width.\n",
      " |      \n",
      " |      Padding is done using the specified fill character (default is a space).\n",
      " |  \n",
      " |  lower(self, /)\n",
      " |      Return a copy of the string converted to lowercase.\n",
      " |  \n",
      " |  lstrip(self, chars=None, /)\n",
      " |      Return a copy of the string with leading whitespace removed.\n",
      " |      \n",
      " |      If chars is given and not None, remove characters in chars instead.\n",
      " |  \n",
      " |  partition(self, sep, /)\n",
      " |      Partition the string into three parts using the given separator.\n",
      " |      \n",
      " |      This will search for the separator in the string.  If the separator is found,\n",
      " |      returns a 3-tuple containing the part before the separator, the separator\n",
      " |      itself, and the part after it.\n",
      " |      \n",
      " |      If the separator is not found, returns a 3-tuple containing the original string\n",
      " |      and two empty strings.\n",
      " |  \n",
      " |  removeprefix(self, prefix, /)\n",
      " |      Return a str with the given prefix string removed if present.\n",
      " |      \n",
      " |      If the string starts with the prefix string, return string[len(prefix):].\n",
      " |      Otherwise, return a copy of the original string.\n",
      " |  \n",
      " |  removesuffix(self, suffix, /)\n",
      " |      Return a str with the given suffix string removed if present.\n",
      " |      \n",
      " |      If the string ends with the suffix string and that suffix is not empty,\n",
      " |      return string[:-len(suffix)]. Otherwise, return a copy of the original\n",
      " |      string.\n",
      " |  \n",
      " |  replace(self, old, new, count=-1, /)\n",
      " |      Return a copy with all occurrences of substring old replaced by new.\n",
      " |      \n",
      " |        count\n",
      " |          Maximum number of occurrences to replace.\n",
      " |          -1 (the default value) means replace all occurrences.\n",
      " |      \n",
      " |      If the optional argument count is given, only the first count occurrences are\n",
      " |      replaced.\n",
      " |  \n",
      " |  rfind(...)\n",
      " |      S.rfind(sub[, start[, end]]) -> int\n",
      " |      \n",
      " |      Return the highest index in S where substring sub is found,\n",
      " |      such that sub is contained within S[start:end].  Optional\n",
      " |      arguments start and end are interpreted as in slice notation.\n",
      " |      \n",
      " |      Return -1 on failure.\n",
      " |  \n",
      " |  rindex(...)\n",
      " |      S.rindex(sub[, start[, end]]) -> int\n",
      " |      \n",
      " |      Return the highest index in S where substring sub is found,\n",
      " |      such that sub is contained within S[start:end].  Optional\n",
      " |      arguments start and end are interpreted as in slice notation.\n",
      " |      \n",
      " |      Raises ValueError when the substring is not found.\n",
      " |  \n",
      " |  rjust(self, width, fillchar=' ', /)\n",
      " |      Return a right-justified string of length width.\n",
      " |      \n",
      " |      Padding is done using the specified fill character (default is a space).\n",
      " |  \n",
      " |  rpartition(self, sep, /)\n",
      " |      Partition the string into three parts using the given separator.\n",
      " |      \n",
      " |      This will search for the separator in the string, starting at the end. If\n",
      " |      the separator is found, returns a 3-tuple containing the part before the\n",
      " |      separator, the separator itself, and the part after it.\n",
      " |      \n",
      " |      If the separator is not found, returns a 3-tuple containing two empty strings\n",
      " |      and the original string.\n",
      " |  \n",
      " |  rsplit(self, /, sep=None, maxsplit=-1)\n",
      " |      Return a list of the words in the string, using sep as the delimiter string.\n",
      " |      \n",
      " |        sep\n",
      " |          The delimiter according which to split the string.\n",
      " |          None (the default value) means split according to any whitespace,\n",
      " |          and discard empty strings from the result.\n",
      " |        maxsplit\n",
      " |          Maximum number of splits to do.\n",
      " |          -1 (the default value) means no limit.\n",
      " |      \n",
      " |      Splits are done starting at the end of the string and working to the front.\n",
      " |  \n",
      " |  rstrip(self, chars=None, /)\n",
      " |      Return a copy of the string with trailing whitespace removed.\n",
      " |      \n",
      " |      If chars is given and not None, remove characters in chars instead.\n",
      " |  \n",
      " |  split(self, /, sep=None, maxsplit=-1)\n",
      " |      Return a list of the words in the string, using sep as the delimiter string.\n",
      " |      \n",
      " |      sep\n",
      " |        The delimiter according which to split the string.\n",
      " |        None (the default value) means split according to any whitespace,\n",
      " |        and discard empty strings from the result.\n",
      " |      maxsplit\n",
      " |        Maximum number of splits to do.\n",
      " |        -1 (the default value) means no limit.\n",
      " |  \n",
      " |  splitlines(self, /, keepends=False)\n",
      " |      Return a list of the lines in the string, breaking at line boundaries.\n",
      " |      \n",
      " |      Line breaks are not included in the resulting list unless keepends is given and\n",
      " |      true.\n",
      " |  \n",
      " |  startswith(...)\n",
      " |      S.startswith(prefix[, start[, end]]) -> bool\n",
      " |      \n",
      " |      Return True if S starts with the specified prefix, False otherwise.\n",
      " |      With optional start, test S beginning at that position.\n",
      " |      With optional end, stop comparing S at that position.\n",
      " |      prefix can also be a tuple of strings to try.\n",
      " |  \n",
      " |  strip(self, chars=None, /)\n",
      " |      Return a copy of the string with leading and trailing whitespace removed.\n",
      " |      \n",
      " |      If chars is given and not None, remove characters in chars instead.\n",
      " |  \n",
      " |  swapcase(self, /)\n",
      " |      Convert uppercase characters to lowercase and lowercase characters to uppercase.\n",
      " |  \n",
      " |  title(self, /)\n",
      " |      Return a version of the string where each word is titlecased.\n",
      " |      \n",
      " |      More specifically, words start with uppercased characters and all remaining\n",
      " |      cased characters have lower case.\n",
      " |  \n",
      " |  translate(self, table, /)\n",
      " |      Replace each character in the string using the given translation table.\n",
      " |      \n",
      " |        table\n",
      " |          Translation table, which must be a mapping of Unicode ordinals to\n",
      " |          Unicode ordinals, strings, or None.\n",
      " |      \n",
      " |      The table must implement lookup/indexing via __getitem__, for instance a\n",
      " |      dictionary or list.  If this operation raises LookupError, the character is\n",
      " |      left untouched.  Characters mapped to None are deleted.\n",
      " |  \n",
      " |  upper(self, /)\n",
      " |      Return a copy of the string converted to uppercase.\n",
      " |  \n",
      " |  zfill(self, width, /)\n",
      " |      Pad a numeric string with zeros on the left, to fill a field of the given width.\n",
      " |      \n",
      " |      The string is never truncated.\n",
      " |  \n",
      " |  ----------------------------------------------------------------------\n",
      " |  Static methods defined here:\n",
      " |  \n",
      " |  __new__(*args, **kwargs) from builtins.type\n",
      " |      Create and return a new object.  See help(type) for accurate signature.\n",
      " |  \n",
      " |  maketrans(...)\n",
      " |      Return a translation table usable for str.translate().\n",
      " |      \n",
      " |      If there is only one argument, it must be a dictionary mapping Unicode\n",
      " |      ordinals (integers) or characters to Unicode ordinals, strings or None.\n",
      " |      Character keys will be then converted to ordinals.\n",
      " |      If there are two arguments, they must be strings of equal length, and\n",
      " |      in the resulting dictionary, each character in x will be mapped to the\n",
      " |      character at the same position in y. If there is a third argument, it\n",
      " |      must be a string, whose characters will be mapped to None in the result.\n",
      "\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(help(str))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "id": "a0850d62-4c13-45d2-9166-b6befe82ebca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on method_descriptor:\n",
      "\n",
      "count(...)\n",
      "    S.count(sub[, start[, end]]) -> int\n",
      "    \n",
      "    Return the number of non-overlapping occurrences of substring sub in\n",
      "    string S[start:end].  Optional arguments start and end are\n",
      "    interpreted as in slice notation.\n",
      "\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(help(str.count))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "878eff0f-74d2-4fca-9dd3-cc71a54b6ebd",
   "metadata": {},
   "source": [
    "## sequence datatype object initializations"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d55d9c1b-b8b8-4dc3-9858-28b8850ae488",
   "metadata": {},
   "source": [
    "### len(obj) returns number of elements in the object\n",
    "##### accepted obj types are string, list, array, tuple, dictionary, set, range"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "2c216bf9-93fc-4daf-ac70-eb9432f48517",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No. of elements in the object :\n",
      "string = 63, list=5, array=5, tuple=14, dictionary=3, set=2, range=3\n"
     ]
    }
   ],
   "source": [
    "print(\"No. of elements in the object :\")\n",
    "print(\"string = {}, list={}, array={}, tuple={}, dictionary={}, set={}, \\\n",
    "range={}\".format(len(strSample), len(listSample), len(arrSample), \\\n",
    "                 len(tupSample), len(dictSample), len(setSample), len(rangeSample)))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "de5a9e2e-9b9c-45a3-b494-e6d558e48d69",
   "metadata": {},
   "source": [
    "## The clear() method removes all items from the object\n",
    "##### Supported sequence data: list, dictionary, set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "id": "330563bf-98ca-49bf-9d14-20bd367a1e70",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "listSample.clear()\n",
    "print(listSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "id": "fa542e1b-d03d-4c13-abd9-cfb0db305124",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{}\n"
     ]
    }
   ],
   "source": [
    "dictSample.clear()\n",
    "print(dictSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "456a1cb1-49a5-43e9-a7e2-0c2f216cde76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "set()\n"
     ]
    }
   ],
   "source": [
    "setSample.clear()\n",
    "print(setSample)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "92a486dd-180f-4502-90ac-9a590bf984ac",
   "metadata": {},
   "source": [
    "## append() Adds an element at the end of the object\n",
    "##### supported datatypes array, list, set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cceefda0-a590-408a-948d-f0aa4fc3bce3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "array('i', [1, 2, 3, 4, 3])\n"
     ]
    }
   ],
   "source": [
    "arrSample.append(3)\n",
    "print(arrSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a5e86ebd-98c3-4053-a811-0acfa63e77f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 'bhargav', 2, 'kumar', 3]\n"
     ]
    }
   ],
   "source": [
    "print(listSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "783b5f8b-2d23-46c0-b1ae-a27dac6cfa29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 'bhargav', 2, 'kumar', 3, 'hello']\n"
     ]
    }
   ],
   "source": [
    "listSample.append('hello')\n",
    "print(listSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4d98016f-ed26-495d-acd4-c83f20baa3b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{226}\n"
     ]
    }
   ],
   "source": [
    "#setSample.append(20)    # set has no attribute append\n",
    "setSample.add(226)      # add() takes single parameter\n",
    "print(setSample)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9ecb69b4-0fdd-4213-bbe9-9f5af07af4b2",
   "metadata": {},
   "source": [
    "## update() function in set adds elements from a set(passed as an argument) to\n",
    "\n",
    "#### -- this method takes only single argument.\n",
    "#### --  the single argument can be a set, list, tuples or a dictionary\n",
    "#### -- It automatically converts into a set and adds to the set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ae8d65cc-e40c-42fd-bd26-39b1acd070bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{226, 10, 5}\n"
     ]
    }
   ],
   "source": [
    "setSample.update([5, 10])\n",
    "print(setSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d930f7bf-e962-4a54-ad95-b9200bb7097f",
   "metadata": {},
   "outputs": [],
   "source": [
    "###Dictionary methods"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "26a02b0b-7287-419e-8326-a945ee446767",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 'first', 2: 'two', 3: 'three'}\n"
     ]
    }
   ],
   "source": [
    "print(dictSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c709ce24-0e73-4b6e-88f0-9d46fd5c6e6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 'first', 2: 'two', 3: 'three', 'five': 5}\n"
     ]
    }
   ],
   "source": [
    "dictSample[\"five\"] = 5\n",
    "print(dictSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "812cf6c9-789c-4c28-a4b8-aaa48e68c24c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 'first', 2: 'two', 3: 'three', 'five': 5, 'six': 6}\n"
     ]
    }
   ],
   "source": [
    "dictSample.update(six = 6)\n",
    "print(dictSample).          # overwriting existing keys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b5164e01-a379-4388-8053-fb9df97694a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 'five', 'six']"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(dictSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "7051a37b-536e-4514-b034-e2798c610de8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(dictSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "1f3e7bae-6441-4431-a0cb-2c9e66319296",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dictSample.get(\"five\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "93cb3814-8038-402b-b2f7-570b89d873b9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys([1, 2, 3, 'five', 'six'])"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dictSample.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "98058bd6-e0ed-42a3-8c2a-591fd4331ad7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_items([(1, 'first'), (2, 'two'), (3, 'three'), ('five', 5), ('six', 6)])"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dictSample.items()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ff672f33-1179-4ec2-b098-5a1abaaa6ae5",
   "metadata": {},
   "source": [
    "## insert()     -- inserts the elements at the specified index of the object\n",
    "####  -- supported datatypes: array, list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "c6f8b2c0-d53c-4604-b04a-bee60a4e542e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "array('i', [1, 100, 2, 3, 4, 3])\n"
     ]
    }
   ],
   "source": [
    "arrSample.insert(1, 100)    # inserting at specified position. insert(key, value)\n",
    "print(arrSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "84168e82-cffa-42cc-a396-c1fc5ba3f177",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "array('i', [1, 100, 2, 3, 4, 24, 3])\n"
     ]
    }
   ],
   "source": [
    "arrSample.insert(5, 24)\n",
    "print(arrSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0223c56-904e-4cc3-b1d8-306fa8ba4187",
   "metadata": {},
   "outputs": [],
   "source": [
    "## pop()    -- removes the elements at the given index from the object and prints the same\n",
    "#### default value is -1, which returns the last item.\n",
    "#### supported datatypes: array, list, set, dictionary."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "89537164-f7f2-4015-9946-b531637cf38e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "array('i', [1, 100, 2, 3, 4, 24])\n"
     ]
    }
   ],
   "source": [
    "arrSample.pop()\n",
    "print(arrSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "ce866c76-25b7-41f3-8437-d8d599693298",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 'bhargav', 2]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(listSample)\n",
    "listSample.pop(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "dde15839-d08a-485e-9e52-3c3277a0ed23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 'first', 2: 'two', 3: 'three', 'six': 6}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(dictSample)\n",
    "dictSample.pop('six')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "2482f1ea-3639-4414-ae86-6d013f9aca43",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'three'"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dictSample.pop(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5b9d5e63-d7f4-4ced-81d0-a61987460973",
   "metadata": {},
   "source": [
    "## Set is an unordered sequence and hence pop in not usually used\n",
    "#### the remove() method removes the first occurrence of the element with the specified value\n",
    "###### -- supported datatypes: array, list, dictionary, set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "b7cb780a-0041-4995-b6fc-e901dc154eda",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "array('i', [1, 100, 2, 3, 4, 24])\n"
     ]
    }
   ],
   "source": [
    "print(arrSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "47b48917-aea2-4082-b6ee-b65ffd48cfa1",
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "array.remove(x): x not in array",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[42], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43marrSample\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mremove\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m0\u001b[39;49m\u001b[43m)\u001b[49m\n",
      "\u001b[0;31mValueError\u001b[0m: array.remove(x): x not in array"
     ]
    }
   ],
   "source": [
    "arrSample.remove(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "00b28776-0861-4567-b627-d8132e1b9d1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "array('i', [2, 3, 4, 24])\n"
     ]
    }
   ],
   "source": [
    "arrSample.remove(100)\n",
    "print(arrSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "ac0eb9f3-47fa-43d7-b86c-b92a78260be2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 'bhargav']\n",
      "['bhargav']\n"
     ]
    }
   ],
   "source": [
    "print(listSample)\n",
    "listSample.remove(1)\n",
    "print(listSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "4997dae8-55ad-4cd2-ab77-a479e6014b85",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{10, 5}\n"
     ]
    },
    {
     "ename": "KeyError",
     "evalue": "226",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[50], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28mprint\u001b[39m(setSample)\n\u001b[0;32m----> 2\u001b[0m \u001b[43msetSample\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mremove\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m226\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28mprint\u001b[39m(setSample)\n",
      "\u001b[0;31mKeyError\u001b[0m: 226"
     ]
    }
   ],
   "source": [
    "print(setSample)\n",
    "setSample.remove(226)\n",
    "print(setSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "295e0612-1f1c-4fc3-91f3-d1862b5ae205",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{10, 5}\n"
     ]
    }
   ],
   "source": [
    "setSample.discard(226)\n",
    "print(setSample)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cfc93f63-5b08-4762-9d47-dd8c7b8d13cd",
   "metadata": {},
   "source": [
    "## del: deletes the entire object of any data type\n",
    "\n",
    "#### -- syntax: del obj_name\n",
    "#### -- del is a python keyword\n",
    "#### -- obj_name can be variables, user-defined, lists, items within lists, dictionaries etc.."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "d0c92b60-5cc1-4ada-9f9b-73268338cf7c",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'setSample' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[51], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mdel\u001b[39;00m setSample\n\u001b[0;32m----> 2\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43msetSample\u001b[49m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'setSample' is not defined"
     ]
    }
   ],
   "source": [
    "del setSample\n",
    "print(setSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "aa7b0a1b-ab36-4924-8d25-d15d4bc9a3d1",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'arrSample' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[52], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mdel\u001b[39;00m arrSample\n\u001b[0;32m----> 2\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43marrSample\u001b[49m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'arrSample' is not defined"
     ]
    }
   ],
   "source": [
    "del arrSample\n",
    "print(arrSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "853365b4-372d-4b07-b6db-3791e68a5716",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'listSample' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[53], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mdel\u001b[39;00m listSample\n\u001b[0;32m----> 2\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43mlistSample\u001b[49m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'listSample' is not defined"
     ]
    }
   ],
   "source": [
    "del listSample\n",
    "print(listSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "7695e6bc-eaed-457c-b926-b673e1da2524",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'listSample' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[54], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mdel\u001b[39;00m \u001b[43mlistSample\u001b[49m[\u001b[38;5;241m2\u001b[39m]\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28mprint\u001b[39m(listSample)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'listSample' is not defined"
     ]
    }
   ],
   "source": [
    "del listSample[2]\n",
    "print(listSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "3c6440b7-bcdc-42d0-9f5e-e1993fbc2300",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'listSample' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[55], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mdel\u001b[39;00m \u001b[43mlistSample\u001b[49m[\u001b[38;5;241m1\u001b[39m:\u001b[38;5;241m3\u001b[39m]\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28mprint\u001b[39m(listSample)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'listSample' is not defined"
     ]
    }
   ],
   "source": [
    "del listSample[1:3]\n",
    "print(listSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "c56d83fb-1db9-4182-8cc6-53328e67e8de",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'listSample' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[56], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mdel\u001b[39;00m \u001b[43mlistSample\u001b[49m[:]\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28mprint\u001b[39m(listSample)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'listSample' is not defined"
     ]
    }
   ],
   "source": [
    "del listSample[:]\n",
    "print(listSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "69b92acc-7398-4f8d-83f1-a84ab513d0f4",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'dictSample' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[57], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mdel\u001b[39;00m dictSample\n\u001b[0;32m----> 2\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43mdictSample\u001b[49m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'dictSample' is not defined"
     ]
    }
   ],
   "source": [
    "del dictSample\n",
    "print(dictSample)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c3a3e98-e4f9-4b3f-be0d-a1f2233dcff4",
   "metadata": {},
   "source": [
    "## the extend() method adds the specified list elements ( or any iterable - list, set, tuple, etc.) to the end of the current list"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd74a548-f341-4bdb-bedc-19106316046b",
   "metadata": {},
   "source": [
    "### Array Operations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "4204551e-ff6b-458a-a04f-3a5524ea14cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "array('i', [1, 2, 3, 4, 5, 6, 7, 8])\n"
     ]
    }
   ],
   "source": [
    "arrSample = array('i',[1, 2, 3])\n",
    "arrSample.extend((4, 5, 6, 7, 8))         # add a tuple to the arrSample array:\n",
    "print(arrSample)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "1355ffec-c29d-4ea9-b99e-44389adc8d24",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "an integer is required (got type str)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[60], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43marrSample\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mextend\u001b[49m\u001b[43m(\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mbhargav\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m)\u001b[49m)\n",
      "\u001b[0;31mTypeError\u001b[0m: an integer is required (got type str)"
     ]
    }
   ],
   "source": [
    "print(arrSample.extend(['bhargav']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "caa41131-2981-4353-942e-09ae9d5da72c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "array('i', [1, 2, 3, 4, 5, 6, 7, 8, 3, 4, 3, 4])\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6, 7, 8, 3, 4, 3, 4]"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arrSample.fromlist([3, 4])     # add values from a list to an array\n",
    "print(arrSample)\n",
    "\n",
    "arrSample.tolist()             # to convert an array into an ordinary list with th same items"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b26df3b-92c0-4b2e-9fb9-94cb0856a064",
   "metadata": {},
   "outputs": [],
   "source": [
    "range"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0237185a-45bd-4eab-b3ce-3169f85e3103",
   "metadata": {},
   "source": [
    "## List Operations\n",
    "\n",
    "### setSample\n",
    "####    A set is an unordered collection of items\n",
    "#####     Every element is unique (no duplicates)\n",
    "#####     sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "f1af2b60-1938-46b8-b73b-e56a6832317c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{24, 'data', 'example', 87.5}\n"
     ]
    }
   ],
   "source": [
    "A = {'example', 24, 87.5, 'data'}    # set with mixed data types\n",
    "print(A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "d9c92d11-e99f-4a17-89b2-e4028f495059",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{24, 87.5}\n"
     ]
    }
   ],
   "source": [
    "B = {24, 87.5}        # set of integers\n",
    "print(B)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "afde7c00-04b7-4c95-8cf5-40fbdf8c2451",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'example', 87.5, 24, 'data'}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{24, 87.5, 'data', 'example'}"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print (A | B)        # union of A and B is a set of all elements from both sets\n",
    "A.union(B)           # using union on B"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "597642d8-0f7d-4e5b-bc7b-a4d947d0b5e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{24, 87.5}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{24, 87.5}"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(A & B)      # intersection of A and B is a set of elements that are common in both sets\n",
    "A.intersection(B) # using intersection() on B"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a42b741b-856b-4e13-b1cc-2dd0caa6d1f5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
