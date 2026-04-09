---
# === CORE IDENTIFICATION ===
concept: Center of a Lie Group
slug: center-of-lie-group

# === CLASSIFICATION ===
category: lie-groups
subcategory: subgroups
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 28
section: "3.6"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$Z(G)$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - adjoint-action-on-lie-algebra
extends: []
related:
  - center-of-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

For a connected Lie group $G$, the center $Z(G) = \{g \in G \mid gh = hg \;\forall h \in G\}$ is a Lie subgroup with Lie algebra $\mathfrak{z}(\mathfrak{g})$, the center of the Lie algebra.

# Core Definition

**Theorem 3.32** (Kirillov): Let $G$ be a connected Lie group. Then its center $Z(G)$ is a Lie subgroup with Lie algebra $\mathfrak{z}(\mathfrak{g})$.

Proof: $Z(G) = \mathrm{Ker}(\mathrm{Ad})$ where $\mathrm{Ad}: G \to \mathrm{GL}(\mathfrak{g})$, and the result follows from Corollary 3.27.

# Prerequisites

- **Lie group** — the group
- **Adjoint representation (Ad)** — $Z(G) = \mathrm{Ker}(\mathrm{Ad})$

# Key Properties

1. $Z(G) = \mathrm{Ker}(\mathrm{Ad}: G \to \mathrm{GL}(\mathfrak{g}))$.
2. $\mathrm{Lie}(Z(G)) = \mathfrak{z}(\mathfrak{g})$.
3. The center is always a normal (even central) Lie subgroup.
4. Discrete central subgroups arise as kernels of covering maps (Theorem 2.5).

# Construction / Recognition

## To Construct/Create:
1. Compute the kernel of Ad.
2. Equivalently, find all $g$ commuting with every element of $G$.

## To Identify/Recognize:
1. The subgroup of elements commuting with everything.

# Context & Application

The center is crucial for the classification of connected Lie groups with a given Lie algebra: any connected group is the simply-connected cover quotiented by a discrete central subgroup (Corollary 3.49).

# Examples

**Example**: $Z(\mathrm{SU}(2)) = \{\pm I\} \cong \mathbb{Z}_2$.

**Example**: $Z(\mathrm{GL}(n, \mathbb{K})) = \{aI \mid a \in \mathbb{K}^*\}$ (scalar matrices).

**Example**: $Z(\mathrm{SO}(3, \mathbb{R})) = \{I\}$ (trivial center).

# Relationships

## Builds Upon
- **Adjoint representation (Ad)** — $Z(G) = \mathrm{Ker}(\mathrm{Ad})$

## Enables
- **Classification of groups with given Lie algebra** — via discrete central subgroups

## Related
- **Center of Lie algebra** — $\mathfrak{z}(\mathfrak{g}) = \mathrm{Lie}(Z(G))$

# Common Errors

- **Error**: Assuming $Z(G)$ is always connected.
  **Correction**: $Z(G)$ can be disconnected. For example, $Z(\mathrm{SU}(n)) = \{e^{2\pi i k/n} I\} \cong \mathbb{Z}_n$ is finite.

# Common Confusions

- **Confusion**: Whether $\mathfrak{z}(\mathfrak{g}) = 0$ implies $Z(G) = \{1\}$.
  **Clarification**: Not necessarily. $Z(G)$ can be a nontrivial discrete group even when $\mathfrak{z}(\mathfrak{g}) = 0$.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.6, Theorem 3.32, page 28.

# Verification Notes

- Definition source: Direct from Theorem 3.32
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified with Corollary 3.27, Corollary 3.49
