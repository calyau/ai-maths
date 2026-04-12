---
# === CORE IDENTIFICATION ===
concept: Module
slug: module

# === CLASSIFICATION ===
category: module-theory
subcategory: basic-definitions
tier: advanced

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Algebra in a Ring"
chapter_number: 14
pdf_page: 432
section: "14.1 Modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "R-module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ring
  - abelian-group
extends:
  - vector-space
related:
  - submodule
  - free-module
  - module-homomorphism
contrasts_with:
  - vector-space

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a module?"
  - "What must I know before learning about modules?"
  - "How do modules generalize vector spaces?"
---

# Quick Definition

A module over a ring R is an abelian group equipped with a scalar multiplication by elements of R, satisfying axioms analogous to those of a vector space. Modules generalize vector spaces by allowing scalars from a ring rather than a field.

# Core Definition

Let R be a ring. An R-module V is an abelian group with a law of composition written +, and a scalar multiplication R x V -> V, written (r, v) -> rv, that satisfies these axioms (Artin, p. 432):

1v = v, (rs)v = r(sv), (r+s)v = rv + sv, and r(v+v') = rv + rv'

for all r and s in R and all v and v' in V. These are precisely the axioms for a vector space (3.1.2), but since elements of a ring need not be invertible, modules are more complicated than vector spaces.

# Prerequisites

- **Ring** -- Scalars come from a ring, so the ring axioms must be understood
- **Abelian group** -- The underlying additive structure of a module is an abelian group
- **Vector space** -- Modules generalize vector spaces; understanding vector spaces provides essential intuition

# Key Properties

1. Every vector space over a field is a module over that field
2. Abelian group and Z-module are equivalent concepts (14.1.2)
3. Submodules of the R-module R are exactly the ideals of R (Proposition 14.1.3)
4. Most modules have no basis (unlike vector spaces)
5. Finite nonzero abelian groups are not free Z-modules

# Construction / Recognition

## To Construct:
1. Start with an abelian group (V, +)
2. Define a scalar multiplication R x V -> V
3. Verify the four module axioms: 1v = v, (rs)v = r(sv), (r+s)v = rv + sv, r(v+v') = rv + rv'

## To Recognize:
1. Check that the underlying set forms an abelian group under addition
2. Verify scalar multiplication by ring elements is defined
3. Confirm all four module axioms hold

# Context & Application

Modules are the central objects of Chapter 14 and provide the framework for studying linear algebra over rings instead of fields. They unify the classification of finitely generated abelian groups (over Z) and the theory of linear operators on vector spaces (over F[t]). The structure theorem for finitely generated modules over a PID is one of the most important results in algebra.

# Examples

**Example 1** (p. 432): The free modules R^n, consisting of column vectors with entries in R, with componentwise addition and scalar multiplication. These are the analog of the vector spaces F^n.

**Example 2** (p. 432): Any abelian group V can be made into a Z-module in exactly one way, by setting nv = v + ... + v (n times) for positive integers n, and (-n)v = -(nv).

**Example 3** (p. 433): Finite abelian groups are Z-modules that are not free, since Z^n is infinite for positive n.

# Relationships

## Builds Upon
- **Ring** -- Provides the scalars for the module
- **Abelian group** -- Every module is an abelian group under addition

## Enables
- **Free module** -- Special case where a basis exists
- **Structure theorem for finitely generated modules over a PID** -- The major classification result
- **Rational canonical form** -- Application to linear operators via F[t]-modules

## Related
- **Submodule** -- Subsets closed under addition and scalar multiplication
- **Module homomorphism** -- Structure-preserving maps between modules

## Contrasts With
- **Vector space** -- A module over a field; always has a basis, unlike general modules

# Common Errors

- **Error**: Assuming every module has a basis (as with vector spaces)
  **Correction**: Only free modules have bases; most modules do not. Finite nonzero abelian groups, for instance, are not free Z-modules.

- **Error**: Applying field-specific results (like dimension theory) directly to modules
  **Correction**: Many vector space results fail for modules because ring elements need not be invertible.

# Common Confusions

- **Confusion**: Believing that Z-modules and abelian groups are different concepts
  **Clarification**: They are equivalent concepts (14.1.2); the Z-module structure on an abelian group is uniquely determined.

- **Confusion**: Thinking modules are just "vector spaces over rings"
  **Clarification**: While the axioms are identical, the lack of multiplicative inverses in rings makes module theory fundamentally different and richer.

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.1, pages 432-434. See especially the axioms (14.1.1) and the equivalence of abelian groups and Z-modules (14.1.2).

# Verification Notes

- Definition source: Direct from Artin, p. 432, explicitly stated axioms
- Confidence rationale: Explicitly defined with clear axioms
- Uncertainties: None
- Cross-reference status: Verified against prerequisites and related concepts
