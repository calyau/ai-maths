---
concept: Subgroup
slug: subgroup
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.2 Groups and Subgroups"
extraction_confidence: high
aliases: []
prerequisites:
  - group
extends: []
related:
  - normal-subgroup
  - coset
  - lagranges-theorem
contrasts_with: []
answers_questions:
  - "What is a subgroup?"
  - "How do I determine if a subset is a subgroup?"
---

# Quick Definition

A subgroup H of a group G is a subset that is itself a group under the same law of composition. This requires closure (ab in H), identity (1 in H), and inverses (a^(-1) in H).

# Core Definition

A subset H of a group G is a subgroup if it has the following properties (Artin, p. 54, formula 2.2.9):
- Closure: If a and b are in H, then ab is in H
- Identity: 1 is in H
- Inverses: If a is in H, then a^(-1) is in H

Associativity carries over automatically from G.

# Prerequisites

- **Group** — A subgroup is a subset of a group that is itself a group

# Key Properties

1. Every group has two obvious subgroups: G itself and {1} (the trivial subgroup)
2. A subgroup is proper if it is neither of these
3. The intersection of any family of subgroups is a subgroup
4. The order of H divides the order of G (Lagrange's theorem)

# Construction / Recognition

## To Construct:
1. Identify a subset H of a group G
2. Verify closure, identity, and inverses

## To Recognize:
1. Check the three subgroup conditions
2. Alternative: H is nonempty and for all a, b in H, ab^(-1) is in H

# Context & Application

Subgroups are the fundamental structural tool in group theory. They appear as kernels and images of homomorphisms, generate cosets and quotient groups, and their orders are constrained by Lagrange's theorem.

# Examples

**Example 1** (p. 54): The set of invertible upper triangular 2x2 matrices is a subgroup of GL_2.

**Example 2** (p. 55): The circle group (complex numbers of absolute value 1) is a subgroup of C*.

**Example 3** (p. 55): SL_n (matrices with determinant 1) is a subgroup of GL_n.

# Relationships

## Builds Upon
- **Group** — A subgroup is a subset that is a group

## Enables
- **Coset** — aH = {ah : h in H} is a left coset
- **Lagrange's theorem** — |H| divides |G|
- **Normal subgroup** — A subgroup that is the kernel of some homomorphism

# Common Errors

- **Error**: Forgetting to check that the identity is in H
  **Correction**: Always verify 1 is in H (or equivalently, that H is nonempty)

- **Error**: Checking only closure, forgetting inverses
  **Correction**: All three conditions must hold (or use the combined test: ab^(-1) in H)

# Common Confusions

- **Confusion**: Thinking every subset closed under the operation is a subgroup
  **Clarification**: The subset must also contain the identity and be closed under inverses

# Source Reference

Chapter 2: Groups, Section 2.2, pages 54-55.

# Verification Notes

- Definition source: Direct from (2.2.9), p. 54
- Confidence rationale: Explicitly defined with examples
- Uncertainties: None
- Cross-reference status: Verified
