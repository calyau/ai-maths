---
# === CORE IDENTIFICATION ===
concept: Stabilizer
slug: stabilizer

# === CLASSIFICATION ===
category: group-actions
subcategory: orbits-stabilizers
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 58
section: "Stabilizers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - isotropy group
  - isotropy subgroup
  - "Stab(x)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
extends: []
related:
  - orbit
  - orbit-stabilizer-theorem
  - centralizer
  - normalizer
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the stabilizer of an element under a group action?"
  - "How do orbits and stabilizers relate via the orbit-stabilizer theorem?"
---

# Quick Definition

The stabilizer of $x \in X$ is the subgroup $\operatorname{Stab}(x) = \{g \in G \mid gx = x\}$ of elements that fix $x$.

# Core Definition

"The stabilizer (or isotropy group) of an element $x \in X$ is $\operatorname{Stab}(x) = \{g \in G \mid gx = x\}$. It is a subgroup, but it need not be a normal subgroup" (Milne, p. 58).

# Prerequisites

- **Group action** — Stabilizers are defined in terms of an action

# Key Properties

1. $\operatorname{Stab}(x)$ is a subgroup of $G$ (not necessarily normal)
2. $\operatorname{Stab}(gx) = g \cdot \operatorname{Stab}(x) \cdot g^{-1}$ (Lemma 4.4)
3. $\bigcap_{x \in X} \operatorname{Stab}(x) = \ker(G \to \operatorname{Sym}(X))$, a normal subgroup
4. The action is faithful iff $\bigcap \operatorname{Stab}(x) = \{1\}$
5. For a subset $S \subset X$: $\operatorname{Stab}(S) = \{g \in G \mid gS = S\}$

# Construction / Recognition

## To compute $\operatorname{Stab}(x)$:
1. Find all $g \in G$ such that $gx = x$
2. Verify this is a subgroup (it always is)

# Context & Application

Stabilizers measure the "symmetry" of a point. The orbit-stabilizer theorem connects the orbit size to the index of the stabilizer. Stabilizers generalize centralizers and normalizers.

# Examples

**Example 1** (p. 58): For conjugation on $G$, $\operatorname{Stab}(x) = C_G(x) = \{g \mid gx = xg\}$, the centralizer.

**Example 2** (p. 59): For $G$ acting on $G/H$ by left multiplication, $\operatorname{Stab}(H) = H$.

**Example 3** (p. 59): For rigid motions of $\mathbb{R}^n$, the stabilizer of the origin is the orthogonal group $O_n$.

# Relationships

## Builds Upon
- **group-action**

## Enables
- **orbit-stabilizer-theorem** — $|Gx_0| = (G : \operatorname{Stab}(x_0))$
- **faithful-action** — Faithful iff intersection of all stabilizers is trivial

## Related
- **centralizer** — Stabilizer under conjugation action
- **normalizer** — Stabilizer of a subgroup under conjugation

# Source Reference

Chapter 4: Groups Acting on Sets, "Stabilizers", page 58.

# Verification Notes

- Definition source: Direct from p. 58
- Confidence: HIGH — explicit definition
- Uncertainties: None
