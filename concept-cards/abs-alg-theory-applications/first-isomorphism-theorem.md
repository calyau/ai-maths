---
# === CORE IDENTIFICATION ===
concept: First Isomorphism Theorem
slug: first-isomorphism-theorem

# === CLASSIFICATION ===
category: morphisms
subcategory: isomorphism-theorems
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Homomorphisms"
chapter_number: 11
pdf_page: 148
section: "The Isomorphism Theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "fundamental homomorphism theorem"
  - "first isomorphism theorem for groups"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-homomorphism
  - kernel-of-homomorphism
  - factor-group
  - canonical-homomorphism
extends: []
related:
  - second-isomorphism-theorem
  - third-isomorphism-theorem
  - correspondence-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do homomorphisms relate to isomorphisms?"
  - "How do normal subgroups relate to factor groups?"
  - "What is the First Isomorphism Theorem?"
---

# Quick Definition

The First Isomorphism Theorem states that if $\psi: G \to H$ is a group homomorphism with kernel $K$, then $K$ is normal in $G$ and $G/K \cong \psi(G)$. Every homomorphism factors through its kernel's quotient.

# Core Definition

**Theorem 11.10 (First Isomorphism Theorem)**: "If $\psi: G \to H$ is a group homomorphism with $K = \ker\psi$, then $K$ is normal in $G$. Let $\phi: G \to G/K$ be the canonical homomorphism. Then there exists a unique isomorphism $\eta: G/K \to \psi(G)$ such that $\psi = \eta\phi$" (Judson, p. 149).

# Prerequisites

- **Group homomorphism** — The theorem applies to any homomorphism
- **Kernel of homomorphism** — The kernel $K$ forms the quotient
- **Factor group** — $G/K$ must be formed
- **Canonical homomorphism** — The natural map $\phi: G \to G/K$

# Key Properties

1. $K = \ker\psi$ is normal in $G$
2. The isomorphism $\eta: G/K \to \psi(G)$ is given by $\eta(gK) = \psi(g)$
3. $\eta$ is well-defined: if $g_1 K = g_2 K$, then $\psi(g_1) = \psi(g_2)$
4. The diagram commutes: $\psi = \eta \circ \phi$
5. $\eta$ is the unique isomorphism making the diagram commute

# Construction / Recognition

## To Apply the First Isomorphism Theorem:
1. Identify a homomorphism $\psi: G \to H$
2. Compute $K = \ker\psi$
3. Determine $\psi(G)$ (the image)
4. Conclude $G/K \cong \psi(G)$
5. The isomorphism is $gK \mapsto \psi(g)$

# Context & Application

The First Isomorphism Theorem is one of the most important results in group theory. It says that factor groups and homomorphic images are the same thing. Every homomorphism naturally factors as a surjection onto a quotient followed by an isomorphism into the codomain.

# Examples

**Example 1** (p. 149): Let $G$ be cyclic with generator $g$, and $\phi: \mathbb{Z} \to G$ by $n \mapsto g^n$. If $|g| = m$, then $\ker\phi = m\mathbb{Z}$ and $\mathbb{Z}/m\mathbb{Z} \cong G$. If $|g| = \infty$, then $\ker\phi = \{0\}$ and $\mathbb{Z} \cong G$. This shows two cyclic groups are isomorphic exactly when they have the same order.

**Example 2**: The determinant $\det: GL_n(\mathbb{R}) \to \mathbb{R}^*$ has kernel $SL_n(\mathbb{R})$, so $GL_n(\mathbb{R})/SL_n(\mathbb{R}) \cong \mathbb{R}^*$.

# Relationships

## Builds Upon
- **Group homomorphism** — The input to the theorem
- **Kernel of homomorphism** — Forms the quotient
- **Factor group** — $G/K$ appears in the conclusion
- **Canonical homomorphism** — Part of the factorization

## Enables
- **Second isomorphism theorem** — Uses the First Isomorphism Theorem in its proof
- **Third isomorphism theorem** — Built on the First

## Related
- **Correspondence theorem** — Another consequence of the isomorphism theory

# Common Errors

- **Error**: Applying the theorem without verifying the map is a homomorphism
  **Correction**: The theorem only applies to group homomorphisms; verify the homomorphism property first

# Common Confusions

- **Confusion**: Thinking the theorem says $G/K \cong H$ (the full codomain)
  **Clarification**: The isomorphism is $G/K \cong \psi(G)$ (the image), not the full codomain unless $\psi$ is surjective

# Source Reference

Chapter 11: Homomorphisms, Section 11.2, pages 149. Theorem 11.10.

# Verification Notes

- Definition source: Direct quote of Theorem 11.10
- Proof: Complete proof in source
- Confidence: HIGH — major theorem with full proof
- Cross-reference status: Verified
