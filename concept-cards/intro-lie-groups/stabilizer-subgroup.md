---
# === CORE IDENTIFICATION ===
concept: Stabilizer Subgroup
slug: stabilizer-subgroup

# === CLASSIFICATION ===
category: lie-groups
subcategory: group-actions
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 12
section: "2.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "isotropy subgroup"
  - "little group"
  - "$\\mathrm{Stab}_G(m)$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action-on-manifold
  - lie-subgroup
extends: []
related:
  - orbit
  - homogeneous-space
  - stabilizer-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie group?"
  - "How do I compute the Lie algebra of a matrix Lie group?"
---

# Quick Definition

The stabilizer (or isotropy subgroup) of a point $m \in M$ under the action of $G$ is $\mathrm{Stab}_G(m) = \{g \in G \mid g.m = m\}$, the subgroup of elements that fix $m$.

# Core Definition

**Lemma 2.18** (Kirillov): Let $M$ be a manifold with an action of $G$. Choose a point $m \in M$ and let $H = \mathrm{Stab}_G(m) = \{g \in G \mid g.m = m\}$. Then $H$ is a Lie subgroup in $G$, and $g \mapsto g.m$ is an injective immersion $G/H \hookrightarrow M$ whose image coincides with the orbit $\mathcal{O}_m$.

**Theorem 3.26** provides the Lie algebra: $\mathfrak{h} = \{x \in \mathfrak{g} \mid \rho_*(x)(m) = 0\}$.

# Prerequisites

- **Group action on a manifold** — stabilizers are defined in terms of actions
- **Lie subgroup** — the stabilizer is always a Lie subgroup

# Key Properties

1. The stabilizer is always a closed subgroup, hence a Lie subgroup (Theorem 2.8).
2. The orbit-stabilizer relation: $\mathcal{O}_m \cong G/\mathrm{Stab}(m)$.
3. The Lie algebra of the stabilizer is $\{x \in \mathfrak{g} \mid \rho_*(x)(m) = 0\}$ (Theorem 3.26).
4. The tangent space to the orbit is $T_m\mathcal{O}_m = \mathfrak{g}/\mathfrak{h}$.

# Construction / Recognition

## To Construct/Create:
1. Given an action of $G$ on $M$ and a point $m$, collect all $g \in G$ with $g.m = m$.

## To Identify/Recognize:
1. The subgroup of $G$ that leaves $m$ fixed.

# Context & Application

Stabilizers are essential for understanding the geometry of group actions. Many important Lie groups arise as stabilizers (e.g., $\mathrm{O}(n)$ stabilizes the standard bilinear form, $\mathrm{SO}(n-1)$ stabilizes a point on $S^{n-1}$).

# Examples

**Example 2.22** (p. 12): For $\mathrm{SO}(n, \mathbb{R})$ acting on $S^{n-1}$, the stabilizer of $e_n = (0, \ldots, 0, 1)$ is $\mathrm{SO}(n-1, \mathbb{R})$.

**Example 2.23** (p. 13): For $\mathrm{GL}(n, \mathbb{R})$ acting on the flag manifold $\mathcal{B}_n(\mathbb{R})$, the stabilizer of the standard flag is the group $B(n, \mathbb{R})$ of invertible upper-triangular matrices.

# Relationships

## Builds Upon
- **Group action on a manifold** — stabilizers arise from actions
- **Lie subgroup** — stabilizers are Lie subgroups

## Enables
- **Homogeneous space** — $G/\mathrm{Stab}(m)$ is a homogeneous space
- **Stabilizer Lie algebra** — the infinitesimal version

## Related
- **Orbit** — $\mathcal{O}_m \cong G/\mathrm{Stab}(m)$

# Common Errors

- **Error**: Assuming the stabilizer is always trivial.
  **Correction**: The stabilizer can be any Lie subgroup. It is trivial only when the action is free.

# Common Confusions

- **Confusion**: Confusing the stabilizer of a point with the kernel of the action.
  **Clarification**: The kernel is $\{g \in G \mid g.m = m \text{ for all } m\}$; the stabilizer is $\{g \in G \mid g.m_0 = m_0\}$ for a specific $m_0$.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.3, Lemma 2.18, page 12. Also Theorem 3.26, page 27.

# Verification Notes

- Definition source: Direct from Lemma 2.18
- Confidence rationale: Explicit definition with proof reference
- Uncertainties: None
- Cross-reference status: Verified with Theorem 3.26, Examples 2.22, 2.23
