---
concept: Split Solvable Group
slug: split-solvable-group
category: solvable-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 192
section: "16f Split solvable groups"
extraction_confidence: high
aliases: []
prerequisites:
  - solvable-algebraic-group
  - split-unipotent-group
extends:
  - solvable-algebraic-group
related: []
contrasts_with: []
answers_questions:
  - "What is a split solvable group?"
---

# Quick Definition

A solvable algebraic group is split if it admits a subnormal series whose quotients are G_a or G_m. Such groups are automatically smooth and connected. Any quotient of a split solvable group is again split solvable.

# Core Definition

A solvable algebraic group is *split* if it admits a subnormal series whose quotients are G_a or G_m (Definition 16.34). Such a group is automatically smooth and connected. Any quotient of a split solvable group is again split solvable (Milne, p. 192).

# Prerequisites

- **Solvable algebraic group** -- The base concept
- **Split unipotent group** -- The unipotent part must be split

# Key Properties

1. Automatically smooth and connected
2. Quotients of split solvable groups are split solvable
3. Generalizes both split tori and split unipotent groups
4. Consistent with the definition of "split unipotent"

# Examples

**Example 1** (p. 192): T_n (upper triangular matrices) is split solvable: the series T_n > U_n > ... > 1 has quotients G_m^n, G_a^{n-1}, G_a^{n-2}, ..., G_a.

# Relationships

## Builds Upon
- **Solvable algebraic group** -- Split is a strengthening

# Source Reference

Chapter I: Basic Theory of Affine Groups, Section 16f, page 192. Definition 16.34.

# Verification Notes

- Definition source: Direct from Definition 16.34
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
