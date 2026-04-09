---
# === CORE IDENTIFICATION ===
concept: Group Action on a Manifold
slug: group-action-on-manifold

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
pdf_page: 11
section: "2.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Lie group action"
  - "smooth group action"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
extends: []
related:
  - representation-of-lie-group
  - orbit
  - stabilizer-subgroup
  - homogeneous-space
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie group?"
---

# Quick Definition

An action of a Lie group $G$ on a manifold $M$ is a smooth assignment of a diffeomorphism $\rho(g) \in \mathrm{Diff}(M)$ to each $g \in G$, compatible with the group structure.

# Core Definition

**Definition 2.14** (Kirillov): An action of a Lie group $G$ on a manifold $M$ is an assignment to each $g \in G$ a diffeomorphism $\rho(g) \in \mathrm{Diff}(M)$ such that $\rho(1) = \mathrm{id}$, $\rho(gh) = \rho(g)\rho(h)$ and such that the map $G \times M \to M: (g, m) \mapsto \rho(g).m$ is a smooth map.

# Prerequisites

- **Lie group** — the group acting

# Key Properties

1. Each $\rho(g)$ is a diffeomorphism of $M$.
2. The map $\rho: G \to \mathrm{Diff}(M)$ is a group homomorphism.
3. The joint map $G \times M \to M$ is smooth.
4. Any action induces representations on $C^\infty(M)$, $\mathrm{Vect}(M)$, differential forms, etc.

# Construction / Recognition

## To Construct/Create:
1. Define a map $\rho: G \to \mathrm{Diff}(M)$ satisfying $\rho(1) = \mathrm{id}$ and $\rho(gh) = \rho(g)\rho(h)$.
2. Verify the joint smoothness of $G \times M \to M$.

## To Identify/Recognize:
1. A smooth map $G \times M \to M$ satisfying the group action axioms.

# Context & Application

Group actions are the primary reason Lie groups are so frequently used — they typically appear as symmetry groups of geometric objects. Actions give rise to orbits, stabilizers, homogeneous spaces, and induced representations.

# Examples

**Example 2.15** (p. 11):
- $\mathrm{GL}(n, \mathbb{R})$ acts on $\mathbb{R}^n$.
- $\mathrm{O}(n, \mathbb{R})$ acts on the sphere $S^{n-1} \subset \mathbb{R}^n$.
- $\mathrm{U}(n)$ acts on the sphere $S^{2n-1} \subset \mathbb{C}^n$.

# Relationships

## Builds Upon
- **Lie group** — the group that acts

## Enables
- **Orbit** — the orbit of a point under the action
- **Stabilizer subgroup** — the subgroup fixing a point
- **Homogeneous space** — when the action is transitive
- **Representation of Lie group** — special case when $M$ is a vector space

## Related
- **Lie algebra action by vector fields** — the infinitesimal version (Theorem 3.22)

# Common Errors

- **Error**: Forgetting the smoothness requirement for the joint map $G \times M \to M$.
  **Correction**: It is not enough for each $\rho(g)$ to be smooth individually; the dependence on $g$ must also be smooth.

# Common Confusions

- **Confusion**: Confusing left actions with right actions.
  **Clarification**: Definition 2.14 gives a left action ($\rho(gh) = \rho(g)\rho(h)$). A right action would satisfy $\rho(gh) = \rho(h)\rho(g)$.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.2, Definition 2.14, page 11.

# Verification Notes

- Definition source: Direct from Definition 2.14
- Confidence rationale: Explicit definition in source
- Uncertainties: None
- Cross-reference status: Verified with Examples 2.15, Theorem 3.22
