---
# === CORE IDENTIFICATION ===
concept: Hom Space as Representation
slug: hom-space-representation

# === CLASSIFICATION ===
category: representations
subcategory: operations
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 40
section: "4.2 Operations on representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Hom(V,W) representation"
  - "End(V) representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
  - tensor-product-of-representations
  - dual-representation
extends:
  - tensor-product-of-representations
related:
  - intertwining-operator
  - invariant-vectors
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a group act on the space of linear maps between two representations?"
---

# Quick Definition

The space $\mathrm{Hom}(V, W)$ of linear maps between representations $V$ and $W$ is itself a representation, with group action $g \cdot A = \rho_W(g) A \rho_V(g^{-1})$ and Lie algebra action $x \cdot A = \rho_W(x) A - A \rho_V(x)$.

# Core Definition

**Example 4.11** (Kirillov, p. 40): The space $\mathrm{Hom}(V, W) \cong W \otimes V^*$ between two representations is also a representation with action:

- Group: $g \cdot A = \rho_W(g) A \rho_V(g^{-1})$ for $g \in G$
- Lie algebra: $x \cdot A = \rho_W(x) A - A \rho_V(x)$ for $x \in \mathfrak{g}$

The special case $V = W$ gives $\mathrm{End}(V) \cong V \otimes V^*$.

# Prerequisites

- **Representation of a Lie group** — The source and target representations
- **Tensor product of representations** — $\mathrm{Hom}(V,W) \cong W \otimes V^*$
- **Dual representation** — $V^*$ appears in the identification

# Key Properties

1. $\mathrm{Hom}(V, W)^G = \mathrm{Hom}_G(V, W)$: invariants are intertwining operators (Example 4.13)
2. $\dim \mathrm{Hom}(V, W) = \dim V \cdot \dim W$
3. For irreducible $V \ncong W$: $\mathrm{Hom}_G(V,W) = 0$ (Schur's lemma)
4. For irreducible $V$: $\mathrm{Hom}_G(V,V) = \mathbb{C} \cdot \mathrm{id}$ (Schur's lemma)

# Construction / Recognition

## To Construct:
1. Take the vector space of all linear maps $V \to W$
2. Define the action: $(g \cdot A)(v) = g \cdot (A(g^{-1} \cdot v))$
3. For Lie algebras: $(x \cdot A)(v) = x \cdot (A(v)) - A(x \cdot v)$

# Context & Application

This construction is crucial for understanding intertwining operators as invariant elements and for applying Schur's lemma. In physics, observables that commute with the symmetry group are elements of $\mathrm{End}(V)^G$.

# Examples

**Example 4.11** (p. 40): $\mathrm{End}(V) \cong V \otimes V^*$ with action $g: A \mapsto \rho(g)A\rho(g^{-1})$.

**Example 4.13** (p. 41): $V^G = \mathrm{Hom}_G(\mathbb{C}, V)$, showing invariant vectors are the intertwiners from the trivial representation.

# Relationships

## Builds Upon
- **Tensor product** and **dual representation** — $\mathrm{Hom}(V,W) \cong W \otimes V^*$

## Enables
- **Schur's lemma** — Characterizes $\mathrm{Hom}_G(V,W)$ for irreducibles

## Related
- **Intertwining operator** — Elements of $\mathrm{Hom}(V,W)^G$

# Common Errors

- **Error**: Writing the Lie algebra action as $x \cdot A = \rho(x) \circ A$ instead of $\rho_W(x) A - A \rho_V(x)$.
  **Correction**: Both terms are needed; this is the commutator action.

# Source Reference

Chapter 4, Section 4.2, Example 4.11, p. 40; Example 4.13, p. 41.

# Verification Notes

- Definition source: Direct from Example 4.11, p. 40
- Confidence rationale: Explicit formula given
- Uncertainties: None
- Cross-reference status: Verified
