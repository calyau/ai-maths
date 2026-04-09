---
concept: Orbit
slug: orbit
category: group-structure
subcategory: group-actions
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Group Actions"
chapter_number: 14
pdf_page: 182
section: "Groups Acting on Sets"
extraction_confidence: high
aliases:
  - "orbit of x"
  - "O_x"
prerequisites:
  - group-action
  - g-equivalence
extends: []
related:
  - stabilizer-subgroup
  - orbit-stabilizer-theorem
  - burnside-counting-theorem
contrasts_with: []
answers_questions:
  - "What is an orbit under a group action?"
  - "How do orbits partition a G-set?"
---

# Quick Definition

The orbit of an element $x$ in a $G$-set $X$ is the set $\mathcal{O}_x = \{gx : g \in G\}$ of all elements reachable from $x$ by the group action. The orbits partition $X$ into disjoint equivalence classes.

# Core Definition

"If $X$ is a $G$-set, then each partition of $X$ associated with $G$-equivalence is called an **orbit** of $X$ under $G$. We will denote the orbit that contains an element $x$ of $X$ by $\mathcal{O}_x$" (Judson, p. 182).

# Prerequisites

- **Group action** — Orbits are defined for group actions
- **G-equivalence** — Orbits are equivalence classes

# Key Properties

1. $\mathcal{O}_x = \{gx : g \in G\}$
2. Orbits partition $X$
3. $|\mathcal{O}_x| = [G:G_x]$ (Orbit-Stabilizer Theorem, Theorem 14.11)
4. If $G$ is finite: $|\mathcal{O}_x| = |G|/|G_x|$, so orbit size divides $|G|$

# Examples

**Example 1** (p. 182): For $G = \{(1),(123),(132),(45),(123)(45),(132)(45)\}$ acting on $\{1,2,3,4,5\}$: orbits are $\{1,2,3\}$ and $\{4,5\}$.

# Relationships

## Builds Upon
- **G-equivalence** — Orbits are equivalence classes

## Enables
- **Orbit-Stabilizer theorem** — $|\mathcal{O}_x| = [G:G_x]$
- **Class equation** — Sums orbit sizes
- **Burnside's counting theorem** — Counts orbits

## Related
- **Stabilizer subgroup** — $|G_x| \cdot |\mathcal{O}_x| = |G|$

# Source Reference

Chapter 14: Group Actions, Section 14.1, p. 182. Example 14.7.

# Verification Notes

- Definition source: Direct from p. 182
- Confidence: HIGH
