---
# === CORE IDENTIFICATION ===
concept: Center of a Group
slug: center-of-group

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 12
section: "Subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - centre

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
  - normal-subgroup
extends: []
related:
  - conjugation
  - commutator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the center of a group?"
  - "Which elements commute with all others?"
---

# Quick Definition

The center of a group $G$ is $Z(G) = \{g \in G \mid gx = xg \text{ for all } x \in G\}$, the set of elements that commute with every element. It is a normal subgroup.

# Core Definition

"The *centre* of a group $G$ is the subset $Z(G) = \{g \in G \mid gx = xg \text{ for all } x \in G\}$. It is a subgroup of $G$." (Milne, Example 1.12, p. 12)

# Prerequisites

- **Subgroup** — The center is a subgroup
- **Normal subgroup** — The center is always normal (it is invariant under conjugation)

# Key Properties

1. $Z(G)$ is a normal subgroup of $G$
2. $G$ is commutative $\iff$ $Z(G) = G$
3. $Z(G) = \{e\}$ for many noncommutative groups
4. $-I$ is in $Z(\mathrm{GL}_n(F))$

# Context & Application

The center captures the "commutative part" of a group. The quotient $G/Z(G)$ measures how far $G$ is from being commutative.

# Examples

**Example 1**: $Z(\mathrm{GL}_n(F))$ consists of scalar matrices $\lambda I$, $\lambda \in F^{\times}$.

**Example 2**: $Z(D_n) = \{e\}$ for odd $n \ge 3$, and $Z(D_n) = \{e, r^{n/2}\}$ for even $n \ge 4$.

# Relationships

## Builds Upon
- **subgroup**, **normal-subgroup** — the center is a normal subgroup

## Related
- **conjugation** — $Z(G)$ is the set of elements fixed by all conjugations
- **commutator** — $a \in Z(G) \iff [a, g] = e$ for all $g$

# Common Errors

- **Error**: Assuming the center is always nontrivial
  **Correction**: Many groups have trivial center (e.g., $S_n$ for $n \ge 3$)

# Source Reference

Chapter 1, Example 1.12, page 12.

# Verification Notes

- Definition source: Direct from Example 1.12
- Confidence: HIGH — explicit definition
- Uncertainties: None
