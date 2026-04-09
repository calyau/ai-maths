---
# === CORE IDENTIFICATION ===
concept: Solvability of p-Groups
slug: solvability-of-p-groups

# === CLASSIFICATION ===
category: series-solvability
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 90
section: "Solvable groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - p-group
  - solvability-closure-properties
extends: []
related:
  - nilpotency-of-p-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is every p-group solvable?"
---

# Quick Definition

Every finite p-group is solvable. This follows from the fact that p-groups have nontrivial centers, combined with induction and the extension property of solvable groups.

# Core Definition

**Corollary 6.7.** A finite p-group is solvable.

Proof: By induction on |G|. The centre Z(G) is nontrivial (by 4.16), so G/Z(G) is solvable by induction. Since Z(G) is commutative, the extension property (Proposition 6.6b) shows G is solvable.

(Milne, Corollary 6.7, p. 90)

# Prerequisites

- **p-group** -- the hypothesis
- **solvability-closure-properties** -- extensions of solvable groups are solvable

# Key Properties

1. The proof is stronger: p-groups are actually nilpotent (Corollary 6.17), which implies solvable
2. The center Z(G) provides the base for the induction

# Relationships

## Builds Upon
- **solvability-closure-properties** -- the extension property

## Related
- **nilpotency-of-p-groups** -- the stronger result that p-groups are nilpotent

# Source Reference

Chapter 6, Corollary 6.7, p. 90.

# Verification Notes

- Definition source: Direct from Corollary 6.7
- Confidence rationale: HIGH -- explicit corollary
- Uncertainties: None
