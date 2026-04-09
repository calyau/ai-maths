---
# === CORE IDENTIFICATION ===
concept: Characteristic of a Finite Field
slug: characteristic-of-finite-field

# === CLASSIFICATION ===
category: field-theory
subcategory: finite-fields
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Finite Fields"
chapter_number: 22
pdf_page: 292
section: "22.1 Structure of a Finite Field"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - finite-field
  - characteristic-of-a-field
extends: []
related:
  - freshmans-dream
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the characteristic of a finite field?"
  - "Why must a finite field have prime characteristic?"
---

# Quick Definition

Every finite field has prime characteristic $p$, and its order is $p^n$ for some positive integer $n$. The prime subfield is isomorphic to $\mathbb{Z}_p$.

# Core Definition

**Proposition 22.1.** If $F$ is a finite field, then the characteristic of $F$ is $p$, where $p$ is prime (Judson, p. 292).

**Proposition 22.2.** If $F$ is a finite field of characteristic $p$, then the order of $F$ is $p^n$ for some $n \in \mathbb{N}$ (p. 292).

The prime subfield (the image of $\mathbb{Z} \to F$) is isomorphic to $\mathbb{Z}_p$, and $F$ is a finite-dimensional vector space over this subfield.

# Prerequisites

- **Finite field** — This characterizes finite fields
- **Characteristic of a field** — The smallest $p$ with $p \cdot 1 = 0$

# Key Properties

1. The characteristic must be prime (Proposition 22.1)
2. The order is $p^n$ where $n$ is the degree $[F:\mathbb{Z}_p]$ (Proposition 22.2)
3. The prime subfield $\mathbb{Z}_p$ is contained in every finite field of characteristic $p$

# Examples

**Example 1**: $GF(4) = \mathbb{Z}_2[x]/\langle x^2 + x + 1 \rangle$ has characteristic 2 and order $2^2 = 4$.

**Example 2**: $GF(27) = \mathbb{Z}_3[x]/\langle f(x) \rangle$ (for appropriate irreducible cubic) has characteristic 3 and order $3^3 = 27$.

# Relationships

## Builds Upon
- **Finite field** — Characterizes the structure
- **Characteristic of a field** — The prime dividing the order

## Related
- **Freshman's Dream** — Uses prime characteristic

# Source Reference

Chapter 22: Finite Fields, Section 22.1, page 292. Propositions 22.1, 22.2.

# Verification Notes

- Definition source: Direct from Propositions 22.1 and 22.2
- Confidence: HIGH — explicit propositions
- Cross-reference status: Verified
- Uncertainties: None
