---
concept: Normal Subgroup
slug: normal-subgroup
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.5 Homomorphisms"
extraction_confidence: high
aliases: []
prerequisites:
  - group
  - subgroup
  - homomorphism
  - kernel
extends:
  - subgroup
related:
  - quotient-group
  - conjugate
  - coset
contrasts_with: []
answers_questions:
  - "What is a normal subgroup?"
  - "How do normal subgroups relate to quotient groups?"
  - "How does the kernel of a homomorphism relate to normal subgroups?"
---

# Quick Definition

A subgroup N of G is normal if gag^(-1) is in N for every a in N and every g in G. Equivalently, N is normal iff left cosets equal right cosets (gN = Ng). Every kernel is normal, and every normal subgroup is the kernel of some homomorphism.

# Core Definition

A subgroup N of a group G is a normal subgroup if for every a in N and every g in G, the conjugate gag^(-1) is in N (Definition 2.5.10, Artin, p. 63). Equivalent conditions (Proposition 2.8.17): (i) gNg^(-1) = N for all g, (ii) gN = Ng for all g (left cosets = right cosets), (iii) every left coset is a right coset.

# Prerequisites

- **Group** — N is a subgroup of a group
- **Subgroup** — Must be a subgroup first
- **Homomorphism** — Normal subgroups arise as kernels
- **Kernel** — Every kernel is normal

# Key Properties

1. gNg^(-1) = N for all g in G
2. Left cosets = right cosets: gN = Ng
3. Every kernel of a homomorphism is normal (Proposition 2.5.11)
4. Every normal subgroup is the kernel of the canonical map G -> G/N
5. Every subgroup of an abelian group is normal
6. Subgroups of non-abelian groups need not be normal

# Construction / Recognition

## To Construct:
1. Take the kernel of any homomorphism from G

## To Recognize:
1. Check that gag^(-1) is in N for all a in N and g in G
2. Or check that gN = Ng for all g in G

# Context & Application

Normal subgroups are precisely the subgroups for which quotient groups can be formed. The quotient G/N is a group iff N is normal. This is the key link between homomorphisms and quotient groups.

# Examples

**Example 1** (p. 63): SL_n(R) is normal in GL_n(R) (kernel of det).

**Example 2** (p. 63): A_n is normal in S_n (kernel of sign).

**Example 3** (p. 63): In S_3, <y> = {1, y} is NOT normal (xyx^(-1) = x^2y is not in <y>). But <x> = {1, x, x^2} IS normal.

# Relationships

## Builds Upon
- **Subgroup** — A normal subgroup is a subgroup with extra property
- **Kernel** — Every kernel is normal

## Enables
- **Quotient group** — G/N is a group when N is normal

## Related
- **Conjugate** — Normality means closure under conjugation
- **Coset** — Normal iff left and right cosets agree

# Common Errors

- **Error**: Assuming every subgroup is normal
  **Correction**: In non-abelian groups, many subgroups are not normal

# Common Confusions

- **Confusion**: Thinking "normal" means "typical" or "common"
  **Clarification**: "Normal" is a technical condition about invariance under conjugation

# Source Reference

Chapter 2: Groups, Sections 2.5 and 2.8, pages 63, 73-74.

# Verification Notes

- Definition source: Direct from Definition 2.5.10, p. 63
- Confidence rationale: Explicitly defined with multiple equivalences
- Uncertainties: None
- Cross-reference status: Verified
