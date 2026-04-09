---
concept: Cyclic Factor Groups
slug: cyclic-factor-group
category: group-structure
subcategory: group-constructions
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Normal Subgroups and Factor Groups"
chapter_number: 10
pdf_page: 144
section: "Exercises"
extraction_confidence: high
aliases: []
prerequisites:
  - factor-group
  - cyclic-group
extends:
  - factor-group
related: []
contrasts_with: []
answers_questions:
  - "When is a factor group cyclic?"
---

# Quick Definition

If $G$ is cyclic, then every factor group $G/H$ is also cyclic. However, the converse is false: $G/H$ cyclic does not imply $G$ is cyclic.

# Core Definition

**Exercise 10.4.8**: "If $G$ is cyclic, prove that $G/H$ must also be cyclic." **Exercise 10.4.9**: "Prove or disprove: If $H$ and $G/H$ are cyclic, then $G$ is cyclic" (Judson, p. 144).

# Prerequisites

- **Factor group** — Structure being studied
- **Cyclic group** — The property being preserved

# Key Properties

1. $G$ cyclic implies $G/H$ cyclic
2. The converse fails: $\mathbb{Z}_2 \times \mathbb{Z}_2$ has cyclic quotients but is not cyclic
3. If $gH$ generates $G/H$, every element of $G/H$ has the form $g^k H$

# Relationships

## Builds Upon
- **Factor group** — Property of factor groups

# Source Reference

Chapter 10: Normal Subgroups and Factor Groups, Exercises 10.4.8-10.4.9, p. 144.

# Verification Notes

- Definition source: Exercises 10.4.8-10.4.9
- Confidence: HIGH
