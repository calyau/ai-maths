---
# === CORE IDENTIFICATION ===
concept: Kernel of a Homomorphism
slug: kernel-of-homomorphism

# === CLASSIFICATION ===
category: morphisms
subcategory: group-maps
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Homomorphisms"
chapter_number: 11
pdf_page: 148
section: "Group Homomorphisms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "ker phi"
  - "kernel"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-homomorphism
  - normal-subgroup
extends: []
related:
  - first-isomorphism-theorem
  - homomorphic-image
  - factor-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the kernel of a group homomorphism?"
  - "How does the kernel relate to injectivity?"
  - "How do normal subgroups relate to factor groups?"
---

# Quick Definition

The kernel of a group homomorphism $\phi: G \to H$ is the set $\ker\phi = \{g \in G : \phi(g) = e_H\}$ of elements mapping to the identity. It is always a normal subgroup of $G$.

# Core Definition

"Let $\phi: G \to H$ be a group homomorphism and suppose that $e$ is the identity of $H$. By Proposition 11.4, $\phi^{-1}(\{e\})$ is a subgroup of $G$. This subgroup is called the **kernel** of $\phi$ and will be denoted by $\ker\phi$" (Judson, p. 148). "In fact, this subgroup is a normal subgroup of $G$ since the trivial subgroup is normal in $H$" (Theorem 11.5).

# Prerequisites

- **Group homomorphism** — The kernel is defined for a homomorphism
- **Normal subgroup** — The kernel is always a normal subgroup

# Key Properties

1. $\ker\phi$ is always a normal subgroup of $G$ (Theorem 11.5)
2. $\phi$ is injective if and only if $\ker\phi = \{e\}$
3. Every normal subgroup is the kernel of some homomorphism (namely, the canonical homomorphism $G \to G/N$)
4. $G/\ker\phi \cong \phi(G)$ (First Isomorphism Theorem)
5. $\ker\phi$ determines the "fibers" of $\phi$: $\phi(g_1) = \phi(g_2)$ if and only if $g_1 \ker\phi = g_2 \ker\phi$

# Construction / Recognition

## To Compute the Kernel:
1. Identify the identity element $e_H$ in the codomain
2. Find all $g \in G$ such that $\phi(g) = e_H$
3. Verify this set forms a subgroup (it always does)

# Context & Application

The kernel is the central concept connecting homomorphisms and normal subgroups. The correspondence "every homomorphism gives a normal subgroup (its kernel)" and "every normal subgroup gives a homomorphism (the canonical map)" is fundamental to group theory.

# Examples

**Example 1** (p. 148): For $\phi: GL_2(\mathbb{R}) \to \mathbb{R}^*$ defined by $A \mapsto \det(A)$, the kernel is $SL_2(\mathbb{R})$, the matrices with determinant 1.

**Example 2** (p. 148): For $\phi: \mathbb{R} \to \mathbb{C}^*$ defined by $\phi(\theta) = \cos\theta + i\sin\theta$, the kernel is $\{2\pi n : n \in \mathbb{Z}\} \cong \mathbb{Z}$.

**Example 3** (p. 148): The only homomorphism from $\mathbb{Z}_7$ to $\mathbb{Z}_{12}$ is the trivial one (mapping everything to 0), because $\mathbb{Z}_{12}$ has no subgroup of order 7.

**Example 4** (p. 148): For $\phi: \mathbb{Z} \to G$ defined by $\phi(n) = g^n$: if $|g| = \infty$, then $\ker\phi = \{0\}$; if $|g| = n$, then $\ker\phi = n\mathbb{Z}$.

# Relationships

## Builds Upon
- **Group homomorphism** — The kernel is defined for a homomorphism
- **Normal subgroup** — The kernel is always a normal subgroup

## Enables
- **First isomorphism theorem** — $G/\ker\phi \cong \phi(G)$
- **Factor group** — $\ker\phi$ is the normal subgroup used to form $G/\ker\phi$

## Related
- **Homomorphic image** — Kernel and image together characterize the homomorphism

# Common Errors

- **Error**: Computing $\ker\phi$ by checking only generators of $G$
  **Correction**: While $\ker\phi$ is determined by the action on generators, one must verify that the full preimage of the identity is captured

# Common Confusions

- **Confusion**: Thinking the kernel is a subgroup of the codomain
  **Clarification**: $\ker\phi \subset G$ (domain), not $H$ (codomain)

# Source Reference

Chapter 11: Homomorphisms, Section 11.1, pages 148. Theorem 11.5 proves normality.

# Verification Notes

- Definition source: Direct quote from p. 148
- Confidence: HIGH — explicit definition with theorem
- Cross-reference status: Verified
