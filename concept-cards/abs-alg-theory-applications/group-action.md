---
concept: Group Action
slug: group-action
category: group-structure
subcategory: group-actions
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Group Actions"
chapter_number: 14
pdf_page: 181
section: "Groups Acting on Sets"
extraction_confidence: high
aliases:
  - "left action"
  - "group acting on a set"
prerequisites:
  - group
extends: []
related:
  - g-set
  - orbit
  - stabilizer-subgroup
  - g-equivalence
contrasts_with: []
answers_questions:
  - "What is a group action?"
  - "How do groups act on sets?"
---

# Quick Definition

A (left) group action of a group $G$ on a set $X$ is a map $G \times X \to X$, written $(g, x) \mapsto gx$, satisfying (1) $ex = x$ for all $x$ and (2) $(g_1 g_2)x = g_1(g_2 x)$ for all $g_1, g_2 \in G$ and $x \in X$.

# Core Definition

"Let $X$ be a set and $G$ be a group. A **(left) action** of $G$ on $X$ is a map $G \times X \to X$ given by $(g, x) \mapsto gx$, where (1) $ex = x$ for all $x \in X$; (2) $(g_1 g_2)x = g_1(g_2 x)$ for all $x \in X$ and all $g_1, g_2 \in G$" (Judson, p. 181).

# Prerequisites

- **Group** — The acting group

# Key Properties

1. Every group acts trivially on every set via $(g, x) \mapsto x$
2. Every group acts on itself by left multiplication
3. Every group acts on itself by conjugation
4. A group acts on the cosets of any subgroup by left multiplication
5. The action gives a homomorphism $G \to S_X$ (permutation representation)

# Examples

**Example 1** (p. 181): $GL_2(\mathbb{R})$ acts on $\mathbb{R}^2$ by matrix multiplication.

**Example 2** (p. 181): $D_4$ acts on vertices $\{1,2,3,4\}$ of a square.

**Example 3** (p. 182): Any group $G$ acts on itself by left multiplication: $(g, x) \mapsto gx$.

**Example 4** (p. 182): $G$ acts on itself by conjugation: $(h, g) \mapsto hgh^{-1}$.

**Example 5** (p. 182): $G$ acts on left cosets of $H$: $(g, xH) \mapsto gxH$.

# Relationships

## Enables
- **G-set** — A set with a group action
- **Orbit** — Equivalence classes under the action
- **Stabilizer subgroup** — Elements fixing a point
- **Class equation** — From the conjugation action

## Related
- **Burnside's counting theorem** — Uses group actions to count orbits

# Source Reference

Chapter 14: Group Actions, Section 14.1, pages 181-182. Examples 14.1-14.5.

# Verification Notes

- Definition source: Direct quote from p. 181
- Confidence: HIGH — explicit definition
