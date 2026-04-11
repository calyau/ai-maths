---
concept: Partition of n
slug: partition-of-n
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
  - "integer partition"
prerequisites: []
extends: []
related:
  - cycle-type
  - conjugacy-class
  - elementary-divisors
contrasts_with: []
answers_questions:
  - "What is a partition of an integer?"
  - "How do partitions relate to conjugacy classes in S_n?"
---

# Quick Definition
A partition of a positive integer n is any nondecreasing sequence of positive integers whose sum is n. Partitions of n correspond bijectively to conjugacy classes of S_n (via cycle types) and to isomorphism types of abelian p-groups of order p^n.

# Core Definition
If n is a positive integer, a partition of n is any nondecreasing sequence of positive integers whose sum is n (Dummit & Foote, p. 130). By Proposition 11, the number of conjugacy classes of S_n equals the number of partitions of n. By the Fundamental Theorem of Abelian Groups, the number of abelian groups of order p^n also equals the number of partitions of n.

# Key Properties
1. Number of partitions of n = number of conjugacy classes of S_n
2. Number of partitions of n = number of abelian groups of order p^n
3. Partitions of 5: (5), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1,1,1,1,1) -- 7 partitions

# Examples
**Example 1** (p. 131): Partitions of 5 give 7 conjugacy classes of S_5.

**Example 2** (p. 164): Partitions of 5 give 7 abelian groups of order p^5.

# Relationships
## Related
- **Cycle type** — Cycle types are partitions; they classify conjugacy in S_n
- **Elementary divisors** — Exponents form partitions of prime-power parts

# Source Reference
Chapter 4, Section 4.3, page 130. Also Section 5.2, pages 164-165.

# Verification Notes
- Definition source: Direct from p. 130
- Confidence: HIGH
- Uncertainties: None
