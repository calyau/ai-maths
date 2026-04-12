---
# === CORE IDENTIFICATION ===
concept: Conjugation Action
slug: conjugation-action

# === CLASSIFICATION ===
category: group-actions
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Actions, Orbits, and Stabilizers"
chapter_number: 17
pdf_page: 98
section: "Example (v)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "action by conjugation"
  - "inner action"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
extends:
  - group-action
related:
  - conjugacy-class
  - centralizer
  - centre-of-p-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a group act on itself by conjugation?"
  - "What are the orbits and stabilizers of the conjugation action?"
---

# Quick Definition

The conjugation action of a group $G$ on itself sends $x$ to $gxg^{-1}$. The orbits are conjugacy classes and the stabilizer of $x$ is the set of elements commuting with $x$.

# Core Definition

Take any group $G$ and let $X$ be the underlying set of $G$. Let $G$ act on $X$ by conjugation: $g \in G$ sends $x$ to $gxg^{-1}$. This is an action because $(gh)x(gh)^{-1} = g(hxh^{-1})g^{-1}$ for all $g, h \in G$ and $x \in X$ (Armstrong, p. 100).

The orbits are the **conjugacy classes** of $G$. The stabilizer of the point $x$ is $\{g \in G \mid gxg^{-1} = x\} = \{g \in G \mid gx = xg\}$, the subgroup of elements commuting with $x$ (p. 100).

# Prerequisites

- **Group action** -- this is a specific instance of a group action

# Key Properties

1. The orbits are conjugacy classes
2. The stabilizer of $x$ is $\{g \in G \mid gx = xg\}$, the centralizer of $x$
3. The centre $Z(G)$ consists of the elements whose conjugacy class is a singleton
4. The size of each conjugacy class divides $|G|$ (by Corollary 17.3)

# Construction / Recognition

## To Construct:
1. Let $G$ act on its own underlying set
2. Define $g \cdot x = gxg^{-1}$
3. Verify: $(gh) \cdot x = ghx(gh)^{-1} = ghxh^{-1}g^{-1} = g \cdot (h \cdot x)$

# Context & Application

The conjugation action is perhaps the most important group action in algebra. It connects group actions to conjugacy classes, centres, centralisers, and normal subgroups. Armstrong uses it to prove that p-groups have non-trivial centres (Theorem 17.4) and to classify groups of order $p^2$ (Theorem 17.5).

# Examples

**Example (v)** (p. 100): For any finite group $G$, the number of elements in each conjugacy class is $|G|/|C(x)|$ where $C(x)$ is the centralizer of $x$. This divides $|G|$.

# Relationships

## Builds Upon
- **Group action** -- conjugation is a particular group action

## Enables
- **Centre of p-group** -- Theorem 17.4 uses conjugation to show p-groups have non-trivial centres
- **Classification of groups of order p-squared** -- Theorem 17.5 uses the conjugation action

## Related
- **Conjugacy class** -- the orbits of this action
- **Centralizer** -- the stabilizers of this action (Exercise 17.10)

# Common Errors

- **Error**: Writing the conjugation action as $g \cdot x = g^{-1}xg$ instead of $gxg^{-1}$.
  **Correction**: Armstrong uses $gxg^{-1}$. Both conventions define valid actions, but one must be consistent.

# Common Confusions

- **Confusion**: Thinking conjugation by different elements always gives different results.
  **Clarification**: If $g$ and $g'$ are in the same coset of the centralizer $C(x)$, then $gxg^{-1} = g'xg'^{-1}$.

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, Example (v), page 100. Continued on p. 100 with applications in Theorems 17.4--17.5.

# Verification Notes

- Definition: Direct from Example (v), p. 100
- Confidence: HIGH -- explicit example with verification of action axiom
