---
# === CORE IDENTIFICATION ===
concept: Invariant Vectors
slug: invariant-vectors

# === CLASSIFICATION ===
category: representations
subcategory: operations
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 41
section: "4.2 Operations on representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "fixed vectors"
  - "G-invariant vectors"
  - "g-invariant vectors"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-of-lie-group
extends: []
related:
  - trivial-representation
  - intertwining-operator
  - invariant-bilinear-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are invariant vectors in a representation?"
  - "How do invariant vectors relate to the trivial representation?"
---

# Quick Definition

An invariant vector in a representation $V$ of $G$ is a vector $v$ satisfying $\rho(g)v = v$ for all $g \in G$; for a Lie algebra, $\rho(x)v = 0$ for all $x \in \mathfrak{g}$.

# Core Definition

**Definition 4.12** (Kirillov, p. 41): Let $V$ be a representation of a Lie group $G$. A vector $v \in V$ is called invariant if $\rho(g)v = v$ for all $g \in G$. The subspace of invariant vectors is denoted $V^G$.

Similarly, for a Lie algebra $\mathfrak{g}$, a vector $v \in V$ is invariant if $\rho(x)v = 0$ for all $x \in \mathfrak{g}$. The subspace is denoted $V^{\mathfrak{g}}$.

For a connected Lie group $G$ with Lie algebra $\mathfrak{g}$, $V^G = V^{\mathfrak{g}}$.

# Prerequisites

- **Representation of a Lie group** — The representation containing invariant vectors

# Key Properties

1. $V^G$ is a subrepresentation (it is the trivial subrepresentation)
2. $V^G = \mathrm{Hom}_G(\mathbb{C}, V)$ where $\mathbb{C}$ is the trivial representation (Example 4.13)
3. $(\mathrm{Hom}(V, W))^G = \mathrm{Hom}_G(V, W)$: invariants of Hom space are intertwiners (Example 4.13)
4. For connected $G$: $V^G = V^{\mathfrak{g}}$

# Construction / Recognition

## To Identify:
1. For groups: solve $\rho(g)v = v$ for all $g \in G$
2. For Lie algebras: solve $\rho(x)v = 0$ for all $x \in \mathfrak{g}$ (a linear system)
3. It suffices to check generators of $G$ or a basis of $\mathfrak{g}$

# Context & Application

Invariant vectors are the simplest objects in a representation. Finding invariants is equivalent to finding copies of the trivial representation. In physics, invariant vectors correspond to quantities preserved by symmetry. The multiplicity of the trivial representation in $V$ equals $\dim V^G$.

# Examples

**Example 4.13** (p. 41): Invariant elements in $\mathrm{Hom}(V, W)$ are exactly the intertwining operators $\mathrm{Hom}_G(V, W)$.

**Example 4.14** (p. 41): A bilinear form $B$ on $V$ is $G$-invariant iff $B(gv, gw) = B(v,w)$ for all $g \in G$; equivalently for $\mathfrak{g}$: $B(x \cdot v, w) + B(v, x \cdot w) = 0$.

# Relationships

## Builds Upon
- **Representation of a Lie group** — Invariants are a fundamental property of representations

## Enables
- **Intertwining operators** — Intertwiners are invariants of Hom spaces
- **Invariant bilinear forms** — Special case of invariants

## Related
- **Trivial representation** — Copies of the trivial rep in $V$ correspond to $V^G$

# Common Confusions

- **Confusion**: Thinking $V^G = 0$ means there are no "interesting" structures.
  **Clarification**: Even when $V^G = 0$, the representation may have rich structure. Invariants of related spaces (like $V \otimes V^*$) may be non-trivial.

# Source Reference

Chapter 4, Section 4.2, Definition 4.12, Examples 4.13-4.14, p. 41.

# Verification Notes

- Definition source: Direct from Definition 4.12, p. 41
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
