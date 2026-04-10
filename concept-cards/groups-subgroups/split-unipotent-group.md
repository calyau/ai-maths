---
concept: Split Unipotent Group
slug: split-unipotent-group
category: unipotent-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 180
section: "15b Unipotent affine groups"
extraction_confidence: high
aliases:
  - k-resoluble group
prerequisites:
  - unipotent-group
extends:
  - unipotent-group
related:
  - split-solvable-group
contrasts_with: []
answers_questions:
  - "What is a split unipotent group?"
---

# Quick Definition

A unipotent algebraic group is split if it admits a subnormal series whose quotients are isomorphic to G_a (not just subgroups of G_a). Split unipotent groups are automatically smooth and connected. Over perfect fields, every smooth connected unipotent group is split.

# Core Definition

A unipotent algebraic group is *split* if it admits a subnormal series whose quotients are isomorphic to G_a (Definition 15.20). Such a group is automatically smooth (7.66) and connected (13.21). Over a perfect field, every smooth connected unipotent algebraic group is split (Proposition 15.21, Milne, pp. 180-181).

# Prerequisites

- **Unipotent group** -- Split is a property of unipotent groups

# Key Properties

1. Automatically smooth and connected
2. Over perfect fields, smooth connected unipotent = split (Proposition 15.21)
3. Over non-perfect fields, non-split forms of G_a exist (Example 15.11)
4. Every form of G_a becomes isomorphic to G_a over a purely inseparable extension

# Examples

**Example 1** (p. 180): U_n is split: it has a subnormal series with quotients G_a^{n-r-1}.

**Example 2** (p. 179): Over a non-perfect field of char p, the subgroup of G_a x G_a defined by Y^p = X - aX^p (a not in k^p) is a non-split form of G_a.

# Relationships

## Builds Upon
- **Unipotent group** -- Split is a strengthening

## Enables
- **Split solvable group** -- Solvable groups with split unipotent radical

# Source Reference

Chapter I, Section 15b, pages 180-181. Definition 15.20, Proposition 15.21.

# Verification Notes

- Definition source: Direct from Definition 15.20
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
