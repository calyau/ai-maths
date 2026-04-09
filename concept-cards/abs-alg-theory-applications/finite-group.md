---
# === CORE IDENTIFICATION ===
concept: Finite Group
slug: finite-group

# === CLASSIFICATION ===
category: group-theory
subcategory: group-properties
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 49
section: "Definitions and Examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - group-order
extends:
  - group
related:
  - cyclic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

A finite group is a group containing a finite number of elements. Its order $|G|$ is the count of its elements.

# Core Definition

"A group is finite, or has finite order, if it contains a finite number of elements; otherwise, the group is said to be infinite or to have infinite order" (Judson, p. 49).

# Prerequisites

- **Group** — A finite group is a group
- **Group order** — Finite groups have finite order

# Key Properties

1. $|G| = n$ for some positive integer $n$
2. Every element has finite order dividing $|G|$
3. Can be completely described by a Cayley table
4. Examples: $\mathbb{Z}_n$, $U(n)$, $S_n$, $D_n$, $Q_8$

# Examples

**Example 1** (p. 49): $|\mathbb{Z}_5| = 5$.

**Example 2** (p. 48): $|U(8)| = 4$.

**Example 3** (p. 48): $|S_3| = 6$.

# Relationships

## Builds Upon
- **group** — A finite group is a group

## Related
- **group-order** — $|G|$ counts elements
- **cayley-table** — Practical for finite groups

# Source Reference

Chapter 3: Groups, Section 3.2, page 49.

# Verification Notes

- Definition source: Direct quote from p. 49
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
