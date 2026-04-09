---
# === CORE IDENTIFICATION ===
concept: "Cauchy's Theorem (from Sylow)"
slug: cauchys-theorem-from-sylow

# === CLASSIFICATION ===
category: sylow-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "The Sylow Theorems; Applications"
chapter_number: 5
pdf_page: 77
section: "The Sylow theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Cauchy's theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - sylow-first-theorem
extends: []
related:
  - sylow-p-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "If a prime p divides |G|, must G contain an element of order p?"
---

# Quick Definition

If a prime p divides the order of a finite group G, then G contains an element of order p. This follows immediately from Sylow's First Theorem.

# Core Definition

**Remark 5.4 (Cauchy's Theorem).** If a prime p divides (G : 1), then G has a subgroup of order p, and any nonidentity element of that subgroup has order p.

(Milne, Remark 5.4, p. 77)

# Prerequisites

- **group** -- the ambient finite group
- **sylow-first-theorem** -- Cauchy's theorem is an immediate corollary

# Key Properties

1. Guarantees the existence of elements of every prime order dividing |G|
2. The subgroup of order p guaranteed by Sylow I is cyclic (every group of prime order is cyclic)
3. Any nonidentity element of this cyclic subgroup has order p

# Context & Application

Cauchy's theorem is historically one of the earliest results in the structure theory of finite groups. Milne notes it as a corollary of Sylow I, though it can also be proved independently (as in Chapter 4 of the same text, Theorem 4.13).

# Examples

**Example 1**: If |G| = 12 = 2^2 * 3, Cauchy's theorem guarantees elements of order 2 and of order 3 in G.

# Relationships

## Builds Upon
- **sylow-first-theorem** -- Cauchy's theorem is the p^1 case

## Enables
- Understanding element orders in finite groups

## Related
- **sylow-p-subgroup** -- gives much more than Cauchy: subgroups of all prime-power orders dividing |G|

# Source Reference

Chapter 5, Remark 5.4, p. 77. Also proved independently in Chapter 4, Theorem 4.13.

# Verification Notes

- Definition source: Remark 5.4, p. 77
- Confidence rationale: HIGH -- explicitly noted as a corollary
- Uncertainties: None
