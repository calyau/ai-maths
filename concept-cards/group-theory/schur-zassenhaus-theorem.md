---
# === CORE IDENTIFICATION ===
concept: Schur-Zassenhaus Theorem
slug: schur-zassenhaus-theorem

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: extensions
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 50
section: "Extensions of groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extension-of-groups
  - split-extension
extends: []
related:
  - semidirect-product
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When does a group extension split?"
---

# Quick Definition

An extension of finite groups of relatively prime order always splits.

# Core Definition

"An extension of finite groups of relatively prime order is split" (Milne, Theorem 3.21, p. 50). That is, if $1 \to N \to G \to Q \to 1$ is exact with $\gcd(|N|, |Q|) = 1$, then the extension splits, and $G \simeq N \rtimes Q$ for some action.

# Prerequisites

- **Extension of groups** — The theorem applies to group extensions
- **Split extension** — The conclusion is that the extension splits

# Key Properties

1. Requires $\gcd(|N|, |Q|) = 1$
2. Guarantees the existence of a complement $Q' \leq G$ with $G = N \rtimes Q'$
3. When $N$ and $Q$ are both abelian, the proof follows from properties of $\operatorname{Ext}^1$ (p. 50)

# Context & Application

The Schur-Zassenhaus theorem is a fundamental tool in finite group theory. It shows that "coprime extensions" are always semidirect products, reducing the extension problem to understanding the possible actions.

# Examples

**Example 1** (p. 63): A group of order $99 = 9 \times 11$ has a normal subgroup of order 11 (by Cauchy), and since $\gcd(11, 9) = 1$, the extension splits.

# Relationships

## Builds Upon
- **extension-of-groups**, **split-extension**

## Enables
- Analysis of groups whose order factors into coprime parts

# Source Reference

Chapter 3: Automorphisms and Extensions, "Extensions of groups", Theorem 3.21, page 50.

# Verification Notes

- Definition source: Theorem 3.21, p. 50
- Confidence: HIGH — explicit theorem statement
- Uncertainties: Proof referenced to Rotman 1995, 7.41
