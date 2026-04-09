---
# === CORE IDENTIFICATION ===
concept: Stable Subset
slug: stable-subset

# === CLASSIFICATION ===
category: group-actions
subcategory: definitions
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 57
section: "Orbits"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - G-stable subset
  - invariant subset

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
extends: []
related:
  - orbit
  - normal-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a stable subset of a G-set?"
---

# Quick Definition

A subset $S \subset X$ is stable (or $G$-stable) under the action of $G$ if $g \in G$, $x \in S$ implies $gx \in S$.

# Core Definition

"A subset $S \subset X$ is said to be stable under the action of $G$ if $g \in G$, $x \in S \implies gx \in S$. The action of $G$ on $X$ then induces an action of $G$ on $S$" (Milne, p. 57).

# Prerequisites

- **Group action** — Stability is defined relative to an action

# Key Properties

1. A subset is stable iff it is a union of orbits
2. Every orbit is a stable subset
3. A subgroup $H \leq G$ is normal iff it is stable under the conjugation action

# Relationships

## Related
- **orbit** — Orbits are the minimal stable subsets
- **normal-subgroup** — Normal = stable under conjugation

# Source Reference

Chapter 4: Groups Acting on Sets, "Orbits", page 57.

# Verification Notes

- Definition source: Direct from p. 57
- Confidence: HIGH — explicit definition
- Uncertainties: None
