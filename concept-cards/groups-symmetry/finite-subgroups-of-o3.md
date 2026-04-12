---
# === CORE IDENTIFICATION ===
concept: Finite Subgroups of O(3)
slug: finite-subgroups-of-o3

# === CLASSIFICATION ===
category: symmetry-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Finite Rotation Groups"
chapter_number: 19
pdf_page: 111
section: "Exercise 19.5"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "classification of finite subgroups of O_3"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - finite-subgroups-of-so3
extends:
  - finite-subgroups-of-so3
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are all finite subgroups of O(3)?"
---

# Quick Definition

Every finite subgroup of $O_3$ is determined by its intersection $H$ with $SO_3$. The possibilities are listed in a table depending on whether $-I$ belongs to $G$ and on the isomorphism type of $H$.

# Core Definition

Let $G$ be a finite subgroup of $O_3$ and $H = G \cap SO_3$. If $-I \in G$, then $G \cong H \times \mathbb{Z}_2$. If $-I \notin G$, the map $A \mapsto (\det A) \cdot A$ gives an isomorphism from $G$ to a subgroup of $SO_3$ (Armstrong, Exercise 19.5, p. 118).

The complete list:

| $H$ | Possible $G$ |
|-----|--------------|
| $\{e\}$ | $\{e\}$, $\mathbb{Z}_2$ |
| $\mathbb{Z}_n$ | $\mathbb{Z}_n$, $\mathbb{Z}_n \times \mathbb{Z}_2$, $\mathbb{Z}_{2n}$ |
| $D_n$ | $D_n$, $D_n \times \mathbb{Z}_2$, $D_{2n}$ |
| $A_4$ | $A_4$, $A_4 \times \mathbb{Z}_2$, $S_4$ |
| $S_4$ | $S_4$, $S_4 \times \mathbb{Z}_2$ |
| $A_5$ | $A_5$, $A_5 \times \mathbb{Z}_2$ |

# Prerequisites

- **Finite subgroups of SO(3)** -- the classification of $H$ is the starting point

# Key Properties

1. $H = G \cap SO_3$ has index at most 2 in $G$
2. If $G \subseteq SO_3$, then $G = H$ and we are in the $SO_3$ case
3. If $-I \in G$, then $G \cong H \times \mathbb{Z}_2$
4. If $-I \notin G$ but $G \not\subseteq SO_3$, the map $A \mapsto (\det A)A$ gives an isomorphism to a subgroup of $SO_3$

# Context & Application

This extends the rotation group classification to include reflections and improper rotations. The full symmetry groups of solids (including reflections) are finite subgroups of $O_3$.

# Relationships

## Builds Upon
- **Finite subgroups of SO(3)** -- the core classification being extended

# Source Reference

Chapter 19: Finite Rotation Groups, Exercise 19.5, pages 118--119. Table on p. 119.

# Verification Notes

- Classification table: Direct from Exercise 19.5, p. 119
- Confidence: MEDIUM -- presented as an exercise, but the table is given explicitly
