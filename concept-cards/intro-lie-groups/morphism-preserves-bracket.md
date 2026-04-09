---
# === CORE IDENTIFICATION ===
concept: Morphisms Preserve the Commutator
slug: morphism-preserves-bracket

# === CLASSIFICATION ===
category: lie-algebras
subcategory: definitions
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 23
section: "3.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Proposition 3.12"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group-morphism
  - commutator-bracket
  - exponential-map
extends: []
related:
  - lie-algebra-morphism
  - lie-functor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

Every morphism of Lie groups $\varphi: G_1 \to G_2$ induces a linear map $\varphi_*: \mathfrak{g}_1 \to \mathfrak{g}_2$ that preserves the bracket: $\varphi_*[x, y] = [\varphi_* x, \varphi_* y]$.

# Core Definition

**Proposition 3.12, part (1)** (Kirillov): For any morphism of Lie groups $\varphi: G_1 \to G_2$, the corresponding map of Lie algebras preserves the commutator: $\varphi_*[x, y] = [\varphi_* x, \varphi_* y]$ for any $x, y \in \mathfrak{g}_1$.

# Prerequisites

- **Lie group morphism** — the group-level map
- **Commutator bracket** — the bracket being preserved
- **Exponential map** — used in the proof

# Key Properties

1. Follows immediately from the definition of the bracket via equation (3.2) and the fact that $\varphi$ commutes with exp (Theorem 3.7 part 4).
2. As a special case: $\mathrm{Ad}\, g$ preserves the bracket (Proposition 3.12 part 2).
3. This is the key property that makes $G \mapsto \mathrm{Lie}(G)$ a functor.

# Construction / Recognition

## To Construct/Create:
1. Given $\varphi: G_1 \to G_2$, take $\varphi_* = d\varphi|_1: T_1G_1 \to T_1G_2$.
2. Verify bracket preservation follows automatically from Theorem 3.7.

## To Identify/Recognize:
1. The induced map on Lie algebras from any Lie group morphism.

# Context & Application

This proposition is what makes the Lie algebra functor well-defined. It ensures that the algebraic structure (bracket) is respected by the passage from groups to algebras.

# Examples

**Example** (p. 23): $\mathrm{Ad}\, g$ is a group automorphism of $G$, so $(\mathrm{Ad}\, g)_*$ preserves the bracket: $\mathrm{Ad}\, g([x,y]) = [\mathrm{Ad}\, g . x, \mathrm{Ad}\, g . y]$.

# Relationships

## Builds Upon
- **Lie group morphism** — the map inducing the algebra morphism
- **Commutator bracket** — the structure being preserved

## Enables
- **Lie functor** — sends morphisms to bracket-preserving maps
- **Theorem 3.17** — summary of the group-algebra correspondence

## Related
- **Lie algebra morphism** — what $\varphi_*$ is

# Common Errors

- **Error**: Assuming the converse — that every bracket-preserving map lifts to a group morphism.
  **Correction**: This requires $G_1$ to be simply connected (Theorem 3.38).

# Common Confusions

- **Confusion**: Whether the bracket preservation is a condition or a consequence.
  **Clarification**: It is automatic (a consequence of the definitions). Every smooth group homomorphism automatically induces a bracket-preserving linear map.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.2, Proposition 3.12, page 23.

# Verification Notes

- Definition source: Direct from Proposition 3.12 part (1)
- Confidence rationale: Explicit proposition with proof
- Uncertainties: None
- Cross-reference status: Verified with Theorem 3.7, Theorem 3.17
