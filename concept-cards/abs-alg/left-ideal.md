---
concept: Left Ideal
slug: left-ideal
category: ring-theory
subcategory: ideals
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 243
section: "7.3 Ring Homomorphisms and Quotient Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - ring
  - subring
extends:
  - subring
related:
  - ideal
  - right-ideal
contrasts_with:
  - right-ideal
  - ideal
answers_questions:
  - "What is a left ideal?"
  - "How do left ideals differ from two-sided ideals?"
---

# Quick Definition
A left ideal I of a ring R is a subring closed under left multiplication by all elements of R: $rI \subseteq I$ for all $r \in R$.

# Core Definition
A subset I of R is a *left ideal* if (i) I is a subring of R, and (ii) I is closed under left multiplication by elements from R, i.e., $rI \subseteq I$ for all $r \in R$. Similarly, a *right ideal* satisfies $Ir \subseteq I$. For commutative rings, left, right, and two-sided ideals coincide (Dummit & Foote, pp. 243-244).

# Prerequisites
- **Ring** — Left ideals are subsets of rings
- **Subring** — A left ideal must be a subring

# Key Properties
1. For commutative rings, left = right = two-sided
2. In $M_n(R)$: the set $L_j$ of matrices with arbitrary $j$th column and zeros elsewhere is a left ideal but NOT a right ideal (p. 248)
3. A ring D with $1 \neq 0$ is a division ring iff its only left ideals are 0 and D (p. 254)

# Examples
**Example** (p. 248): In $M_n(R)$, the set of matrices with arbitrary entries in column j and zeros elsewhere is a left ideal but not a right ideal.

# Relationships

## Related
- **ideal** — A two-sided ideal is both a left and right ideal
- **right-ideal** — Closed under right multiplication instead

## Contrasts With
- **ideal** — A left ideal need not be a right ideal in noncommutative rings

# Source Reference
Chapter 7, Section 7.3, Definition (2), pages 243-244.

# Verification Notes
- Definition: Direct from pp. 243-244
- Confidence: HIGH — explicit definition
