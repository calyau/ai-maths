---
# === CORE IDENTIFICATION ===
concept: Flag
slug: flag

# === CLASSIFICATION ===
category: structure-theory
subcategory: solvable-nilpotent
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 68
section: "6.2. Solvable and nilpotent Lie algebras"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "complete flag"
  - "partial flag"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
extends: []
related:
  - solvable-lie-algebra
  - nilpotent-lie-algebra
  - borel-subalgebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a flag in the context of Lie algebra structure theory?"
---

# Quick Definition

A flag $\mathcal{F}$ in a vector space $V$ is a nested chain of subspaces $\{0\} \subset V_1 \subset V_2 \subset \cdots \subset V_n = V$. Flags are used to define the Borel and nilpotent subalgebras that provide key examples of solvable and nilpotent Lie algebras.

# Core Definition

A flag in a finite-dimensional vector space $V$ is a sequence of subspaces (Kirillov, p. 68):

$$\mathcal{F} = (\{0\} \subset V_1 \subset V_2 \subset \cdots \subset V_n = V)$$

with $\dim V_i < \dim V_{i+1}$. Associated Lie algebras:

$$\mathfrak{b}(\mathcal{F}) = \{x \in \mathfrak{gl}(V) \mid xV_i \subset V_i\}, \quad \mathfrak{n}(\mathcal{F}) = \{x \in \mathfrak{gl}(V) \mid xV_i \subset V_{i-1}\}.$$

# Prerequisites

- **Lie algebra** — Flags define subalgebras of $\mathfrak{gl}(V)$

# Key Properties

1. $\mathfrak{b}(\mathcal{F})$ (flag-preserving operators) is a solvable Lie algebra
2. $\mathfrak{n}(\mathcal{F})$ (flag-lowering operators) is a nilpotent Lie algebra
3. For the standard flag in $\mathbb{K}^n$, $\mathfrak{b}(\mathcal{F})$ is upper-triangular matrices and $\mathfrak{n}(\mathcal{F})$ is strictly upper-triangular
4. $[\mathfrak{a}_k, \mathfrak{a}_l] \subset \mathfrak{a}_{k+l}$ where $\mathfrak{a}_k = \{x \mid xV_i \subset V_{i-k}\}$

# Construction / Recognition

## To Construct:
1. Choose an ordered basis $v_1, \ldots, v_n$ of $V$
2. Set $V_i = \operatorname{span}(v_1, \ldots, v_i)$
3. The resulting flag gives upper-triangular and strictly upper-triangular subalgebras

# Context & Application

Flags provide the canonical examples of solvable and nilpotent Lie algebras. The Lie theorem states that any representation of a solvable algebra admits a flag preserved by the algebra, generalizing Jordan normal form.

# Examples

**Example 6.12** (p. 68): The standard flag in $\mathbb{K}^n$ gives $\mathfrak{b}$ = upper-triangular matrices (solvable) and $\mathfrak{n}$ = strictly upper-triangular matrices (nilpotent). Moreover, $\mathfrak{b}$ is solvable but not nilpotent.

# Relationships

## Enables
- **Solvable Lie algebra** — $\mathfrak{b}(\mathcal{F})$ provides canonical examples
- **Nilpotent Lie algebra** — $\mathfrak{n}(\mathcal{F})$ provides canonical examples

# Common Confusions

- **Confusion**: Thinking $\mathfrak{b}(\mathcal{F})$ is nilpotent
  **Clarification**: $\mathfrak{b}(\mathcal{F})$ is only solvable; $\mathfrak{n}(\mathcal{F})$ is nilpotent

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.2, pages 68-69. Example 6.12.

# Verification Notes

- Definition source: Synthesized from Example 6.12 discussion
- Confidence rationale: Medium — concept is used in examples but not given a formal definition number
- Uncertainties: The flag itself is not formally defined here; Kirillov references Example 2.23
- Cross-reference status: Verified
