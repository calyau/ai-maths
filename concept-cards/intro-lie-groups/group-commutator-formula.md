---
# === CORE IDENTIFICATION ===
concept: Group Commutator Formula
slug: group-commutator-formula

# === CLASSIFICATION ===
category: lie-algebras
subcategory: exponential-map
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 23
section: "3.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "equation (3.3)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exponential-map
  - commutator-bracket
extends: []
related:
  - campbell-hausdorff-formula
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

The group commutator $\exp(x)\exp(y)\exp(-x)\exp(-y)$ equals $\exp([x, y] + \cdots)$ where dots are terms of degree 3 and higher. This directly connects the Lie bracket to the group commutator.

# Core Definition

**Proposition 3.12, part (3)** (Kirillov, equation 3.3):
$$\exp(x)\exp(y)\exp(-x)\exp(-y) = \exp([x, y] + \cdots)$$
where dots stand for terms of degree three and higher.

# Prerequisites

- **Exponential map** — used throughout
- **Commutator bracket** — the leading term of the result

# Key Properties

1. The leading non-trivial term is exactly $[x, y]$.
2. This explains the name "commutator" for $[x, y]$: it measures the non-commutativity of the group.
3. If $G$ is abelian, $[x, y] = 0$ for all $x, y$.
4. For matrix groups, this is proved by direct computation using $(1+x+\cdots)(1+y+\cdots)(1-x+\cdots)(1-y+\cdots) = 1 + (xy - yx) + \cdots$ (Example 3.13).

# Construction / Recognition

## To Construct/Create:
1. Compute $\exp(x)\exp(y)\exp(-x)\exp(-y)$ to second order.
2. Extract the bilinear term.

## To Identify/Recognize:
1. Any expression relating group commutators to Lie brackets.

# Context & Application

This formula is the intuitive explanation for why the Lie bracket is called the "commutator." It shows that the Lie bracket measures the failure of group elements to commute, at the infinitesimal level.

# Examples

**Example 3.13** (p. 23): For $G \subset \mathrm{GL}(n)$: $(1+x)(1+y)(1-x)(1-y) = 1 + (xy - yx) + \cdots$ gives $[x, y] = xy - yx$.

# Relationships

## Builds Upon
- **Commutator bracket** — appears as the leading term
- **Exponential map** — the formula uses exp

## Enables
- **Proof that Ad preserves bracket** — Proposition 3.12 part (2) follows from part (1)

## Related
- **Campbell-Hausdorff formula** — the full version of the group law

# Common Errors

- **Error**: Keeping only the $[x,y]$ term and ignoring higher-order terms.
  **Correction**: The higher-order terms exist and matter for finite (non-infinitesimal) group elements.

# Common Confusions

- **Confusion**: Whether this shows $[x,y] = 0 \Leftrightarrow \exp(x)\exp(y) = \exp(y)\exp(x)$.
  **Clarification**: $\Leftarrow$ is not immediate from this formula alone (the higher-order terms could conspire). The full equivalence follows from Theorem 3.33.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.2, Proposition 3.12 part (3), equation (3.3), page 23.

# Verification Notes

- Definition source: Direct from equation (3.3)
- Confidence rationale: Explicit formula
- Uncertainties: None
- Cross-reference status: Verified with Example 3.13
