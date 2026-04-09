---
# === CORE IDENTIFICATION ===
concept: Imprimitive Action
slug: imprimitive-action

# === CLASSIFICATION ===
category: group-actions
subcategory: action-properties
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 71
section: "Primitive actions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - transitive-action
extends: []
related:
  - block-system
contrasts_with:
  - primitive-action

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an imprimitive action?"
---

# Quick Definition

A transitive action is imprimitive if $G$ stabilizes a nontrivial partition of $X$ (one that is neither all singletons nor $\{X\}$).

# Core Definition

A transitive action that is not primitive is imprimitive. Equivalently (Proposition 4.43), there exists a proper subset $A$ of $X$ with $|A| \geq 2$ such that for each $g \in G$, either $gA = A$ or $gA \cap A = \emptyset$.

# Prerequisites

- **Transitive action** — Imprimitivity is defined for transitive actions

# Key Properties

1. Imprimitive iff there exists a nontrivial block (Proposition 4.43)
2. Imprimitive iff $\operatorname{Stab}(x)$ is not maximal in $G$ (Theorem 4.45)
3. The blocks form a partition of $X$ stabilized by $G$

# Examples

**Example 1** (p. 71): $\langle (1234) \rangle$ acting on $\{1,2,3,4\}$ stabilizes $\{\{1,3\}, \{2,4\}\}$.

**Example 2** (p. 71): $D_4$ acting on vertices of a square stabilizes the partition of opposite vertices.

# Relationships

## Contrasts With
- **primitive-action** — Primitive means no nontrivial stabilized partition

## Related
- **block-system** — Blocks characterize imprimitivity

# Source Reference

Chapter 4: Groups Acting on Sets, "Primitive actions", page 71.

# Verification Notes

- Definition source: Direct from p. 71
- Confidence: HIGH — explicit definition
- Uncertainties: None
