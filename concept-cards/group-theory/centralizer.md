---
# === CORE IDENTIFICATION ===
concept: Centralizer
slug: centralizer

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
pdf_page: 59
section: "Stabilizers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "C_G(x)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - stabilizer
  - group-action
extends:
  - stabilizer
related:
  - centre-of-group
  - normalizer
  - conjugacy-class
contrasts_with:
  - normalizer

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the centralizer of an element?"
---

# Quick Definition

The centralizer $C_G(x)$ of $x$ in $G$ is the set of elements that commute with $x$: $C_G(x) = \{g \in G \mid gx = xg\}$.

# Core Definition

"Let $G$ act on itself by conjugation. Then $\operatorname{Stab}(x) = \{g \in G \mid gx = xg\}$. This group is called the centralizer $C_G(x)$ of $x$ in $G$" (Milne, Example 4.5a, p. 59).

# Prerequisites

- **Stabilizer** — The centralizer is the stabilizer under conjugation
- **Group action** — Specifically the conjugation action

# Key Properties

1. $C_G(x)$ is a subgroup of $G$
2. $\bigcap_{x \in G} C_G(x) = Z(G)$, the centre
3. Size of conjugacy class of $x$ is $(G : C_G(x))$
4. $x \in Z(G)$ iff $C_G(x) = G$

# Context & Application

Centralizers measure how much an element commutes with the rest of the group. They are the stabilizers of the conjugation action and appear throughout the class equation.

# Examples

**Example 1** (p. 59): $\bigcap_{x \in G} C_G(x) = Z(G)$.

# Relationships

## Builds Upon
- **stabilizer** — Centralizer is stabilizer of conjugation action

## Related
- **centre-of-group** — $Z(G) = \bigcap C_G(x)$
- **conjugacy-class** — Size is $(G : C_G(x))$

## Contrasts With
- **normalizer** — Normalizer stabilizes a subgroup; centralizer stabilizes an element

# Source Reference

Chapter 4: Groups Acting on Sets, "Stabilizers", Example 4.5a, page 59.

# Verification Notes

- Definition source: Direct from Example 4.5a, p. 59
- Confidence: HIGH — explicit definition
- Uncertainties: None
