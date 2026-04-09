---
concept: Conjugation Action
slug: conjugation-action
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
  - "action by conjugation"
prerequisites:
  - group-action
extends:
  - group-action
related:
  - conjugacy-class
  - class-equation
  - center-of-group
  - inner-automorphism
contrasts_with: []
answers_questions:
  - "How does a group act on itself by conjugation?"
---

# Quick Definition

The conjugation action of $G$ on itself is defined by $(g, x) \mapsto gxg^{-1}$. Its orbits are conjugacy classes, its fixed points form the center $Z(G)$, and its stabilizers are centralizer subgroups.

# Core Definition

"If $G$ is a group and suppose that $X = G$. If $H$ is a subgroup of $G$, then $G$ is an $H$-set under **conjugation**; that is, we can define an action of $H$ on $G$ via $(h, g) \mapsto hgh^{-1}$" (Judson, p. 182, Example 14.4).

# Prerequisites

- **Group action** — Conjugation is a specific group action

# Key Properties

1. Orbits = conjugacy classes
2. Fixed points = center $Z(G) = \{x : gxg^{-1} = x \text{ for all } g\}$
3. Stabilizer of $x$ = centralizer $C(x) = \{g : gxg^{-1} = x\}$
4. Size of conjugacy class of $x$ = $[G:C(x)]$
5. Gives rise to the class equation

# Examples

**Example 1** (p. 182): Conjugation of $G$ by $H$ satisfies: $(h_1 h_2, g) = h_1 h_2 g(h_1 h_2)^{-1} = h_1(h_2 g h_2^{-1})h_1^{-1} = (h_1, (h_2, g))$.

# Relationships

## Enables
- **Conjugacy class** — Orbits under conjugation
- **Class equation** — From partitioning by orbits
- **Center of group** — Fixed points

# Source Reference

Chapter 14: Group Actions, Section 14.1, p. 182 (Example 14.4) and Section 14.2, p. 184.

# Verification Notes

- Definition source: Example 14.4
- Confidence: HIGH
