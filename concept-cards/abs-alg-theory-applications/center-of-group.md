---
# === CORE IDENTIFICATION ===
concept: Center of a Group
slug: center-of-group

# === CLASSIFICATION ===
category: group-theory
subcategory: group-properties
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 56
section: "Exercises"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "Z(G)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - subgroup
extends: []
related:
  - abelian-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a subgroup?"
---

# Quick Definition

The center of a group $G$, denoted $Z(G)$, is the set of elements that commute with every element of $G$: $Z(G) = \{x \in G : gx = xg \text{ for all } g \in G\}$.

# Core Definition

"Let $G$ be a group and $g \in G$. Show that $Z(G) = \{x \in G : gx = xg \text{ for all } g \in G\}$ is a subgroup of $G$. This subgroup is called the center of $G$" (Judson, Exercise 48, p. 56).

# Prerequisites

- **Group** — The center is defined for groups
- **Subgroup** — The center is a subgroup

# Key Properties

1. $Z(G)$ is always a subgroup of $G$
2. $Z(G)$ is always abelian
3. $G$ is abelian if and only if $Z(G) = G$
4. $Z(G) = \{e\}$ is possible for nonabelian groups

# Context & Application

The center measures "how abelian" a group is. If $Z(G) = G$, the group is abelian. The center plays an important role in the structure theory of groups.

# Examples

**Example 1**: For an abelian group $G$, $Z(G) = G$.

**Example 2**: For $S_3$, $Z(S_3) = \{e\}$ since no non-identity element commutes with all others.

# Relationships

## Builds Upon
- **group** — Defined for groups
- **subgroup** — The center is a subgroup

## Related
- **abelian-group** — $G$ is abelian iff $Z(G) = G$

# Source Reference

Chapter 3: Groups, Section 3.5, Exercise 48, page 56.

# Verification Notes

- Definition source: From exercise statement, not a theorem in the main text
- Confidence: MEDIUM — defined in exercises, not main exposition
- Cross-reference status: Verified
- Uncertainties: Formal treatment may appear in later chapters
