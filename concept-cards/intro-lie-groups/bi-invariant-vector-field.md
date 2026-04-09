---
# === CORE IDENTIFICATION ===
concept: Bi-Invariant Vector Field
slug: bi-invariant-vector-field

# === CLASSIFICATION ===
category: lie-groups
subcategory: group-actions
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 14
section: "2.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - left-invariant-vector-field
  - adjoint-action-on-lie-group
extends:
  - left-invariant-vector-field
related:
  - center-of-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

A bi-invariant vector field on $G$ is one that is both left- and right-invariant. The space of bi-invariant vector fields is isomorphic to $(T_1G)^{\mathrm{Ad}\, G}$, the subspace of $\mathfrak{g}$ fixed by the adjoint action.

# Core Definition

**Definition 2.24** (Kirillov): A vector field is bi-invariant if it is both left- and right-invariant.

**Theorem 2.26**: The map $v \mapsto v(1)$ defines an isomorphism of bi-invariant vector fields on $G$ with $(T_1G)^{\mathrm{Ad}\, G} = \{x \in T_1G \mid \mathrm{Ad}\, g(x) = x \text{ for all } g \in G\}$.

# Prerequisites

- **Left-invariant vector field** — bi-invariance includes left-invariance
- **Adjoint action on Lie group** — the compatibility condition

# Key Properties

1. A left-invariant field is bi-invariant iff $x = v(1) \in (T_1G)^{\mathrm{Ad}\, G}$.
2. For semisimple groups with trivial center, the only bi-invariant vector field is zero.

# Construction / Recognition

## To Construct/Create:
1. Find $x \in \mathfrak{g}$ with $\mathrm{Ad}\, g(x) = x$ for all $g$.
2. Extend to a left-invariant (equivalently right-invariant) field.

## To Identify/Recognize:
1. Invariant under both left and right translations.

# Context & Application

Bi-invariant objects (vector fields, metrics, differential forms) are important in geometry. A similar result holds for bi-invariant differential forms.

# Examples

**Example**: For any abelian Lie group, all left-invariant vector fields are bi-invariant since the adjoint action is trivial.

**Example**: For $G = \mathrm{SU}(2)$, the center of $\mathfrak{su}(2)$ is trivial, so there are no nonzero bi-invariant vector fields.

# Relationships

## Builds Upon
- **Left-invariant vector field** — bi-invariance is a stronger condition
- **Adjoint action on Lie group** — determines which fields are bi-invariant

## Enables
- **Bi-invariant metrics** — similar characterization applies to metrics

## Related
- **Center of Lie algebra** — $\mathfrak{z}(\mathfrak{g}) \subset (T_1G)^{\mathrm{Ad}\, G}$

# Common Errors

- **Error**: Assuming every left-invariant vector field is bi-invariant.
  **Correction**: This only holds for abelian groups where the adjoint action is trivial.

# Common Confusions

- **Confusion**: Whether bi-invariant means the same as Ad-invariant.
  **Clarification**: For vector fields, yes: bi-invariance of $v$ is equivalent to $v(1)$ being Ad-invariant.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.4, Definition 2.24 and Theorem 2.26, page 14.

# Verification Notes

- Definition source: Direct from Definition 2.24 and Theorem 2.26
- Confidence rationale: Explicit theorem in source
- Uncertainties: None
- Cross-reference status: Verified
