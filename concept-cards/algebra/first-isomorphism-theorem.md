---
concept: First Isomorphism Theorem
slug: first-isomorphism-theorem
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
  - "fundamental homomorphism theorem"
prerequisites:
  - homomorphism
  - kernel
  - quotient-group
extends: []
related:
  - correspondence-theorem
contrasts_with: []
answers_questions:
  - "What is a homomorphism?"
---

# Quick Definition

The First Isomorphism Theorem states that if phi: G -> G' is a surjective homomorphism with kernel N, then the quotient group G/N is isomorphic to G'. More generally, G/ker(phi) ≅ im(phi).

# Core Definition

Theorem 2.12.10: Let phi: G -> G' be a surjective group homomorphism with kernel N. The quotient group G/N is isomorphic to G'. Precisely, there is a unique isomorphism phi_bar: G/N -> G' such that phi = phi_bar ∘ pi, where pi: G -> G/N is the canonical map (Artin, pp. 79-80). Corollary 2.12.11 extends this: for any homomorphism phi, G/ker(phi) ≅ im(phi).

# Prerequisites

- **Homomorphism** — The map whose kernel and image are being related
- **Kernel** — The normal subgroup being quotiented out
- **Quotient group** — G/N is the quotient

# Key Properties

1. G/ker(phi) ≅ im(phi)
2. The isomorphism sends the coset aN to phi(a)
3. Every quotient G/N arises this way (from the canonical map)
4. Provides a fundamental method for identifying quotient groups

# Construction / Recognition

## To Construct:
1. Given phi: G -> G', identify ker(phi)
2. The quotient G/ker(phi) is isomorphic to im(phi)

## To Recognize:
1. Any identification of a quotient group with a known group

# Context & Application

The First Isomorphism Theorem is the fundamental structural result connecting homomorphisms and quotient groups. It provides the standard method for computing quotient groups: find a suitable surjective homomorphism, and the quotient by the kernel equals the image.

# Examples

**Example 1** (p. 80): det: GL_n(R) -> R* is surjective with kernel SL_n. So GL_n/SL_n ≅ R*.

**Example 2** (p. 80): |·|: C* -> R*_+ (absolute value) has kernel U (unit circle). So C*/U ≅ R*_+.

# Relationships

## Builds Upon
- **Homomorphism** — The map being analyzed
- **Kernel** — Quotiented out
- **Quotient group** — The result

## Related
- **Correspondence theorem** — Extends the theorem to subgroup lattices

# Common Errors

- **Error**: Applying the theorem to a non-surjective homomorphism without adjusting the codomain
  **Correction**: For non-surjective phi, the isomorphism is G/ker(phi) ≅ im(phi), not G'

# Common Confusions

- **Confusion**: Thinking the theorem constructs new groups
  **Clarification**: It identifies a quotient group with a known image; both already exist

# Source Reference

Chapter 2: Groups, Section 2.12, pages 79-80.

# Verification Notes

- Definition source: Direct from Theorem 2.12.10
- Confidence rationale: Named theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
