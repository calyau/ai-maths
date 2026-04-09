---
# === CORE IDENTIFICATION ===
concept: Fiber Bundle (Lie Group Context)
slug: fiber-bundle

# === CLASSIFICATION ===
category: lie-groups
subcategory: homogeneous-spaces
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 10
section: "2.1"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "principal bundle"
  - "locally trivial fibration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - lie-subgroup
  - coset-space
extends: []
related:
  - homogeneous-space
  - homotopy-exact-sequence
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
---

# Quick Definition

In the context of Lie groups, a fiber bundle structure arises naturally from the projection $G \to G/H$, where $G$ is a Lie group and $H$ is a Lie subgroup. Locally, $G$ looks like a product of $G/H$ and $H$.

# Core Definition

**Theorem 2.10** (Kirillov): The canonical map $p: G \to G/H$ is a fiber bundle, with fiber diffeomorphic to $H$. This means that locally, $G$ is diffeomorphic to $(G/H) \times H$.

The associated long exact sequence of homotopy groups (Corollary 2.11) gives:
$$\pi_2(G/H) \to \pi_1(H) \to \pi_1(G) \to \pi_1(G/H) \to \{1\}$$

# Prerequisites

- **Lie group** — the total space
- **Lie subgroup** — the fiber
- **Coset space** — the base space

# Key Properties

1. The projection $p: G \to G/H$ is locally trivial.
2. The fiber over each point is diffeomorphic to $H$.
3. If $H$ is connected, $\pi_0(G) = \pi_0(G/H)$.
4. The long exact sequence of homotopy groups relates the topology of $G$, $H$, and $G/H$.

# Construction / Recognition

## To Construct/Create:
1. Take a Lie group $G$ and Lie subgroup $H$.
2. The projection $p: G \to G/H$ automatically has fiber bundle structure.

## To Identify/Recognize:
1. A surjective smooth map whose fibers are all diffeomorphic and which is locally trivial.

# Context & Application

Fiber bundles from Lie group quotients are used extensively to compute topological invariants ($\pi_0$, $\pi_1$) of classical groups by induction on dimension.

# Examples

**Example 2.22** (p. 12): The fiber bundle $\mathrm{SO}(n-1, \mathbb{R}) \to \mathrm{SO}(n, \mathbb{R}) \to S^{n-1}$ and $\mathrm{SU}(n-1) \to \mathrm{SU}(n) \to S^{2n-1}$.

**Example** (p. 18, Exercise 2.8): These fiber bundles are used to prove by induction that $\mathrm{SU}(n)$ is simply-connected and $\pi_1(\mathrm{U}(n)) = \mathbb{Z}$.

# Relationships

## Builds Upon
- **Coset space** — the base of the fiber bundle
- **Lie subgroup** — the fiber

## Enables
- **Homotopy exact sequence** — computing $\pi_0$, $\pi_1$ of classical groups
- **Topological classification of classical groups** — the tables on pp. 16-17

## Related
- **Homogeneous space** — homogeneous spaces give rise to fiber bundles via $H \to G \to G/H$

# Common Errors

- **Error**: Assuming the fiber bundle is globally trivial (i.e., $G \cong (G/H) \times H$).
  **Correction**: The bundle is only locally trivial. For example, $\mathrm{SO}(3, \mathbb{R}) \to S^2$ is not globally trivial.

# Common Confusions

- **Confusion**: Conflating the fiber bundle $G \to G/H$ with a general fiber bundle.
  **Clarification**: These are specifically principal $H$-bundles with a right $H$-action on the total space $G$.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.1, Theorem 2.10 and Corollary 2.11, pages 10-11.

# Verification Notes

- Definition source: Synthesized from Theorem 2.10 and Corollary 2.11
- Confidence rationale: The fiber bundle concept is used but not independently defined; it arises from the coset space theorem
- Uncertainties: None significant
- Cross-reference status: Verified with Example 2.22, Exercise 2.8
