---
concept: Direct Sum of Modules
slug: direct-sum-modules
category: module-theory
subcategory: basic-definitions
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Algebra in a Ring"
chapter_number: 14
pdf_page: 432
section: "14.7 Structure of Abelian Groups"
extraction_confidence: high
aliases:
  - "direct sum"
  - "internal direct sum"
prerequisites:
  - module
  - submodule
extends: []
related:
  - structure-theorem-finitely-generated-modules-pid
contrasts_with: []
answers_questions:
  - "What is a direct sum of modules?"
---

# Quick Definition

A module V is the direct sum of submodules W_1, ..., W_k if every element can be written uniquely as w_1 + ... + w_k with w_i in W_i. This means the submodules generate V and are independent.

# Core Definition

Let W_1, ..., W_k be submodules of an R-module V. V is the direct sum of these submodules, written V = W_1 + ... + W_k, if (Artin, p. 443, equations 14.7.1-14.7.2): (1) they generate: V = W_1 + ... + W_k, and (2) they are independent: if w_1 + ... + w_k = 0 with w_i in W_i, then w_i = 0 for all i.

# Prerequisites

- **Module** -- Direct sums are formed from modules
- **Submodule** -- The summands must be submodules

# Key Properties

1. V = W_1 + W_2 iff W_1 + W_2 = V and W_1 intersect W_2 = 0
2. Every element v has a unique representation v = w_1 + ... + w_k
3. The structure theorem decomposes modules as direct sums of cyclic modules

# Context & Application

Direct sums are the fundamental decomposition tool in module theory. The structure theorems for abelian groups and for modules over PIDs express modules as direct sums of simpler pieces.

# Examples

**Example 1** (p. 443): Z/6Z is isomorphic to Z/2Z + Z/3Z as a direct sum of cyclic groups.

# Relationships

## Builds Upon
- **Module** and **Submodule** -- The components

## Enables
- **Structure theorem for finitely generated modules over a PID** -- Decomposes into direct sums

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.7, pages 443-444.

# Verification Notes

- Definition source: Direct from Artin, p. 443
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
