{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "17133932-e1be-48d8-85ca-a8f8cd9d8384",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(2, 5), (3, 4)]\n"
     ]
    }
   ],
   "source": [
    "def find_pairs(arr, target_sum):\n",
    "    pairs = []\n",
    "    for i in range(len(arr)):\n",
    "        for j in range(i+1, len(arr)):\n",
    "            if arr[i] + arr[j] == target_sum:\n",
    "                pairs.append((arr[i], arr[j]))\n",
    "            \n",
    "    return pairs\n",
    "\n",
    "arr = [1, 2, 3, 4, 5]\n",
    "target_sum = 7\n",
    "result = find_pairs(arr, target_sum)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3a370f6d-7bd7-4b84-9b86-281f5cab81c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "def reverse_array(arr):\n",
    "    start_index = 0\n",
    "    end_index = len(arr) - 1\n",
    "    while end_index > start_index:\n",
    "        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]\n",
    "        start_index += 1\n",
    "        end_index -= 1\n",
    "\n",
    "arr = [ 1,2,3,4,5]\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e1524d3-463e-47f1-8895-325c48a29a04",
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
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
