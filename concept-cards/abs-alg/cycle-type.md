---
concept: Cycle Type
slug: cycle-type
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 130
section: "4.3 Groups Acting on Themselves by Conjugation"
extraction_confidence: high
aliases:
  - "cycle structure"
prerequisites:
  - symmetric-group
  - conjugacy-class
extends: []
related:
  - partition-of-n
  - conjugacy-class
contrasts_with: []
answers_questions:
  - "What determines conjugacy in symmetric groups?"
  - "What is the cycle type of a permutation?"
---

# Quick Definition
The cycle type of a permutation sigma in S_n is the nondecreasing sequence of lengths of the disjoint cycles in its cycle decomposition (including 1-cycles). Two elements of S_n are conjugate if and only if they have the same cycle type.

# Core Definition
If sigma in S_n is the product of disjoint cycles of lengths n_1 <= n_2 <= ... <= n_r (including 1-cycles), the integers n_1, ..., n_r are called the cycle type of sigma (Dummit & Foote, p. 130). By Proposition 11, two elements of S_n are conjugate in S_n if and only if they have the same cycle type. The number of conjugacy classes of S_n equals the number of partitions of n. A partition of n is any nondecreasing sequence of positive integers summing to n.

# Prerequisites
- **Symmetric group** — Cycle types are defined for permutations
- **Conjugacy class** — Cycle type determines conjugacy in S_n

# Key Properties
1. Cycle type uniquely determines conjugacy class in S_n (Proposition 11)
2. Number of conjugacy classes of S_n = number of partitions of n
3. Conjugation by tau replaces each entry i in sigma's cycles by tau(i) (Proposition 10)
4. The cycle type is unique up to ordering

# Examples
**Example 1** (p. 131): For n = 5, the 7 partitions give 7 conjugacy classes with representatives: 1, (12), (123), (1234), (12345), (12)(34), (12)(345).

# Relationships
## Enables
- **Conjugacy class** — Cycle type classifies conjugacy in S_n
## Related
- **Partition of n** — Cycle types correspond bijectively to partitions of n

# Source Reference
Chapter 4, Section 4.3, pages 130-131. Propositions 10 and 11.

# Verification Notes
- Definition source: Direct from p. 130
- Confidence: HIGH
- Uncertainties: None
