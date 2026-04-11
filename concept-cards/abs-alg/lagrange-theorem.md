---
concept: "Lagrange's Theorem"
slug: lagrange-theorem
category: group-theory
subcategory: quotients
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Quotient Groups and Homomorphisms"
chapter_number: 3
pdf_page: 73
section: "3.2 More on Cosets and Lagrange's Theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - coset
  - subgroup
extends: []
related:
  - index-of-a-subgroup
  - cauchy-theorem
  - sylow-theorem
  - order-of-an-element
contrasts_with: []
answers_questions:
  - "How does the order of a subgroup relate to the order of a group?"
  - "What constraints does Lagrange's Theorem place on subgroup orders?"
---

# Quick Definition
If G is a finite group and H is a subgroup, then $|H|$ divides $|G|$, and the number of left cosets of H in G equals $|G|/|H|$.

# Core Definition
**Theorem 8 (Lagrange's Theorem):** If G is a finite group and H is a subgroup of G, then $|H|$ divides $|G|$ and the number of left cosets of H in G equals $|G|/|H|$. The proof follows from the fact that cosets partition G into subsets each of size $|H|$ (Dummit & Foote, pp. 89-90).

# Prerequisites
- **Coset** — the proof uses the coset partition
- **Subgroup** — applies to subgroups of finite groups

# Key Properties
1. $|H|$ divides $|G|$ for any subgroup H of finite G
2. Number of cosets $= |G|/|H|$ (the index)
3. $|x|$ divides $|G|$ for every $x \in G$ (Corollary 9)
4. $x^{|G|} = 1$ for all $x$ in a finite group G
5. Every group of prime order p is cyclic (Corollary 10)
6. The CONVERSE is false: n dividing $|G|$ does NOT guarantee a subgroup of order n

# Construction / Recognition
## To Apply:
1. Compute $|G|$ and $|H|$
2. Conclude $|H| \mid |G|$
3. The index $|G:H| = |G|/|H|$ counts the cosets

# Context & Application
Lagrange's Theorem is one of the most important combinatorial results in finite group theory. It constrains possible subgroup orders, gives Fermat's Little Theorem and Euler's Theorem as corollaries, and is used repeatedly throughout the text.

# Examples
**Example 1** (p. 90): $|S_3| = 6$, so subgroups can only have orders 1, 2, 3, or 6.
**Example 2** (p. 90): Groups of prime order p are cyclic: any nonidentity element generates the whole group.
**Example 3** (p. 91): $A_4$ (order 12) has no subgroup of order 6, showing the converse fails.

# Relationships
## Builds Upon
- **coset**, **subgroup**

## Enables
- **index-of-a-subgroup** — defined as $|G|/|H|$
- **cauchy-theorem** — partial converse for prime divisors
- **sylow-theorem** — partial converse for prime power divisors

## Related
- **order-of-an-element** — element order divides group order

# Common Errors
- **Error**: Assuming the converse: that G has a subgroup of order n for every divisor n of $|G|$. **Correction**: The converse is false in general ($A_4$ has no subgroup of order 6). Partial converses hold (Cauchy, Sylow).

# Common Confusions
- **Confusion**: Thinking Lagrange's Theorem says something about the number of subgroups of a given order. **Clarification**: It only constrains which orders are possible, not how many subgroups of each order exist.

# Source Reference
Chapter 3: Quotient Groups and Homomorphisms, Section 3.2, pages 89-93, Theorem 8, Corollaries 9-10.

# Verification Notes
- Definition source: direct from source pp. 89-90
- Confidence rationale: major theorem, explicitly proved
- Uncertainties: none
- Cross-reference status: verified
