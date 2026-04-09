---
# === CORE IDENTIFICATION ===
concept: Inverse Uniqueness
slug: inverse-uniqueness

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
section: "Basic Properties of Groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - identity-element-uniqueness
  - group-cancellation-laws
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

In a group, each element has exactly one inverse. If $g' g = g g' = e$ and $g'' g = g g'' = e$, then $g' = g''$.

# Core Definition

**Proposition 3.18**: "If $g$ is any element in a group $G$, then the inverse of $g$, denoted by $g^{-1}$, is unique" (Judson, p. 49).

Additional properties:
- **Proposition 3.19**: $(ab)^{-1} = b^{-1}a^{-1}$
- **Proposition 3.20**: $(a^{-1})^{-1} = a$

# Prerequisites

- **Group** — Inverse uniqueness is a property of groups

# Key Properties

1. Each element has exactly one inverse
2. $(ab)^{-1} = b^{-1}a^{-1}$ (order reverses, "socks-shoes" property)
3. $(a^{-1})^{-1} = a$ (double inverse returns the original element)

# Context & Application

Uniqueness of inverses ensures the notation $g^{-1}$ is well-defined and that the cancellation laws hold in groups.

# Examples

**Example 1** (p. 49): If $g'$ and $g''$ are both inverses of $g$, then $g' = g'e = g'(gg'') = (g'g)g'' = eg'' = g''$.

# Relationships

## Builds Upon
- **group** — Property of groups

## Related
- **identity-element-uniqueness** — Parallel result for identities
- **group-cancellation-laws** — Follows from inverse uniqueness

# Source Reference

Chapter 3: Groups, Section 3.2, Propositions 3.18-3.20, pages 49-50.

# Verification Notes

- Definition source: Direct from Propositions 3.18-3.20
- Confidence: HIGH — explicit propositions with proofs
- Cross-reference status: Verified
- Uncertainties: None
