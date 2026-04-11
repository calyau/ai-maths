---
concept: Product of Ideals
slug: product-of-ideals
category: ring-theory
subcategory: ideals
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 247
section: "7.3 Ring Homomorphisms and Quotient Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - ideal
extends: []
related:
  - sum-of-ideals
  - comaximal-ideals
  - chinese-remainder-theorem
contrasts_with: []
answers_questions:
  - "What is the product of two ideals?"
  - "How does the product of ideals relate to their intersection?"
---

# Quick Definition
The product IJ of ideals I and J is the ideal consisting of all finite sums of elements $ab$ with $a \in I$ and $b \in J$.

# Core Definition
The *product* of ideals I and J, denoted IJ, is the set of all finite sums of elements of the form $ab$ with $a \in I$ and $b \in J$. The $n^{th}$ power $I^n$ is defined inductively: $I^1 = I$ and $I^n = II^{n-1}$ (Dummit & Foote, p. 248).

# Prerequisites
- **Ideal** — Both factors must be ideals

# Key Properties
1. IJ is an ideal contained in $I \cap J$ (p. 248)
2. IJ may be strictly smaller than $I \cap J$ (Exercise 34(c), p. 250)
3. If I + J = R (comaximal), then $IJ = I \cap J$ (Exercise 34(d), p. 251)
4. $I(J+K) = IJ + IK$ (distributive law, Exercise 35, p. 251)
5. The set $\{ab \mid a \in I, b \in J\}$ is generally *not* closed under addition, hence not an ideal

# Construction / Recognition
## To Construct:
1. Form all products $ab$ with $a \in I$, $b \in J$
2. Take all finite sums of such products
3. The resulting set is the ideal IJ

# Context & Application
Products of ideals are essential for the Chinese Remainder Theorem and for understanding ideal factorization in Dedekind domains.

# Examples
**Example 1** (p. 248): In $\mathbb{Z}$, $(6)(10) = (60)$ since $6\mathbb{Z} \cdot 10\mathbb{Z} = 60\mathbb{Z}$.

**Example 2** (p. 249): In $\mathbb{Z}[x]$, if $I = (2, x)$ then $I^2$ contains $x^2 + 4$ but this cannot be written as a single product $pq$ with $p, q \in I$.

# Relationships

## Related
- **sum-of-ideals** — $I + J$ is the smallest ideal containing both
- **comaximal-ideals** — When $I + J = R$, $IJ = I \cap J$
- **chinese-remainder-theorem** — Uses products of comaximal ideals

# Common Errors
- **Error**: Thinking IJ is just the set $\{ab \mid a \in I, b \in J\}$
  **Correction**: IJ consists of all *finite sums* of such products

# Common Confusions
- **Confusion**: Assuming $IJ = I \cap J$ always
  **Clarification**: This holds only when I and J are comaximal; in general $IJ \subseteq I \cap J$

# Source Reference
Chapter 7, Section 7.3, Definition on page 248.

# Verification Notes
- Definition: Direct from p. 248
- Confidence: HIGH — explicit definition
