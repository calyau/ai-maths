---
# === CORE IDENTIFICATION ===
concept: Representations of Commutative Groups
slug: representations-of-commutative-groups

# === CLASSIFICATION ===
category: representations
subcategory: irreducibility
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 44
section: "4.4 Intertwining operators and Schur lemma"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - schur-lemma
  - irreducible-representation
extends:
  - schur-lemma
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the irreducible representations of a commutative group?"
---

# Quick Definition

Every irreducible complex representation of a commutative group (or Lie algebra) is one-dimensional. This follows immediately from Schur's lemma.

# Core Definition

**Proposition 4.25** (Kirillov, p. 44): If $G$ is a commutative group, then any irreducible complex representation of $G$ is one-dimensional. Similarly for commutative Lie algebras.

**Proof**: Since $G$ is commutative, every $\rho(g)$ commutes with the action of $G$, so by Schur's lemma $\rho(g) = \lambda(g)\,\mathrm{id}$. Hence every subspace is invariant, so irreducibility forces $\dim V = 1$.

# Prerequisites

- **Schur's lemma** — The key tool
- **Irreducible representation** — The objects being classified

# Key Properties

1. Classification reduces to finding characters: $\rho: G \to \mathbb{C}^\times$
2. For $G = \mathbb{R}$: irreducibles are $V_\lambda$ ($\lambda \in \mathbb{C}$) with $\rho(a) = e^{\lambda a}$ (Example 4.26)
3. For $G = S^1 = \mathbb{R}/\mathbb{Z}$: irreducibles are $V_k$ ($k \in \mathbb{Z}$) with $\rho(a) = e^{2\pi ika}$ (Example 4.26)
4. Not every representation is completely reducible (Example 4.18: Jordan blocks for $\mathbb{R}$)

# Examples

**Example 4.26** (p. 44): Irreducible representations of $\mathbb{R}$ are $V_\lambda$, $\lambda \in \mathbb{C}$, with $\rho(a) = e^{\lambda a}$. Those of $S^1$ are $V_k$, $k \in \mathbb{Z}$, with $\rho(a) = e^{2\pi ika}$ (or equivalently, $z \mapsto z^k$ for $z \in S^1 \subset \mathbb{C}$).

# Relationships

## Builds Upon
- **Schur's lemma** — Implies all operators are scalar

# Source Reference

Chapter 4, Section 4.4, Proposition 4.25, Example 4.26, p. 44.

# Verification Notes

- Definition source: Direct from Proposition 4.25
- Confidence rationale: Explicit proposition with proof
- Uncertainties: None
- Cross-reference status: Verified
