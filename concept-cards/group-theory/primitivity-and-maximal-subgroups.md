---
# === CORE IDENTIFICATION ===
concept: Primitivity and Maximal Subgroups
slug: primitivity-and-maximal-subgroups

# === CLASSIFICATION ===
category: group-actions
subcategory: action-properties
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 72
section: "Primitive actions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primitive-action
  - stabilizer
extends:
  - primitive-action
related:
  - block-system
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does primitivity relate to maximal subgroups?"
---

# Quick Definition

A transitive action of $G$ on $X$ is primitive if and only if the stabilizer $\operatorname{Stab}(x)$ is a maximal subgroup of $G$ for any $x \in X$.

# Core Definition

"The group $G$ acts primitively on $X$ if and only if, for one (hence all) $x$ in $X$, $\operatorname{Stab}(x)$ is a maximal subgroup of $G$" (Milne, Theorem 4.45, p. 72).

# Prerequisites

- **Primitive action** — The property being characterized
- **Stabilizer** — Maximality of stabilizers characterizes primitivity

# Key Properties

1. If not primitive: there exists a block $A$ with $\operatorname{Stab}(x) \subsetneq \operatorname{Stab}(A) \subsetneq G$
2. If $\operatorname{Stab}(x)$ is not maximal, say $\operatorname{Stab}(x) \subsetneq H \subsetneq G$, then $Hx$ is a nontrivial block
3. This provides a practical criterion: check maximality of a point stabilizer

# Context & Application

This theorem connects the combinatorial notion of primitivity with the algebraic notion of maximal subgroups. It is the key tool for determining whether an action is primitive.

# Relationships

## Builds Upon
- **primitive-action**, **stabilizer**

# Source Reference

Chapter 4: Groups Acting on Sets, "Primitive actions", Theorem 4.45, page 72.

# Verification Notes

- Definition source: Theorem 4.45, p. 72
- Confidence: HIGH — explicit theorem with proof
- Uncertainties: None
