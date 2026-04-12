---
concept: "Lagrange's Theorem"
slug: lagranges-theorem
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.8 Cosets"
extraction_confidence: high
aliases: []
prerequisites:
  - group
  - subgroup
  - coset
extends: []
related:
  - order-of-a-group
  - order-of-an-element
  - index
contrasts_with: []
answers_questions:
  - "How do cosets relate to Lagrange's theorem?"
---

# Quick Definition

Lagrange's theorem states that the order of any subgroup H of a finite group G divides the order of G. Consequently, the order of every element divides |G|.

# Core Definition

Theorem 2.8.9 (Lagrange's Theorem): Let H be a subgroup of a finite group G. The order of H divides the order of G (Artin, p. 72). This follows from the counting formula |G| = |H| * [G:H], since all cosets have the same size. Corollary: the order of any element divides |G| (Corollary 2.8.10). Corollary: a group of prime order p is cyclic (Corollary 2.8.11).

# Prerequisites

- **Group** — Must be a finite group
- **Subgroup** — The subgroup whose order divides |G|
- **Coset** — The proof uses the partition into cosets

# Key Properties

1. |H| divides |G| for any subgroup H of finite group G
2. [G:H] = |G|/|H| (the index)
3. The order of any element divides |G|
4. If |G| = p (prime), then G is cyclic
5. The converse is false: not every divisor of |G| need be the order of a subgroup

# Construction / Recognition

## To Construct:
1. Not applicable (this is a theorem, not a construction)

## To Recognize:
1. Any statement of the form "|H| divides |G|" is an application of Lagrange's theorem

# Context & Application

Lagrange's theorem is one of the most fundamental results in group theory. It immediately constrains what subgroups can exist and classifies groups of prime order as cyclic. Combined with the counting formula, it is a powerful tool.

# Examples

**Example 1** (p. 72): For <y> in S_3: |<y>| = 2 divides |S_3| = 6, and [S_3 : <y>] = 3.

**Example 2** (p. 72): Any group of prime order p is cyclic, since every non-identity element must have order p.

**Example 3** (p. 73): |ker(phi)| * |im(phi)| = |G| for a homomorphism phi from a finite group G.

# Relationships

## Builds Upon
- **Coset** — The proof uses the partition of G into cosets of H

## Enables
- Classification of groups of prime order as cyclic

## Related
- **Index** — [G:H] = |G|/|H|

# Common Errors

- **Error**: Thinking the converse holds (every divisor of |G| is the order of some subgroup)
  **Correction**: The converse is false in general; A_4 has order 12 but no subgroup of order 6

# Common Confusions

- **Confusion**: Thinking Lagrange's theorem gives the number of subgroups
  **Clarification**: It only constrains the ORDERS of subgroups, not their number

# Source Reference

Chapter 2: Groups, Section 2.8, pages 72-73.

# Verification Notes

- Definition source: Direct from Theorem 2.8.9, p. 72
- Confidence rationale: Named theorem with complete proof
- Uncertainties: None
- Cross-reference status: Verified
