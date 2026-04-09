---
# === CORE IDENTIFICATION ===
concept: Orbit
slug: orbit

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
  - "G-orbit"
  - "$\\mathcal{O}_m$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action-on-manifold
extends: []
related:
  - stabilizer-subgroup
  - homogeneous-space
  - coset-space
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie group?"
---

# Quick Definition

The orbit of a point $m \in M$ under a Lie group action is the set $\mathcal{O}_m = G \cdot m = \{g.m \mid g \in G\}$ of all points reachable from $m$ by the group action.

# Core Definition

(Kirillov, p. 12): Let $G$ act on a manifold $M$. For every point $m \in M$, the orbit is $\mathcal{O}_m = G m = \{g.m \mid g \in G\}$.

**Corollary 2.19**: The orbit $\mathcal{O}_m$ is an immersed submanifold in $M$, with tangent space $T_m\mathcal{O}_m = T_1G/T_1H$ where $H = \mathrm{Stab}(m)$. If $\mathcal{O}_m$ is closed, then $g \mapsto g.m$ is a diffeomorphism $G/\mathrm{Stab}(m) \xrightarrow{\sim} \mathcal{O}_m$.

# Prerequisites

- **Group action on a manifold** — orbits are defined via group actions

# Key Properties

1. The orbit is in natural bijection with $G/\mathrm{Stab}(m)$ (Lemma 2.18).
2. The orbit is an immersed submanifold of $M$.
3. If the orbit is closed, it is diffeomorphic to $G/\mathrm{Stab}(m)$.
4. $\dim \mathcal{O}_m = \dim G - \dim \mathrm{Stab}(m)$.

# Construction / Recognition

## To Construct/Create:
1. Choose a point $m \in M$.
2. Apply all group elements: $\mathcal{O}_m = \{g.m \mid g \in G\}$.

## To Identify/Recognize:
1. A subset of $M$ that is closed under the group action and minimal (i.e., any point can reach any other).

# Context & Application

Orbits partition $M$ into equivalence classes. The structure of orbits and stabilizers is fundamental to understanding group actions.

# Examples

**Example** (p. 12): The action of $\mathrm{SO}(n, \mathbb{R})$ on $\mathbb{R}^n$ has orbits that are spheres $S^{n-1}_r$ of radius $r$, plus the origin.

**Example** (p. 13): $\mathrm{GL}(n, \mathbb{C})$ acts on $n \times n$ matrices by conjugation; orbits are similarity classes (Jordan normal form).

# Relationships

## Builds Upon
- **Group action on a manifold** — orbits arise from group actions

## Enables
- **Homogeneous space** — a space with a single orbit

## Related
- **Stabilizer subgroup** — the subgroup fixing a point; $\mathcal{O}_m \cong G/\mathrm{Stab}(m)$
- **Coset space** — orbits are diffeomorphic to coset spaces

# Common Errors

- **Error**: Assuming all orbits have the same dimension.
  **Correction**: Orbit dimension equals $\dim G - \dim \mathrm{Stab}(m)$, and stabilizers can vary.

# Common Confusions

- **Confusion**: Confusing the orbit space $M/G$ with a coset space $G/H$.
  **Clarification**: The orbit space $M/G$ is the set of all orbits and can be very singular. A coset space $G/H$ is always a smooth manifold.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.3, pages 12-13. Lemma 2.18, Corollary 2.19.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Explicit definition with theorem on structure
- Uncertainties: None
- Cross-reference status: Verified with Lemma 2.18, Corollary 2.19
