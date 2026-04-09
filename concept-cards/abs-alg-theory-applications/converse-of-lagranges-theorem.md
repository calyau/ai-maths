---
concept: Converse of Lagrange's Theorem
slug: converse-of-lagranges-theorem
category: group-structure
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Cosets and Lagrange's Theorem"
chapter_number: 6
pdf_page: 89
section: "6.2 Lagrange's Theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - lagranges-theorem
  - alternating-group
extends: []
related:
  - groups-of-prime-order
contrasts_with: []
answers_questions:
  - "Does the converse of Lagrange's theorem hold?"
  - "Does every divisor of |G| correspond to a subgroup?"
---

# Quick Definition

The converse of Lagrange's Theorem is false: if $d$ divides $|G|$, there need not exist a subgroup of order $d$. The standard counterexample is $A_4$ (order 12), which has no subgroup of order 6.

# Core Definition

"The converse of Lagrange's Theorem is false. The group $A_4$ has order 12; however, it can be shown that it does not possess a subgroup of order 6" (Judson, Remark 6.14, p. 89). Proposition 6.15 proves this by showing that any subgroup of $A_4$ containing a 3-cycle must contain at least 7 elements, contradicting order 6.

# Prerequisites

- **Lagrange's Theorem** — The converse of this theorem is being examined
- **Alternating Group** — $A_4$ provides the counterexample

# Key Properties

1. 6 divides 12, but $A_4$ has no subgroup of order 6
2. Lagrange only restricts which subgroup orders are *possible* (divisors of $|G|$)
3. It does not guarantee existence of subgroups of every possible order
4. The converse does hold for cyclic groups and for certain special classes

# Construction / Recognition

## To Show $A_4$ has No Subgroup of Order 6:
1. Suppose $H \leq A_4$ with $|H| = 6$
2. Then $[A_4 : H] = 2$, so $gH = Hg$ for all $g$
3. $H$ must contain a 3-cycle and its inverse
4. Conjugation forces $H$ to contain additional 3-cycles
5. This gives $|H| \geq 7$, a contradiction

# Context & Application

This counterexample is important because it shows that Lagrange's Theorem, while powerful, has limits. The question of which groups have subgroups of every possible order leads to the Sylow theorems.

# Examples

**Example 1** (p. 89-90): $A_4$ has order 12. Divisors of 12 are 1, 2, 3, 4, 6, 12. $A_4$ has subgroups of orders 1, 2, 3, 4, and 12, but not 6.

# Relationships

## Builds Upon
- **Lagrange's Theorem** — This is about its converse
- **Alternating Group** — $A_4$ provides the counterexample

## Related
- **Groups of Prime Order** — For prime order, the converse trivially holds

# Common Errors

- **Error**: Assuming every divisor of $|G|$ yields a subgroup
  **Correction**: Lagrange's theorem only gives a necessary condition, not sufficient

# Common Confusions

- **Confusion**: Thinking the converse fails for all groups
  **Clarification**: For cyclic groups, the converse holds (a cyclic group of order $n$ has exactly one subgroup of each order dividing $n$)

# Source Reference

Chapter 6: Cosets and Lagrange's Theorem, Section 6.2, Remark 6.14, Proposition 6.15, pages 89-90.

# Verification Notes

- Definition source: Direct from Remark 6.14 and Proposition 6.15
- Confidence rationale: Explicit counterexample with proof
- Uncertainties: None
- Cross-reference status: Verified
