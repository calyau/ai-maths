---
# === CORE IDENTIFICATION ===
concept: Primitive Action
slug: primitive-action

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
aliases:
  - primitive group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - transitive-action
  - stabilizer
extends:
  - transitive-action
related:
  - doubly-transitive-action
  - block-system
contrasts_with:
  - imprimitive-action

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a primitive group action?"
  - "How does primitivity relate to maximal subgroups?"
---

# Quick Definition

A transitive action is primitive if the only partitions of $X$ stabilized by $G$ are the trivial ones (singletons and $\{X\}$).

# Core Definition

"The group $G$ always stabilizes the trivial partitions of $X$, namely, the set of all one-element subsets of $X$, and $\{X\}$. When it stabilizes only those partitions, we say that the action is primitive; otherwise it is imprimitive" (Milne, p. 71).

# Prerequisites

- **Transitive action** — Primitive implies transitive (Remark 4.42)
- **Stabilizer** — Primitivity characterized by maximal stabilizers

# Key Properties

1. Primitive implies transitive or trivial (Remark 4.42)
2. Doubly transitive implies primitive (Example 4.41)
3. $G$ acts primitively iff $\operatorname{Stab}(x)$ is a maximal subgroup of $G$ for any $x$ (Theorem 4.45)
4. $G$ acts imprimitively iff there exists a proper subset $A \subset X$ with $|A| \geq 2$ such that for each $g$, either $gA = A$ or $gA \cap A = \emptyset$ (Proposition 4.43)

# Construction / Recognition

## To check primitivity:
1. Verify the action is transitive
2. Check that $\operatorname{Stab}(x)$ is a maximal subgroup of $G$ for some (hence any) $x \in X$
3. Alternatively: verify no nontrivial block exists

# Context & Application

Primitive actions are the "irreducible" transitive actions. Understanding which groups act primitively on which sets is important in permutation group theory and connects to the O'Nan-Scott theorem.

# Examples

**Example 1** (p. 71): $S_n$ acts primitively on $\{1, \ldots, n\}$.

**Example 2** (p. 71): $D_4$ acting on $\{1,2,3,4\}$ (vertices of a square) is not primitive: the partition $\{\{1,3\}, \{2,4\}\}$ (opposite vertices) is stabilized.

# Relationships

## Builds Upon
- **transitive-action**, **stabilizer**

## Contrasts With
- **imprimitive-action** — Stabilizes a nontrivial partition

## Related
- **doubly-transitive-action** — Doubly transitive implies primitive
- **block-system** — Blocks characterize imprimitivity

# Source Reference

Chapter 4: Groups Acting on Sets, "Primitive actions", pages 71-72.

# Verification Notes

- Definition source: Direct from p. 71
- Confidence: HIGH — explicit definition
- Uncertainties: None
