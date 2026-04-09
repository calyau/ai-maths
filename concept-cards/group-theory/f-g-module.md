---
# === CORE IDENTIFICATION ===
concept: F[G]-module
slug: f-g-module

# === CLASSIFICATION ===
category: representation-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 104
section: "The group algebra; semisimplicity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "module over the group algebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-algebra
  - linear-representation
extends: []
related:
  - g-invariant-subspace
  - irreducible-representation
  - simple-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an F[G]-module?"
  - "How do F[G]-modules relate to linear representations?"
---

# Quick Definition

An F[G]-module is an F-vector space V with a linear action of F[G], equivalently a linear representation of G on V.

# Core Definition

A linear action of G on an F-vector space V extends uniquely to an action of F[G] on V via (sum c_g g) v = sum c_g (gv), making V into an **F[G]-module**. The submodules are exactly the G-invariant subspaces. Conversely, every F[G]-module structure on V restricts to a linear representation G -> GL(V). (Milne, Chapter 7, p. 104)

# Prerequisites

- **Group algebra** — F[G]-modules are modules over the group algebra
- **Linear representation** — equivalent formulation

# Key Properties

1. F[G]-modules are the same as linear representations of G
2. F[G]-submodules = G-invariant subspaces
3. Simple F[G]-modules = irreducible representations
4. Semisimple F[G]-modules = completely reducible representations
5. All F[G]-modules are finite-dimensional as F-vector spaces (by convention in this chapter)

# Construction / Recognition

1. Given a linear representation rho: G -> GL(V)
2. Define (sum c_g g) v = sum c_g rho(g)(v)
3. This makes V an F[G]-module
4. The construction is reversible

# Context & Application

The equivalence between linear representations and F[G]-modules is the fundamental translation that allows module-theoretic tools to be applied to representation theory. Module decomposition = representation decomposition. Simple modules = irreducible representations.

# Examples

**Example 1** (p. 104): Any representation G -> GL(V) extends to an F[G]-module structure on V.

# Relationships

## Builds Upon
- **group-algebra** — the ring of scalars
- **linear-representation** — equivalent formulation

## Enables
- All module-theoretic results apply to representations

## Related
- **g-invariant-subspace** — = F[G]-submodule
- **irreducible-representation** — = simple F[G]-module

## Contrasts With
- Modules over other algebras (not arising from groups)

# Common Errors

- **Error**: Thinking F[G]-modules and representations are different theories
  **Correction**: They are the same theory in different language

# Source Reference

Chapter 7: Representations of Finite Groups, p. 104.

# Verification Notes

- Definition source: Direct from p. 104
- Confidence rationale: HIGH — explicit construction
- Uncertainties: None
