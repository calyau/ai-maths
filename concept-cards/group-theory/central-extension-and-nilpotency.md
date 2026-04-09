---
# === CORE IDENTIFICATION ===
concept: Central Extension and Nilpotency
slug: central-extension-and-nilpotency

# === CLASSIFICATION ===
category: nilpotent-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 94
section: "Nilpotent groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nilpotent-group
  - center-of-group
extends: []
related:
  - nilpotent-subgroups-and-quotients
  - nilpotency-of-p-groups
  - solvable-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When does an extension of nilpotent groups remain nilpotent?"
  - "How are nilpotent groups built from abelian groups?"
---

# Quick Definition

If N is a subgroup of the center of G and G/N is nilpotent of class m, then G is nilpotent of class at most m+1. Thus nilpotent groups are precisely those obtained from abelian groups by successive central extensions, while solvable groups allow arbitrary extensions.

# Core Definition

**Corollary 6.16.** For any subgroup N of the centre of G,

G/N nilpotent of class m implies G nilpotent of class <= m+1.

The key contrast:
- The nilpotent groups are those that can be obtained from commutative groups by successive *central* extensions.
- The solvable groups are those that can be obtained from commutative groups by successive extensions (not necessarily central).

(Milne, Corollary 6.16 and subsequent discussion, p. 94)

# Prerequisites

- **nilpotent-group** -- the property being preserved
- **center-of-group** -- N must be central

# Key Properties

1. The proof uses the iterated commutator criterion: commutators of length m+1 map to 1 in G/N, so they lie in N subset Z(G), hence commutators of length m+2 vanish
2. General extensions of nilpotent groups need not be nilpotent
3. Central extensions always preserve nilpotency (with class increasing by at most 1)

# Context & Application

This result, combined with the nontriviality of Z(G) for p-groups, immediately gives that p-groups are nilpotent (Corollary 6.17). The characterization of nilpotent groups as "central extension towers" provides a conceptual way to understand them.

# Relationships

## Builds Upon
- **nilpotent-group** -- the property being preserved
- **center-of-group** -- centrality is the key condition

## Enables
- **nilpotency-of-p-groups** -- p-groups are nilpotent via this result

## Related
- **solvable-group** -- solvable groups use arbitrary extensions (weaker condition, larger class of groups)

# Source Reference

Chapter 6, Corollary 6.16, p. 94.

# Verification Notes

- Definition source: Direct from Corollary 6.16
- Confidence rationale: HIGH -- explicit corollary with proof
- Uncertainties: None
