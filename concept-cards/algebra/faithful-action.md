---
concept: Faithful Action
slug: faithful-action
category: symmetry
subcategory: group-actions
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Symmetry"
chapter_number: 6
pdf_page: 162
section: "6.11 Permutation Representations"
extraction_confidence: high
aliases: []
prerequisites:
  - group-action
  - permutation-representation
extends:
  - group-action
related:
  - cayleys-theorem
contrasts_with: []
answers_questions:
  - "What is a faithful group action?"
---

# Quick Definition

An action is faithful if the only group element that fixes every element of S is the identity. Equivalently, the associated permutation representation is injective.

# Core Definition

An operation is faithful if the only element g of G such that gs = s for every s in S is the identity (Artin, (6.11.4), p. 196). This means the permutation representation phi: G -> Perm(S) is injective.

# Prerequisites

- **Group action** — Faithfulness is a property of actions
- **Permutation representation** — Faithful means injective representation

# Key Properties

1. The kernel of the permutation representation is trivial
2. G embeds into Perm(S)
3. Left multiplication of G on itself is always faithful (used in Cayley's Theorem)

# Context & Application

Faithful actions allow embedding abstract groups into permutation groups. This is the basis of Cayley's Theorem (7.1.3). In applications, faithfulness ensures the group elements are distinguishable by their actions.

# Examples

**Example 1** (p. 196): The action of M on equilateral triangles is faithful.

**Example 2** (p. 196): GL_2(F_2) acts faithfully on the three nonzero vectors of F_2^2, giving an isomorphism GL_2(F_2) = S_3 (Example 6.11.5).

# Relationships

## Builds Upon
- **Permutation representation** — Faithful = injective representation

## Enables
- **Cayley's theorem** — Uses the faithful left multiplication action

# Common Confusions

- **Confusion**: Thinking faithful means transitive
  **Clarification**: Faithful means no nontrivial element fixes everything; transitive means one orbit. These are independent properties.

# Source Reference

Chapter 6: Symmetry, Section 6.11, (6.11.4), pages 196-197.

# Verification Notes

- Definition source: Direct from (6.11.4)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
