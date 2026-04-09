---
# === CORE IDENTIFICATION ===
concept: Doubly Transitive Action
slug: doubly-transitive-action

# === CLASSIFICATION ===
category: group-actions
subcategory: action-properties
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 58
section: "Orbits"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - 2-transitive action
  - k-fold transitivity

# === TYPED RELATIONSHIPS ===
prerequisites:
  - transitive-action
extends:
  - transitive-action
related:
  - primitive-action
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a doubly transitive action?"
---

# Quick Definition

An action is doubly transitive if for any two pairs $(x_1, x_2)$ and $(y_1, y_2)$ of distinct elements of $X$, there exists $g \in G$ with $gx_1 = y_1$ and $gx_2 = y_2$.

# Core Definition

"The action of $G$ on $X$ is doubly transitive if for any two pairs $(x_1, x_2)$, $(y_1, y_2)$ of elements of $X$ with $x_1 \neq x_2$ and $y_1 \neq y_2$, there exists a (single) $g \in G$ such that $gx_1 = y_1$ and $gx_2 = y_2$. Define $k$-fold transitivity for $k \geq 3$ similarly" (Milne, p. 58).

# Prerequisites

- **Transitive action** — Doubly transitive implies transitive

# Key Properties

1. Doubly transitive implies transitive
2. Doubly transitive implies primitive (Example 4.41)
3. $S_n$ acts $n$-fold transitively on $\{1, \ldots, n\}$

# Context & Application

Doubly transitive actions are important in the classification of primitive groups and in the study of designs and codes.

# Examples

**Example 1** (p. 71): A doubly transitive action is primitive: if it stabilized a nontrivial partition $\{\{x, x', \ldots\}, \{y, \ldots\}, \ldots\}$, no element could send $(x, x')$ to $(x, y)$.

# Relationships

## Builds Upon
- **transitive-action**

## Enables
- **primitive-action** — Doubly transitive implies primitive

# Source Reference

Chapter 4: Groups Acting on Sets, "Orbits", page 58.

# Verification Notes

- Definition source: Direct from p. 58
- Confidence: HIGH — explicit definition
- Uncertainties: None
