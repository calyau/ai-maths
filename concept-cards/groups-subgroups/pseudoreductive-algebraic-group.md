---
concept: Pseudoreductive Algebraic Group
slug: pseudoreductive-algebraic-group
category: group-structure
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 200
section: "17f Pseudoreductive groups"
extraction_confidence: high
aliases:
  - "pseudo-reductive group"
prerequisites:
  - reductive-algebraic-group
  - unipotent-radical
extends: []
related:
  - reductive-algebraic-group
contrasts_with:
  - reductive-algebraic-group
answers_questions:
  - "What is a reductive algebraic group?"
---

# Quick Definition

A pseudoreductive algebraic group is a smooth connected algebraic group whose unipotent radical (over k, not k^{al}) is trivial. Over perfect fields, pseudoreductive equals reductive.

# Core Definition

An algebraic group G over a field k is **pseudoreductive** if it is smooth and connected and its unipotent radical R_uG is trivial (Milne, Definition 17.5c). Over imperfect fields, this is strictly weaker than reductive: R_uG = 1 does not imply R_u(G_{k^{al}}) = 1.

# Prerequisites

- **Reductive algebraic group** -- Pseudoreductive is a weakening of reductive
- **Unipotent radical** -- The defining condition involves R_uG

# Key Properties

1. Over perfect fields, pseudoreductive = reductive (Proposition 17.6b)
2. Over imperfect fields, pseudoreductive groups can fail to be reductive (Example 17.22)
3. The structure theory of pseudoreductive groups is given by Conrad-Gabber-Prasad (2010)
4. Commutative pseudoreductive groups over imperfect fields are very complicated (17.24)

# Context & Application

Pseudoreductive groups arise naturally over imperfect fields (e.g., function fields in positive characteristic). Their structure is much more complex than reductive groups and was only classified by Conrad, Gabber, and Prasad in 2010.

# Examples

**Example 1** (p. 200): Let k be separably closed of characteristic p, and let k' be an extension of degree p. Then (G_m)_{k'/k} is pseudoreductive but not reductive: it has no unipotent subgroup over k, but over k^{al} it decomposes to reveal unipotent components.

# Relationships

## Builds Upon
- **Reductive algebraic group** -- Pseudoreductive weakens the condition from R_u(G_{k^{al}}) = 1 to R_uG = 1

## Contrasts With
- **Reductive algebraic group** -- Reductive requires the geometric unipotent radical to vanish

# Common Confusions

- **Confusion**: Assuming pseudoreductive and reductive are the same
  **Clarification**: They coincide over perfect fields but differ over imperfect fields

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 17f, pages 200-202.

# Verification Notes

- Definition source: Direct from Definition 17.5c
- Confidence rationale: Explicit definition with counterexample
- Uncertainties: None
- Cross-reference status: Verified
