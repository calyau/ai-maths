---
# === CORE IDENTIFICATION ===
concept: Block (Group Actions)
slug: block-system

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
  - block
  - system of imprimitivity

# === TYPED RELATIONSHIPS ===
prerequisites:
  - transitive-action
  - stabilizer
extends: []
related:
  - primitive-action
  - imprimitive-action
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a block in the context of group actions?"
---

# Quick Definition

A block is a proper nonempty subset $A \subsetneq X$ with $|A| \geq 2$ such that for each $g \in G$, either $gA = A$ or $gA \cap A = \emptyset$.

# Core Definition

"A subset $A$ of $X$ satisfying [for each $g \in G$, either $gA = A$ or $gA \cap A = \emptyset$] is called a block" (Milne, p. 71, after Proposition 4.43).

# Prerequisites

- **Transitive action** — Blocks are defined for transitive actions
- **Stabilizer** — Block stabilizers connect to primitivity

# Key Properties

1. The translates $\{A, g_1 A, g_2 A, \ldots\}$ form a $G$-stabilized partition of $X$ (Proposition 4.43)
2. For any $x \in A$: $\operatorname{Stab}(x) \subsetneq \operatorname{Stab}(A) \subsetneq G$ (Proposition 4.44)
3. No nontrivial blocks exist iff the action is primitive
4. Existence of a block iff $\operatorname{Stab}(x)$ is not maximal (Theorem 4.45)
5. If $H$ is a proper subgroup strictly containing $\operatorname{Stab}(x)$, then $Hx$ is a block

# Context & Application

Blocks decompose a transitive action into "smaller" pieces. An imprimitive action can be understood by first understanding the action on the block system, then the action within each block.

# Examples

**Example 1** (p. 71): $\{1,3\}$ is a block for $\langle (1234) \rangle$ acting on $\{1,2,3,4\}$; the block system is $\{\{1,3\}, \{2,4\}\}$.

**Example 2** (p. 71): $\{1,3\}$ is a block for $D_4$ acting on vertices of a square.

# Relationships

## Related
- **primitive-action** — Primitive iff no nontrivial blocks
- **imprimitive-action** — Characterized by existence of blocks

# Source Reference

Chapter 4: Groups Acting on Sets, "Primitive actions", page 71.

# Verification Notes

- Definition source: Direct from p. 71
- Confidence: HIGH — explicit definition
- Uncertainties: None
