---
# === CORE IDENTIFICATION ===
concept: Classification of Transitive Actions
slug: transitive-action-classification

# === CLASSIFICATION ===
category: group-actions
subcategory: action-properties
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 59
section: "Transitive actions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - transitive-action
  - stabilizer
extends:
  - transitive-action
related:
  - homogeneous-g-set
  - orbit-stabilizer-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are transitive G-sets classified?"
---

# Quick Definition

Every transitive $G$-set is isomorphic to $G/\operatorname{Stab}(x_0)$ for any chosen basepoint $x_0$, via the map $g\operatorname{Stab}(x_0) \mapsto gx_0$.

# Core Definition

"If $G$ acts transitively on $X$, then for any $x_0 \in X$, the map $g\operatorname{Stab}(x_0) \mapsto gx_0 : G/\operatorname{Stab}(x_0) \to X$ is an isomorphism of $G$-sets" (Milne, Proposition 4.7, p. 59).

# Prerequisites

- **Transitive action** — The action must be transitive
- **Stabilizer** — The stabilizer determines the isomorphism type

# Key Properties

1. Well-defined: $h \in \operatorname{Stab}(x_0) \implies ghx_0 = gx_0$
2. Injective: $gx_0 = g'x_0 \implies g^{-1}g' \in \operatorname{Stab}(x_0)$
3. Surjective: transitivity
4. $G$-equivariant: obvious
5. The realization depends on the choice of $x_0$; different choices give conjugate stabilizers
6. A transitive $G$-set with a preferred point $\leftrightarrow$ a subgroup of $G$

# Context & Application

This is the fundamental structure theorem for transitive actions: they are completely determined (up to isomorphism) by the conjugacy class of a point stabilizer.

# Examples

**Example 1** (p. 60): Kernel of $G \to \operatorname{Sym}(X)$ for a transitive action is the largest normal subgroup in $\operatorname{Stab}(x_0)$ (Proposition 4.9).

# Relationships

## Builds Upon
- **transitive-action**, **stabilizer**

## Related
- **homogeneous-g-set** — Synonym for transitive $G$-set

# Source Reference

Chapter 4: Groups Acting on Sets, "Transitive actions", Proposition 4.7, page 59.

# Verification Notes

- Definition source: Proposition 4.7, p. 59
- Confidence: HIGH — explicit theorem with proof
- Uncertainties: None
