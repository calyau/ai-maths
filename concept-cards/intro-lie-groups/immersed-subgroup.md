---
# === CORE IDENTIFICATION ===
concept: Immersed Subgroup
slug: immersed-subgroup

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
pdf_page: 30
section: "3.8"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "analytic subgroup"
  - "virtual Lie subgroup"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - lie-subgroup
extends:
  - lie-subgroup
related:
  - lie-subalgebra
  - second-fundamental-theorem-of-lie-theory
contrasts_with:
  - lie-subgroup

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
  - "What must I know before studying the structure theory of Lie algebras?"
---

# Quick Definition

An immersed subgroup of a Lie group $G$ is a subgroup $H \subset G$ that is also an immersed submanifold — it can be given a manifold topology (possibly different from the subspace topology) making the inclusion an immersion.

# Core Definition

**Definition 3.39** (Kirillov): An immersed subgroup in a Lie group $G$ is a subset $H \subset G$ such that (1) $H$ is a subgroup of $G$, and (2) $H$ is an immersed submanifold: $H = \mathrm{Im}(i)$ for some injective immersion $i: \tilde{H} \hookrightarrow G$.

# Prerequisites

- **Lie group** — the ambient group
- **Lie subgroup** — the stricter notion that immersed subgroups generalize

# Key Properties

1. The topology on $\tilde{H}$ may differ from the subspace topology inherited from $G$.
2. $\tilde{H}$ is itself a Lie group and $i$ is a morphism of Lie groups (Proposition 3.42).
3. $\mathfrak{h} = i_*(T_1\tilde{H})$ is a Lie subalgebra of $\mathfrak{g}$ (Proposition 3.42).
4. If $H = i(\tilde{H})$ is closed in $G$, then $H$ is actually a Lie subgroup (Proposition 3.42).
5. There is a bijection between connected immersed subgroups and Lie subalgebras (Theorem 3.43).

# Construction / Recognition

## To Construct/Create:
1. Given a Lie subalgebra $\mathfrak{h} \subset \mathfrak{g}$, the corresponding immersed subgroup is the maximal connected integral manifold of the distribution $\mathcal{D}^{\mathfrak{h}}_p = \mathfrak{h} \cdot p$ (from the proof of Theorem 3.43).
2. Concretely: $H = \{\exp(x_1) \cdots \exp(x_n) \mid x_i \in \mathfrak{h}\}$.

## To Identify/Recognize:
1. A subgroup that is the image of an injective immersion from another Lie group.

# Context & Application

Immersed subgroups are needed to establish the bijection between Lie subalgebras and connected subgroups (Theorem 3.43). Without this generalization, not every Lie subalgebra would correspond to a subgroup.

# Examples

**Example 3.37** (p. 30): Let $G = T^2 = \mathbb{R}^2/\mathbb{Z}^2$ and $\mathfrak{h} = \{(t, \alpha t) \mid t \in \mathbb{R}\}$ for irrational $\alpha$. The corresponding immersed subgroup is the irrational winding on the torus — dense in $T^2$ but not a Lie subgroup.

**Example 3.41** (p. 31): If $\varphi: G_1 \to G_2$ is a morphism with injective $\varphi_*$, then $\varphi(G_1)$ is an immersed subgroup. Every one-parameter subgroup is an immersed subgroup.

# Relationships

## Builds Upon
- **Lie subgroup** — immersed subgroups generalize Lie subgroups

## Enables
- **Second fundamental theorem of Lie theory** — bijection between subalgebras and connected immersed subgroups

## Related
- **Lie subalgebra** — each immersed subgroup has a Lie subalgebra

## Contrasts With
- **Lie subgroup** — a Lie subgroup is an embedded (closed) submanifold; an immersed subgroup may not be closed

# Common Errors

- **Error**: Expecting every subalgebra to correspond to a closed (Lie) subgroup.
  **Correction**: The irrational winding on the torus shows this fails; one needs immersed subgroups.

# Common Confusions

- **Confusion**: Terminology varies across books — some call immersed subgroups "Lie subgroups" or "analytic subgroups."
  **Clarification**: Kirillov reserves "Lie subgroup" for the embedded (closed) case and uses "immersed subgroup" for the more general notion.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.8, Definition 3.39 and Proposition 3.42, pages 30-31.

# Verification Notes

- Definition source: Direct from Definition 3.39
- Confidence rationale: Explicit definition with examples in source
- Uncertainties: None
- Cross-reference status: Verified with Examples 3.37, 3.41, Proposition 3.42, Theorem 3.43
