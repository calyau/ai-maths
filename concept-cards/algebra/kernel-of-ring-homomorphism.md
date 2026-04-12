---
concept: Kernel of a Ring Homomorphism
slug: kernel-of-ring-homomorphism
category: ring-theory
subcategory: morphisms
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Homomorphisms and Ideals"
extraction_confidence: high
aliases: []
prerequisites:
  - ring-homomorphism
extends: []
related:
  - ideal
  - first-isomorphism-theorem-rings
contrasts_with: []
answers_questions:
  - "What is the kernel of a ring homomorphism?"
  - "How do ideals relate to quotient rings?"
---

# Quick Definition

The kernel of a ring homomorphism phi: R -> R' is the set of elements of R that map to zero. It is always an ideal of R, and phi is injective if and only if its kernel is {0}.

# Core Definition

Let phi: R -> R' be a ring homomorphism. The kernel of phi is ker phi = {s in R | phi(s) = 0} (Artin, formula 11.3.11, p. 346). The kernel is an ideal of R: if s is in ker phi, then for every r in R, rs is in ker phi. The homomorphism is injective if and only if ker phi = (0).

# Prerequisites

- **Ring homomorphism** -- Kernel is a property of a homomorphism

# Key Properties

1. The kernel is an ideal (not just a subring)
2. phi is injective if and only if ker phi = (0)
3. The kernel property rs in ker phi for s in ker phi and any r in R motivates the definition of ideal

# Context & Application

The kernel-ideal connection is the bridge between homomorphisms and ideals, exactly as the kernel-normal subgroup connection works for groups.

# Examples

**Example 1** (p. 347): The kernel of the substitution map R[x] -> R sending x to 2 is the principal ideal (x - 2).

**Example 2** (p. 347): The kernel of the map Z[x] -> F_p sending f(x) to f(0) mod p is the ideal (p, x).

# Relationships

## Builds Upon
- **Ring homomorphism** -- Kernel is defined for homomorphisms

## Enables
- **Ideal** -- The kernel motivated the definition of ideals
- **First Isomorphism Theorem (rings)** -- R/ker(phi) is isomorphic to im(phi)

# Source Reference

Chapter 11: Rings, Section 11.3, formula 11.3.11, pages 346-347.

# Verification Notes

- Definition source: Direct from formula 11.3.11
- Confidence rationale: Explicit definition and motivation
- Uncertainties: None
- Cross-reference status: Verified
