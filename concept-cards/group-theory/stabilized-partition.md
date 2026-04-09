---
# === CORE IDENTIFICATION ===
concept: Stabilized Partition
slug: stabilized-partition

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
  - G-stable partition

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
extends: []
related:
  - primitive-action
  - imprimitive-action
  - block-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a stabilized partition in the context of group actions?"
---

# Quick Definition

A partition $\pi$ of $X$ is stabilized by $G$ if $A \in \pi \implies gA \in \pi$ for all $g \in G$.

# Core Definition

"Let $G$ be a group acting on a set $X$, and let $\pi$ be a partition of $X$. We say that $\pi$ is stabilized by $G$ if $A \in \pi \implies gA \in \pi$" (Milne, p. 71). It suffices to check for a generating set of $G$.

# Prerequisites

- **Group action** — Stabilized partitions are defined relative to an action

# Key Properties

1. Every action stabilizes two trivial partitions: all singletons, and $\{X\}$
2. The partition into orbits is always stabilized
3. The action is primitive iff only trivial partitions are stabilized

# Examples

**Example 1** (p. 71): $\langle (1234) \rangle$ stabilizes $\{\{1,3\}, \{2,4\}\}$ in $S_4$.

**Example 2** (p. 71): $D_4$ stabilizes $\{\{1,3\}, \{2,4\}\}$ (opposite vertices of a square).

# Relationships

## Related
- **primitive-action** — Primitive iff only trivial partitions stabilized
- **block-system** — Parts of a nontrivial stabilized partition are blocks

# Source Reference

Chapter 4: Groups Acting on Sets, "Primitive actions", page 71.

# Verification Notes

- Definition source: Direct from p. 71
- Confidence: HIGH — explicit definition
- Uncertainties: None
