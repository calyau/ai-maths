---
concept: Unique Subgroup of Given Order is Normal
slug: unique-subgroup-is-normal
category: group-structure
subcategory: subgroup-types
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
  - normal-subgroup
  - conjugation-of-subgroups
extends: []
related:
  - sylow-p-subgroup
  - second-sylow-theorem
contrasts_with: []
answers_questions:
  - "How do I determine if a subgroup is normal?"
---

# Quick Definition

If a group $G$ has exactly one subgroup $H$ of a given order $k$, then $H$ is automatically normal in $G$, since conjugation preserves subgroup order.

# Core Definition

**Exercise 10.4.11**: "If a group $G$ has exactly one subgroup $H$ of order $k$, prove that $H$ is normal in $G$" (Judson, p. 144). Since $gHg^{-1}$ is a subgroup of the same order $k$, and $H$ is the unique such subgroup, $gHg^{-1} = H$ for all $g$.

# Prerequisites

- **Normal subgroup** — The conclusion
- **Conjugation of subgroups** — $gHg^{-1}$ has the same order as $H$

# Key Properties

1. $|gHg^{-1}| = |H|$ for all $g$
2. Uniqueness of $H$ forces $gHg^{-1} = H$
3. This is the key argument in Sylow theory: a unique Sylow $p$-subgroup is normal

# Relationships

## Related
- **Sylow $p$-subgroup** — If there's only one, it's normal (same argument)

# Source Reference

Chapter 10, Exercise 10.4.11, p. 144. Also Chapter 11, Exercise 11.4.12.

# Verification Notes

- Definition source: Exercise 10.4.11
- Confidence: HIGH
