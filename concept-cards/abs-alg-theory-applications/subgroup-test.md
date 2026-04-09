---
# === CORE IDENTIFICATION ===
concept: Subgroup Test
slug: subgroup-test

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
pdf_page: 52
section: "Some Subgroup Theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - two-step subgroup test
  - one-step subgroup test

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
  - group
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a subgroup?"
  - "How do I determine if a set with an operation forms a group?"
---

# Quick Definition

The subgroup tests provide efficient criteria for determining whether a subset of a group is a subgroup, without verifying all group axioms from scratch.

# Core Definition

**Two-Step Test (Proposition 3.30)**: A subset $H$ of $G$ is a subgroup if and only if:
1. $e \in H$
2. If $h_1, h_2 \in H$, then $h_1 h_2 \in H$ (closure)
3. If $h \in H$, then $h^{-1} \in H$ (inverses)

**One-Step Test (Proposition 3.31)**: $H$ is a subgroup of $G$ if and only if $H \neq \emptyset$ and whenever $g, h \in H$, then $gh^{-1} \in H$.

(Judson, pp. 52-53).

# Prerequisites

- **Subgroup** — The tests determine subgroup membership
- **Group** — Applied within a group

# Key Properties

1. The two-step test checks identity, closure, and inverses separately
2. The one-step test combines all conditions into a single check
3. Associativity is inherited from $G$ and need not be checked
4. Both tests are equivalent to the full group axioms

# Construction / Recognition

## To Apply the One-Step Subgroup Test:
1. Verify $H \neq \emptyset$
2. Take arbitrary $g, h \in H$
3. Show $gh^{-1} \in H$
4. If so, $H$ is a subgroup

## Why the One-Step Test Works:
- If $g \in H$: $gg^{-1} = e \in H$ (identity)
- If $g \in H$: $eg^{-1} = g^{-1} \in H$ (inverses)
- If $h_1, h_2 \in H$: $h_1(h_2^{-1})^{-1} = h_1 h_2 \in H$ (closure)

# Context & Application

The subgroup tests are among the most frequently used tools in group theory. They allow efficient verification that a subset is a subgroup without checking associativity (which is inherited from the ambient group).

# Examples

**Example 1** (p. 51): To show $\mathbb{Q}^*$ is a subgroup of $\mathbb{R}^*$: $1 = 1/1 \in \mathbb{Q}^*$ (identity); if $p/q, r/s \in \mathbb{Q}^*$, then $(p/q)(r/s) = pr/qs \in \mathbb{Q}^*$ (closure); $(p/q)^{-1} = q/p \in \mathbb{Q}^*$ (inverses).

# Relationships

## Builds Upon
- **subgroup** — The tests determine subgroup membership
- **group** — Associativity inherited from ambient group

# Common Errors

- **Error**: Forgetting to check that $H \neq \emptyset$ in the one-step test
  **Correction**: The nonempty condition is essential; the empty set is never a subgroup

# Common Confusions

- **Confusion**: Thinking you must verify associativity for $H$
  **Clarification**: Associativity is inherited from $G$; you only need identity, closure, and inverses

# Source Reference

Chapter 3: Groups, Section 3.3, Propositions 3.30 and 3.31, pages 52-53.

# Verification Notes

- Definition source: Direct from Propositions 3.30-3.31
- Confidence: HIGH — explicit propositions with proofs
- Cross-reference status: Verified
- Uncertainties: None
