---
# === CORE IDENTIFICATION ===
concept: Cyclic Groups Are Abelian
slug: cyclic-group-abelian

# === CLASSIFICATION ===
category: cyclic-groups
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Cyclic Groups"
chapter_number: 4
pdf_page: 60
section: "Cyclic Subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cyclic-group
  - abelian-group
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cyclic group?"
---

# Quick Definition

Every cyclic group is abelian: if $G = \langle a \rangle$, then $gh = hg$ for all $g, h \in G$.

# Core Definition

**Theorem 4.9**: "Every cyclic group is abelian" (Judson, p. 60).

**Proof**: If $g = a^r$ and $h = a^s$, then $gh = a^r a^s = a^{r+s} = a^{s+r} = a^s a^r = hg$.

# Prerequisites

- **Cyclic group** — The theorem applies to cyclic groups
- **Abelian group** — The conclusion is that the group is abelian

# Key Properties

1. The proof relies on commutativity of integer addition ($r + s = s + r$)
2. The converse is false: not every abelian group is cyclic
3. Example of converse failure: $\mathbb{Z}_2 \times \mathbb{Z}_2$ is abelian but not cyclic

# Context & Application

This theorem provides a quick test: if a group is not abelian, it cannot be cyclic. This immediately shows groups like $S_3$, $GL_2(\mathbb{R})$, and $Q_8$ are not cyclic.

# Examples

**Example 1** (p. 60): In $\mathbb{Z}_6 = \langle 1 \rangle$: $2 + 3 = 5 = 3 + 2$.

**Non-Example**: $\mathbb{Z}_2 \times \mathbb{Z}_2$ is abelian but NOT cyclic (no element has order 4).

# Relationships

## Builds Upon
- **cyclic-group** — Applies to cyclic groups
- **abelian-group** — Concludes abelianness

# Common Confusions

- **Confusion**: Thinking the converse holds (every abelian group is cyclic)
  **Clarification**: $\mathbb{Z}_2 \times \mathbb{Z}_2$ is abelian but not cyclic

# Source Reference

Chapter 4: Cyclic Groups, Section 4.1, Theorem 4.9, page 60.

# Verification Notes

- Definition source: Direct from Theorem 4.9
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
