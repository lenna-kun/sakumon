## Problem Statement

There are $N$ cards for each of spades, clovers, diamonds, and hearts, and there are $N$ cards with numbers $1$ to $N$ for each mark. For example, "1" of spade, "1" of clover, "1" of diamond, and "1" of heart are represented by "S1", "C1", "D1", and "H1", respectively. Initially, the cards are arranged in the order of $\{S1,...,SN,C1,...CN,D1,...,DN,H1,...,HN\}$.

"Shuffle" according to 'Q' queries. Specifically, in the $i (1 \leq i \leq Q)$-th query, do the following:

- $L_i$ and $R_i$ are given. Bring all the cards from card $L_i$ to card $R_i$ to the beginning while keeping their order. That is, when $L_i=a_j,R_i=a_k (1 \leq j \leq k \leq 4N)$ in the sequence $\{a_1,…,a_{j-1},a_j,…,a_k,a_{k+1}...,a_{4N}\}$ of the card, the sequence is changed to $\{a_j,…,a_k,a_1,…,a_{j−1},a_{k+1},...a_{4N}\}$.

Process $Q$ queries in order, and Output the subsequence consisting only of all spade cards, the subsequence consisting only of all clover cards, the subsequence consisting only of all diamond cards, and the subsequence consisting only of all heart cards in this order.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

## Constraints

- $1 \leq N \leq {10}^5$
- $1 \leq Q \leq {10}^5$

## Input

$N\ Q$

$L_i\ R_i(1 \leq i \leq Q)$

$L_i$ and $R_i$ are $4N$ kinds of character strings that can be made by arranging one character of "S" or "C" or "D" or "H" and the number $j (1 \leq j \leq N)$ respectively.

## Output

Output the subsequence consisting only of spade cards, the subsequence consisting only of clover cards, the subsequence consisting only of diamond cards, and the subsequence consisting only of heart cards in this order in 4 rows.
