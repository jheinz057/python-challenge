{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os \n",
    "import csv\n",
    "from collections import Counter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import the csv\n",
    "csvpath = os.path.join('election_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculate the total number of votes and candidate votes\n",
    "total_votes = 0\n",
    "candidate_votes = []\n",
    "with open (csvpath, newline=\"\") as csvfile:\n",
    "    csv_reader = csv.reader(csvfile, delimiter = \",\")\n",
    "    next(csv_reader, None)\n",
    "    for row in csv_reader:\n",
    "        total_votes += 1\n",
    "        candidate_votes.append(row[2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3521001"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "total_votes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# distinct list of all candidates and their respective number of votes\n",
    "c= Counter(candidate_votes)  \n",
    "c= dict(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Khan': 0.6300001050837531,\n",
       " 'Correy': 0.19999994319797126,\n",
       " 'Li': 0.13999996023857988,\n",
       " \"O'Tooley\": 0.02999999147969569}"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# determine the percentage of total votes each candidate received\n",
    "c_percent = {k:v / total for total in (sum(c.values()),) for k, v in c.items()}\n",
    "c_percent"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Khan'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# determine winner based on popular vote\n",
    "winner = max(c, key= lambda key: c[key])\n",
    "winner"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# merge the count dictionary and count percentage dictionary\n",
    "ml = [c,c_percent]\n",
    "md= {}\n",
    "for k in c.keys():\n",
    "    md[k] = tuple(md[k] for md in ml)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Khan': (2218231, 0.6300001050837531),\n",
       " 'Correy': (704200, 0.19999994319797126),\n",
       " 'Li': (492940, 0.13999996023857988),\n",
       " \"O'Tooley\": (105630, 0.02999999147969569)}"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "md"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "Total Votes: 3521001\n",
      "Khan: 63% (2218231)\n",
      "Correy: 20% (704200)\n",
      "Li: 14% (492940)\n",
      "O'Tooley: 3% (105630)\n",
      "Winner: Khan\n"
     ]
    }
   ],
   "source": [
    "# print results using the specified format\n",
    "print('Election Results')\n",
    "print('Total Votes: {}'.format(total_votes))\n",
    "for x,y in md.items():\n",
    "    print(\"{}: {:0.0%} ({})\".format(x,y[1],y[0]))\n",
    "print('Winner: {}'.format(winner))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pypoll_file = open(\"pypoll.txt\", \"w\")\n",
    "\n",
    "\n",
    "\n",
    "# writing the text file\n",
    "\n",
    "pypoll_file.write(\"Election Results \\n\")\n",
    "\n",
    "pypoll_file.write(\"-------------------------------------------- \\n\")\n",
    "\n",
    "pypoll_file.write(\"Total Votes: \" + str(total_votes) + \"\\n\")\n",
    "\n",
    "pypoll_file.write(\"Winner: \" + str(winner) + \"\\n\")\n",
    "                  \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
