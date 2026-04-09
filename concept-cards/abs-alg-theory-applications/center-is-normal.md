---
concept: Center of a Group is Normal
slug: center-is-normal
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
  - center-of-group
  - normal-subgroup
extends: []
related:
  - centralizer-of-element
  - conjugacy-class
contrasts_with: []
answers_questions:
  - "Is the center of a group always normal?"
---

# Quick Definition

The center $Z(G) = \{x \in G : xg = gx \text{ for all } g \in G\}$ is always a normal subgroup of $G$. Moreover, if $G/Z(G)$ is cyclic, then $G$ is abelian.

# Core Definition

**Exercise 10.4.13(c)**: "Show that the center of any group $G$ is a normal subgroup of $G$" (Judson, p. 144). **Exercise 10.4.13(d)**: "If $G/Z(G)$ is cyclic, show that $G$ is abelian."

# Prerequisites

- **Center of group** — $Z(G)$ is the set of elements commuting with everything
- **Normal subgroup** — $Z(G)$ is normal

# Key Properties

1. $Z(G) \trianglelefteq G$ (since $gxg^{-1} = x$ for $x \in Z(G)$)
2. If $G/Z(G)$ is cyclic, then $G$ is abelian
3. $Z(G) = G$ if and only if $G$ is abelian

# Context & Application

The fact that $G/Z(G)$ cyclic implies $G$ abelian is used in proving groups of order $p^2$ are abelian (Corollary 14.16).

# Relationships

## Builds Upon
- **Center of group** — The subject
- **Normal subgroup** — The center is always normal

## Enables
- **Groups of order $p^2$ are abelian** — Uses $G/Z(G)$ cyclic implies $G$ abelian

# Source Reference

Chapter 10: Normal Subgroups and Factor Groups, Exercise 10.4.13, p. 144.

# Verification Notes

- Definition source: Exercise 10.4.13
- Confidence: HIGH
