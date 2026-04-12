---
# === CORE IDENTIFICATION ===
concept: Poles of a Rotation
slug: poles-of-rotation

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
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "poles"
  - "poles of a rotation matrix"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
extends: []
related:
  - finite-subgroups-of-so3
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the poles of a rotation in three-dimensional space?"
---

# Quick Definition

The poles of a rotation $g \in SO_3$ (other than the identity) are the two points where the rotation axis meets the unit sphere. These are the only points on the unit sphere fixed by $g$.

# Core Definition

The two points where the axis of a rotation $g \in G$ meets the unit sphere are called the **poles** of $g$. If the axis is the $z$-axis, these are the usual North and South poles. These poles are the only points on the unit sphere which are left fixed by the given rotation (Armstrong, p. 112).

# Prerequisites

- **Group action** -- poles arise from the action of $SO_3$ on the unit sphere

# Key Properties

1. Every non-identity rotation in $\mathbb{R}^3$ has exactly two poles (antipodal points on the unit sphere)
2. The poles are precisely the fixed points of the rotation on the unit sphere
3. If $x$ is a pole of $h$ and $g \in G$, then $g(x)$ is a pole of $ghg^{-1}$
4. The set of all poles is invariant under the group action

# Construction / Recognition

## To Find Poles:
1. Given a rotation $g \ne e$ in $SO_3$, find its axis of rotation
2. The two intersection points of this axis with the unit sphere are the poles

# Context & Application

Poles are the key geometric tool in the classification of finite subgroups of $SO_3$ (Theorem 19.2). The proof applies the Counting Theorem to the action of $G$ on the set $X$ of all poles of non-identity elements, then analyses the resulting constraints on orbit sizes and stabilizer orders.

# Examples

**Figure 19.1** (p. 112): Illustration of poles as the two points where a rotation axis pierces the unit sphere.

# Relationships

## Enables
- **Finite subgroups of SO(3)** -- the classification proof analyses orbits and stabilizers of poles

## Related
- **Group action** -- $G$ acts on the set of poles

# Source Reference

Chapter 19: Finite Rotation Groups, page 112. Definition in the proof of Theorem 19.2.

# Verification Notes

- Definition: Direct from p. 112
- Confidence: HIGH -- clearly defined geometric concept
