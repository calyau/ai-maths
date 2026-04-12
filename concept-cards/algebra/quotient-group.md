---
concept: Quotient Group
slug: quotient-group
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.12 Quotient Groups"
extraction_confidence: high
aliases:
  - "factor group"
  - "G/N"
prerequisites:
  - group
  - normal-subgroup
  - coset
extends: []
related:
  - first-isomorphism-theorem
  - integers-mod-n
contrasts_with: []
answers_questions:
  - "What is a quotient group?"
  - "How do normal subgroups relate to quotient groups?"
  - "What must I know before understanding quotient groups?"
---

# Quick Definition

The quotient group G/N is the group formed by the cosets of a normal subgroup N, with multiplication defined by (aN)(bN) = (ab)N. The canonical map pi: G -> G/N sending a to its coset aN is a surjective homomorphism with kernel N.

# Core Definition

Let N be a normal subgroup of G. The set G/N of cosets of N in G becomes a group under the law [aN][bN] = [abN] (Theorem 2.12.2, Artin, pp. 78-79). The normality of N is essential: it ensures the product set (aN)(bN) = abN is a single coset (Lemma 2.12.5). The canonical map pi: G -> G/N defined by pi(a) = aN is a surjective homomorphism with kernel N.

# Prerequisites

- **Group** — The group G being quotiented
- **Normal subgroup** — N must be normal for the quotient to be a group
- **Coset** — Elements of G/N are cosets

# Key Properties

1. Elements of G/N are the cosets aN of N
2. Multiplication: (aN)(bN) = (ab)N
3. The canonical map pi: G -> G/N is a surjective homomorphism with ker(pi) = N
4. |G/N| = [G:N] = |G|/|N| for finite groups
5. N must be normal for the product of cosets to be well-defined

# Construction / Recognition

## To Construct:
1. Identify a normal subgroup N of G
2. Form the set of cosets {aN : a in G}
3. Define (aN)(bN) = (ab)N

## To Recognize:
1. A group whose elements are cosets of a normal subgroup

# Context & Application

Quotient groups are one of the most important constructions in algebra. They simplify a group by "collapsing" a normal subgroup to the identity. Z/nZ is the prototypical example. The First Isomorphism Theorem says every quotient by a kernel is isomorphic to the image.

# Examples

**Example 1** (p. 78): Z/nZ — the integers modulo n, where the normal subgroup is nZ.

**Example 2** (p. 80): GL_n(R)/SL_n(R) ≅ R* via the determinant map.

**Example 3** (p. 80): C*/U ≅ R*_+ (positive reals), where U is the unit circle.

# Relationships

## Builds Upon
- **Normal subgroup** — N must be normal
- **Coset** — Elements of G/N are cosets

## Enables
- **First isomorphism theorem** — G/ker(phi) ≅ im(phi)

## Related
- **Integers mod n** — Z/nZ is the simplest quotient group

# Common Errors

- **Error**: Trying to form a quotient group with a non-normal subgroup
  **Correction**: The subgroup MUST be normal for coset multiplication to be well-defined

# Common Confusions

- **Confusion**: Thinking the elements of G/N are elements of G
  **Clarification**: Elements of G/N are cosets (subsets of G), not individual elements

# Source Reference

Chapter 2: Groups, Section 2.12, pages 78-81.

# Verification Notes

- Definition source: Direct from Theorem 2.12.2, pp. 78-79
- Confidence rationale: Central construction with detailed proof
- Uncertainties: None
- Cross-reference status: Verified
