---
concept: p-Group
slug: p-group
category: group-theory
subcategory: p-groups
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "More Group Theory"
chapter_number: 7
pdf_page: 206
section: "7.3 p-Groups"
extraction_confidence: high
aliases: []
prerequisites:
  - class-equation
extends: []
related:
  - sylow-p-subgroup
  - cauchys-theorem
  - fixed-point-theorem-p-group
contrasts_with: []
answers_questions:
  - "What is a p-group?"
  - "What must I know before studying the Sylow theorems?"
---

# Quick Definition

A p-group is a group whose order is a positive power of a prime p. The center of a p-group is always nontrivial, and every group of order p^2 is abelian.

# Core Definition

Groups whose orders are positive powers of a prime p are called p-groups (Artin, p. 209). The class equation proves that the center of a p-group is nontrivial (Proposition 7.3.1): if |G| = p^e with e >= 1, then every term in the class equation divides p^e, and since the left side is divisible by p, there must be more than one term equal to 1.

# Prerequisites

- **Class equation** — Used to prove key properties of p-groups

# Key Properties

1. Order is p^e for some prime p and e >= 1
2. Center is nontrivial (Proposition 7.3.1)
3. Every group of order p^2 is abelian (Proposition 7.3.3)
4. Groups of order p^2 are either cyclic or C_p x C_p (Corollary 7.3.4)
5. Fixed Point Theorem: if a p-group acts on a set whose order is not divisible by p, there is a fixed point (Theorem 7.3.2)

# Construction / Recognition

## To Recognize:
1. Check that |G| = p^e for some prime p

# Context & Application

p-groups are the building blocks for the Sylow theorems. The fact that p-groups have nontrivial centers is a powerful constraint used in classifying groups. The Fixed Point Theorem for p-groups is used in the proof of the second Sylow theorem.

# Examples

**Example 1** (p. 209): If |G| = p^2, the center Z has order p or p^2. If |Z| = p, choosing x not in Z gives Z(x) properly containing Z, forcing Z(x) = G, contradiction. So |Z| = p^2 and G is abelian.

**Example 2** (p. 209): Groups of order 8: there are 5 isomorphism classes. Groups of order 16: 14 classes. Order 32: 51 classes.

# Relationships

## Builds Upon
- **Class equation** — Proves center is nontrivial

## Enables
- **Sylow p-subgroup** — p-groups of maximal order in G
- **Cauchy's theorem** — Groups of order divisible by p contain elements of order p

## Related
- **Fixed point theorem (p-group)** — Key tool for Sylow proofs

# Common Errors

- **Error**: Assuming all p-groups are abelian
  **Correction**: Only groups of order p and p^2 are necessarily abelian; the dihedral group D_4 (order 8) is a non-abelian 2-group

# Source Reference

Chapter 7: More Group Theory, Section 7.3, Propositions 7.3.1-7.3.3, pages 209-210.

# Verification Notes

- Definition source: Direct from p. 209
- Confidence rationale: Explicitly defined with key properties proved
- Uncertainties: None
- Cross-reference status: Verified
