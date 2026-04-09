---
# === CORE IDENTIFICATION ===
concept: Outer Automorphism Group
slug: outer-automorphism-group

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: automorphisms
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 50
section: "Extensions of groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Out(G)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - automorphism-group
  - inner-automorphism-group
extends: []
related:
  - extension-of-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between an inner and outer automorphism?"
---

# Quick Definition

The outer automorphism group $\operatorname{Out}(G)$ is the quotient $\operatorname{Aut}(G)/\operatorname{Inn}(G)$.

# Core Definition

$\operatorname{Out}(G) \stackrel{\text{def}}{=} \operatorname{Aut}(G)/\operatorname{Inn}(G)$ (Milne, p. 50). An extension $1 \to N \to G \to Q \to 1$ naturally gives a homomorphism $\theta: Q \to \operatorname{Out}(N)$.

# Prerequisites

- **Automorphism group** — $\operatorname{Out}(G)$ is a quotient of $\operatorname{Aut}(G)$
- **Inner automorphism group** — $\operatorname{Inn}(G)$ is the kernel of the projection

# Key Properties

1. $\operatorname{Out}(G) = 1$ if and only if every automorphism of $G$ is inner
2. Extensions of $Q$ by $N$ give rise to homomorphisms $Q \to \operatorname{Out}(N)$
3. $\operatorname{Ext}^1(Q,N)_\theta$ classifies extensions with a given $\theta: Q \to \operatorname{Out}(N)$

# Context & Application

$\operatorname{Out}(G)$ appears naturally in the classification of group extensions. It measures the "external symmetries" of $G$ not captured by conjugation.

# Examples

**Example 1** (p. 43): $\operatorname{Out}(S_n) = 1$ for $n \neq 2, 6$.

**Example 2** (p. 43): $\operatorname{Out}(S_6) \simeq C_2$.

# Relationships

## Builds Upon
- **automorphism-group** — Numerator of the quotient
- **inner-automorphism-group** — Denominator of the quotient

## Related
- **extension-of-groups** — Extensions give maps to $\operatorname{Out}(N)$
- **complete-group** — Has $\operatorname{Out}(G) = 1$ and $Z(G) = 1$

# Source Reference

Chapter 3: Automorphisms and Extensions, "Extensions of groups", page 50.

# Verification Notes

- Definition source: Direct from p. 50
- Confidence: HIGH — explicit definition
- Uncertainties: None
